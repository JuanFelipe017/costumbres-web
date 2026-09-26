# Generador de páginas (no se publica)

Genera las 14 páginas del sitio (ES en la raíz, EN en `en/`) desde una sola estructura por página,
para que español e inglés nunca se desincronicen.

```bash
python herramientas/build.py Costumbres_Web
```

- Datos del negocio (WhatsApp, dirección, NIT, redes): `common.py` (`WA_NUMBER`, `D`, `T`).
- Textos de cada página: diccionario `S = {"es": ..., "en": ...}` en cada `*_page.py`.
- Páginas legales: `legal_pages.py`. Página 404: `error_page.py`.

Después de generar, verificar con la skill:
`python .claude/skills/sitio-web-negocio/scripts/verificar.py Costumbres_Web`
