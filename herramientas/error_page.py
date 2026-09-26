from common import *

S = {
    "es": {
        "title": "Página no encontrada | Costumbres",
        "desc": "La página que buscas no existe o cambió de lugar.",
        "code": "Error 404",
        "h1": "Esta página se nos destejió",
        "lead": "No encontramos lo que buscabas. Puede que el enlace esté roto o que la página haya cambiado de lugar.",
        "home": "Volver al inicio",
        "cats": "Ver categorías",
        "wa_pre": "¿Buscabas una pieza en especial?",
        "wa_link": "Escríbenos por WhatsApp",
        "wa_msg": "Hola, Costumbres. Estaba buscando algo en su página y no lo encontré.",
    },
    "en": {
        "title": "Page not found | Costumbres",
        "desc": "The page you are looking for doesn't exist or has moved.",
        "code": "Error 404",
        "h1": "This page came unwoven",
        "lead": "We couldn't find what you were looking for. The link may be broken or the page may have moved.",
        "home": "Back to home",
        "cats": "See categories",
        "wa_pre": "Looking for a specific piece?",
        "wa_link": "Message us on WhatsApp",
        "wa_msg": "Hi Costumbres, I was looking for something on your website and couldn't find it.",
    },
}


def body(lang, L):
    s = S[lang]
    return f"""    <main id="contenido" class="pt-20">
        <section class="min-h-[70vh] flex items-center justify-center px-margin-mobile md:px-margin-desktop py-24">
            <div class="max-w-2xl mx-auto text-center" data-anim="hero">
                <p class="font-label-md text-label-md text-on-primary-fixed-variant bg-surface-container-low px-4 py-1 rounded-full mb-6 inline-block border border-outline-variant/30">{s["code"]}</p>
                <h1 class="font-display-lg text-display-lg-mobile md:text-display-lg text-primary mb-6 leading-tight">{s["h1"]}</h1>
                <p class="font-body-lg text-body-lg text-on-surface-variant mb-10 text-balance">{s["lead"]}</p>
                <div class="flex flex-col sm:flex-row gap-4 justify-center">
                    <a class="{BTN_PRIMARY}" href="{L}index.html">{s["home"]}</a>
                    <a class="{BTN_OUTLINE}" href="{L}categorias.html">{s["cats"]}</a>
                </div>
                <p class="mt-10 font-body-md text-body-md text-on-surface-variant">{s["wa_pre"]}
                    <a class="underline underline-offset-4 text-on-primary-fixed-variant" href="{wa(s["wa_msg"])}" target="_blank" rel="noopener">{s["wa_link"]}</a></p>
            </div>
        </section>
    </main>
"""


def build(lang):
    # Rutas desde la raíz: el 404 se muestra en cualquier URL (p. ej. /en/a/b/c)
    P = "/"
    L = "/" if lang == "es" else "/en/"
    alt = "/en/index.html" if lang == "es" else "/index.html"
    here = L + "index.html"
    s = S[lang]
    return page(lang, P, "404", alt, s["title"], s["desc"], [], body(lang, L), ["nav"],
                L=L, here_href=here, extra_head='    <meta name="robots" content="noindex" />')
