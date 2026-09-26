"""Genera las páginas ES (raíz) y EN (en/) del sitio a partir de los módulos *_page.py.

Uso:  python build.py <carpeta_del_sitio>
Ejemplo (Costumbres): python build.py "C:/.../Costumbres_Web"

Cada *_page.py tiene UNA función de estructura y un diccionario de textos S = {"es": ..., "en": ...},
así ES y EN nunca se desincronizan. Los datos del negocio (WhatsApp, dirección, NIT...) están en common.py.
"""
import io, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import index_page, categorias_page, historia_page, contacto_page, legal_pages, error_page

if len(sys.argv) < 2:
    sys.exit("Uso: python build.py <carpeta_del_sitio>")
ROOT = sys.argv[1]

for lang in ("es", "en"):
    base = ROOT if lang == "es" else os.path.join(ROOT, "en")
    os.makedirs(base, exist_ok=True)
    out = {
        "index": index_page.build(lang),
        "categorias": categorias_page.build(lang),
        "historia": historia_page.build(lang),
        "contacto": contacto_page.build(lang),
        "privacidad": legal_pages.build(lang, "privacidad"),
        "terminos": legal_pages.build(lang, "terminos"),
        "404": error_page.build(lang),
    }
    for name, html in out.items():
        io.open(os.path.join(base, name + ".html"), "w", encoding="utf-8", newline="\n").write(html)
        print(lang, name, len(html))
