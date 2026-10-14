"""Plantillas compartidas (head, nav, footer) para generar las páginas ES/EN de Costumbres.
Script de un solo uso: el resultado son HTML estáticos normales."""
from urllib.parse import quote, quote_plus

# ---- Datos del negocio (un solo lugar) ----
WA_NUMBER = "573000000000"  # PENDIENTE: número real
EMAIL = "costumbres.co@hotmail.com"
INSTAGRAM = "https://www.instagram.com/costumbres.co/"
MAP_QUERY = "Calle 16 #5-24 Local 11, Bogotá, Colombia"
MAP_EMBED = "https://www.google.com/maps?q=" + quote_plus(MAP_QUERY) + "&amp;output=embed"
MAP_OPEN = "https://www.google.com/maps/search/?api=1&amp;query=" + quote_plus(MAP_QUERY)

D = {
    "es": {
        "address": "Calle 16 # 5-24, Local 11",
        "city": "Centro Histórico, Bogotá, Colombia",
        "days": "Lunes a sábado",
        "hours": "10:00 a. m. – 7:00 p. m.",
        "legal_name": "[RAZÓN SOCIAL]",
        "nit": "NIT [000.000.000-0]",
    },
    "en": {
        "address": "Calle 16 # 5-24, Local 11",
        "city": "Historic Center, Bogotá, Colombia",
        "days": "Monday to Saturday",
        "hours": "10:00 AM – 7:00 PM",
        "legal_name": "[LEGAL BUSINESS NAME]",
        "nit": "Tax ID (NIT) [000.000.000-0]",
    },
}

ICONS = sorted([
    "arrow_forward", "chat", "close", "eco", "energy_savings_leaf", "expand_more",
    "format_quote", "location_on", "mail", "map", "menu", "open_in_new", "pause",
    "play_arrow", "schedule", "verified", "chevron_left", "chevron_right", "zoom_in",
])

LAZY = 'loading="lazy" decoding="async"'


def wa(text):
    return f"https://wa.me/{WA_NUMBER}?text=" + quote(text)


def icon(name, cls=""):
    c = ("material-symbols-outlined " + cls).strip()
    return f'<span class="{c}" aria-hidden="true">{name}</span>'


WA_SVG = ('<svg class="w-6 h-6 fill-current" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"></path></svg>')

T = {
    "es": {
        "skip": "Saltar al contenido",
        "nav_label": "Principal",
        "home_label": "Costumbres, inicio",
        "nav": [("index", "Tienda"), ("categorias", "Categorías"), ("historia", "Historia"), ("contacto", "Contacto")],
        "menu_open": "Abrir menú", "menu_close": "Cerrar menú",
        "lang_label": "Idioma",
        "foot_desc": "Joyería con certificado de garantía y artesanía colombiana hecha a mano, con el alma de nuestra gente.",
        "explore": "Explorar",
        "explore_links": [("index", "Inicio"), ("categorias", "Categorías"), ("historia", "Historia"), ("contacto", "Contacto")],
        "social": "Redes",
        "legal": "Legal",
        "legal_links": [("privacidad.html", "Política de privacidad"), ("privacidad.html#cookies", "Política de cookies"),
                        ("terminos.html", "Términos y condiciones"), ("terminos.html#garantia", "Garantía y devoluciones")],
        "logo_alt": "Costumbres Joyería y Artesanía",
        "copy": "© 2026 Costumbres Joyería y Artesanía.",
        "sic": 'Si tienes una queja, escríbenos primero; también puedes acudir a la <a class="underline underline-offset-4 hover:text-on-primary-fixed-variant" href="https://www.sic.gov.co" target="_blank" rel="noopener">Superintendencia de Industria y Comercio</a>.',
        "og_locale": "es_CO",
        "consent": 'Al escribirnos por WhatsApp o correo aceptas el tratamiento de tus datos según nuestra <a class="underline underline-offset-4 hover:text-on-primary-fixed-variant" href="privacidad.html">política de privacidad</a>.',
        "map_note": 'Al cargar el mapa, Google puede usar cookies. <a class="underline underline-offset-4" href="privacidad.html#cookies">Más información</a>',
        "map_load": "Cargar mapa",
        "map_open": "Abrir en Google Maps",
        "map_title": "Ubicación de Costumbres en Bogotá",
        "fab_label": "Escríbenos por WhatsApp",
        "fab_msg": "Hola, Costumbres. Vengo desde su página web y tengo una consulta.",
    },
    "en": {
        "skip": "Skip to content",
        "nav_label": "Main",
        "home_label": "Costumbres, home",
        "nav": [("index", "Shop"), ("categorias", "Categories"), ("historia", "Our Story"), ("contacto", "Contact")],
        "menu_open": "Open menu", "menu_close": "Close menu",
        "lang_label": "Language",
        "foot_desc": "Jewelry with a warranty certificate and handmade Colombian crafts, with the soul of our people.",
        "explore": "Explore",
        "explore_links": [("index", "Home"), ("categorias", "Categories"), ("historia", "Our Story"), ("contacto", "Contact")],
        "social": "Follow us",
        "legal": "Legal",
        "legal_links": [("privacidad.html", "Privacy policy"), ("privacidad.html#cookies", "Cookie policy"),
                        ("terminos.html", "Terms and conditions"), ("terminos.html#garantia", "Warranty and returns")],
        "logo_alt": "Costumbres Jewelry & Handcrafts",
        "copy": "© 2026 Costumbres Jewelry & Handcrafts.",
        "sic": 'If you have a complaint, please contact us first; you can also reach Colombia\'s consumer authority, the <a class="underline underline-offset-4 hover:text-on-primary-fixed-variant" href="https://www.sic.gov.co" target="_blank" rel="noopener">Superintendencia de Industria y Comercio</a>.',
        "og_locale": "en_US",
        "consent": 'By messaging us on WhatsApp or by email you agree to the processing of your data as described in our <a class="underline underline-offset-4 hover:text-on-primary-fixed-variant" href="privacidad.html">privacy policy</a>.',
        "map_note": 'Loading the map lets Google set cookies. <a class="underline underline-offset-4" href="privacidad.html#cookies">Learn more</a>',
        "map_load": "Load map",
        "map_open": "Open in Google Maps",
        "map_title": "Costumbres location in Bogotá",
        "fab_label": "Message us on WhatsApp",
        "fab_msg": "Hi Costumbres, I'm writing from your website and I have a question.",
    },
}

LINK = "text-on-surface-variant hover:text-on-primary-fixed-variant transition-colors hover:underline decoration-primary/30 underline-offset-4 inline-block py-1"
BTN_PRIMARY = "bg-primary text-on-primary-fixed px-8 py-4 rounded-full font-label-md text-label-md shadow-lg shadow-primary/20 inline-flex items-center justify-center gap-2 text-center press-anim overlay-anim overlay-anim--claro"
BTN_OUTLINE = "border-2 border-primary text-on-primary-fixed-variant px-8 py-4 rounded-full font-label-md text-label-md inline-flex items-center justify-center gap-2 text-center press-anim overlay-anim"
BTN_WA = "inline-flex items-center gap-3 bg-whatsapp text-on-surface px-8 py-4 rounded-full font-label-md text-label-md shadow-lg shadow-whatsapp/20 press-anim overlay-anim overlay-anim--claro"


def head(lang, P, title, desc, css):
    t = T[lang]
    css_links = "\n".join(f'    <link href="{P}css/{c}.css" rel="stylesheet" />' for c in ["base"] + css)
    return f'''<!DOCTYPE html>

<html class="light" lang="{lang}">

<head>
    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <title>{title}</title>
    <meta name="description" content="{desc}" />
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="Costumbres" />
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{desc}" />
    <meta property="og:locale" content="{t["og_locale"]}" />
    <!-- Al publicar en Cloudflare: agregar og:image, <link rel="canonical"> y <link rel="alternate" hreflang> con la URL absoluta del dominio -->
    <link rel="icon" type="image/png" href="{P}img/logos/tortuga-96.png" />
    <link rel="apple-touch-icon" href="{P}img/logos/tortuga-192.png" />
    <link href="https://fonts.googleapis.com" rel="preconnect" />
    <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect" />
    <link
        href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;600&amp;family=Bricolage+Grotesque:wght@600;700;800&amp;display=swap"
        rel="stylesheet" />
    <link
        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0..1,0&amp;icon_names={",".join(ICONS)}&amp;display=block"
        rel="stylesheet" />
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <script src="{P}js/tailwind-config.js"></script>
    <script src="{P}js/animaciones.js"></script>
{css_links}
    <link href="{P}css/animaciones.css" rel="stylesheet" />
</head>
'''


def nav(lang, P, page, alt_href, L="", here_href=None):
    t = T[lang]
    desk, mob = [], []
    for key, label in t["nav"]:
        if key == page:
            desk.append(f'                <a class="font-label-md text-label-md text-on-primary-fixed-variant border-b-2 border-primary pb-1"\n                    href="{L}{key}.html" aria-current="page">{label}</a>')
            mob.append(f'            <a class="block py-3 font-label-md text-label-md text-on-primary-fixed-variant font-bold" href="{L}{key}.html" aria-current="page">{label}</a>')
        else:
            desk.append(f'                <a class="font-label-md text-label-md text-on-surface-variant hover:text-on-primary-fixed-variant transition-colors duration-300"\n                    href="{L}{key}.html">{label}</a>')
            mob.append(f'            <a class="block py-3 font-label-md text-label-md text-on-surface-variant" href="{L}{key}.html">{label}</a>')
    here = here_href or f"{page}.html"
    es_href, en_href = (here, alt_href) if lang == "es" else (alt_href, here)
    on = 'text-on-primary-fixed-variant bg-surface-container-low" aria-current="true'
    off = "text-on-surface-variant hover:text-on-primary-fixed-variant"
    es_cls, en_cls = (on, off) if lang == "es" else (off, on)
    lang_desk = f'''                <div class="flex items-center gap-1 border-l border-outline-variant/40 pl-6" role="group" aria-label="{t["lang_label"]}">
                    <a href="{es_href}" hreflang="es" lang="es" title="Español"
                        class="flex items-center gap-2 px-3 py-2 rounded-full font-label-md text-label-md transition-colors {es_cls}">
                        <img src="https://flagcdn.com/24x18/co.png" alt="" width="24" height="18" class="rounded-sm shadow-sm" />ES
                    </a>
                    <a href="{en_href}" hreflang="en" lang="en" title="English"
                        class="flex items-center gap-2 px-3 py-2 rounded-full font-label-md text-label-md transition-colors {en_cls}">
                        <img src="https://flagcdn.com/24x18/us.png" alt="" width="24" height="18" class="rounded-sm shadow-sm" />EN
                    </a>
                </div>'''
    es_m = 'text-on-primary-fixed-variant font-bold" aria-current="true' if lang == "es" else "text-on-surface-variant"
    en_m = 'text-on-primary-fixed-variant font-bold" aria-current="true' if lang == "en" else "text-on-surface-variant"
    nl = "\n"
    return f'''
<body
    class="bg-background text-on-surface selection:bg-primary selection:text-on-primary font-body-md overflow-x-hidden organic-texture">
    <a href="#contenido"
        class="sr-only focus:not-sr-only focus:fixed focus:top-3 focus:left-3 focus:z-[60] focus:bg-surface focus:text-on-primary-fixed-variant focus:px-5 focus:py-3 focus:rounded-full focus:shadow-md font-label-md text-label-md">{t["skip"]}</a>
    <!-- TopNavBar -->
    <nav aria-label="{t["nav_label"]}"
        class="site-nav fixed top-0 w-full z-50 bg-surface/90 backdrop-blur-md border-b border-outline-variant/30">
        <div
            class="flex justify-between items-center px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto h-20">
            <a href="{L}index.html" aria-label="{t["home_label"]}" class="rounded-lg transition-transform active:scale-95 flex items-center gap-3">
                <img alt="" class="h-12 md:h-14 w-auto" src="{P}img/logos/tortuga-nav.png" width="104" height="56" />
                <span
                    class="font-headline-md text-headline-md font-bold text-primary tracking-tight hidden sm:inline">Costumbres</span>
            </a>
            <div class="hidden md:flex items-center gap-8">
{nl.join(desk)}
{lang_desk}
            </div>
            <button id="menu-toggle" type="button"
                class="md:hidden w-11 h-11 flex items-center justify-center rounded-full hover:bg-surface-container-low transition-colors"
                aria-label="{t["menu_open"]}" aria-expanded="false" aria-controls="mobile-menu"
                data-label-open="{t["menu_open"]}" data-label-close="{t["menu_close"]}">
                <span class="material-symbols-outlined" aria-hidden="true">menu</span>
            </button>
        </div>
        <div id="mobile-menu"
            class="hidden md:hidden flex-col bg-surface border-t border-outline-variant/30 px-margin-mobile py-4 gap-1">
{nl.join(mob)}
            <div class="flex items-center gap-2 pt-3 mt-2 border-t border-outline-variant/20 text-label-md font-label-md"
                role="group" aria-label="{t["lang_label"]}">
                <a class="py-3 {es_m}" href="{es_href}" hreflang="es" lang="es">Español</a>
                <span class="text-on-surface-variant" aria-hidden="true">|</span>
                <a class="py-3 {en_m}" href="{en_href}" hreflang="en" lang="en">English</a>
            </div>
        </div>
    </nav>
'''


def footer(lang, P, scripts, L=""):
    t, d = T[lang], D[lang]
    explore = "\n".join(f'                    <li><a class="{LINK}" href="{L}{k}.html">{l}</a></li>' for k, l in t["explore_links"])
    legal = "\n".join(f'                    <li><a class="{LINK}" href="{L}{h}">{l}</a></li>' for h, l in t["legal_links"])
    sc = "\n".join(f'    <script src="{P}js/{s}.js"></script>' for s in scripts)
    return f'''    <!-- Footer -->
    <footer class="bg-surface-container-low border-t border-outline-variant/20 pt-16 pb-24 md:pb-10 mt-12">
        <div class="grid grid-cols-2 md:grid-cols-12 gap-x-gutter gap-y-10 px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto mb-12">
            <div class="col-span-2 md:col-span-3 space-y-4">
                <p class="font-headline-md text-headline-md text-on-primary-fixed-variant font-bold">Costumbres</p>
                <p class="font-body-md text-body-md text-on-surface-variant max-w-xs">{t["foot_desc"]}</p>
            </div>
            <div class="md:col-span-2">
                <h2 class="font-label-md text-label-md text-on-surface mb-4">{t["explore"]}</h2>
                <ul class="space-y-2">
{explore}
                </ul>
            </div>
            <div class="md:col-span-2">
                <h2 class="font-label-md text-label-md text-on-surface mb-4">{t["social"]}</h2>
                <ul class="space-y-2">
                    <li><a class="{LINK}" href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a></li>
                    <!-- PENDIENTE: agregar Facebook y TikTok cuando tengan URL real -->
                </ul>
            </div>
            <div class="md:col-span-2">
                <h2 class="font-label-md text-label-md text-on-surface mb-4">{t["legal"]}</h2>
                <ul class="space-y-2">
{legal}
                </ul>
            </div>
            <div class="col-span-2 md:col-span-3 flex justify-center items-center md:self-center">
                <img class="w-60 md:w-64 h-auto" src="{P}img/logos/logo-tortuga.png" width="280" height="167" {LAZY}
                    alt="{t["logo_alt"]}" />
            </div>
        </div>
        <div class="px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto pt-8 border-t border-outline-variant/30 text-center space-y-3">
            <p class="font-body-md text-label-md text-on-surface-variant">
                {d["address"]}, {d["city"]} ·
                <a class="underline underline-offset-4 hover:text-on-primary-fixed-variant" href="mailto:{EMAIL}">{EMAIL}</a>
            </p>
            <p class="font-body-md text-label-md text-on-surface-variant max-w-2xl mx-auto">{t["sic"]}</p>
            <p class="font-label-md text-label-md text-on-secondary-container italic">{t["copy"]}</p>
        </div>
        <!-- Botón flotante de WhatsApp (dentro del footer para quedar en una región; es fixed) -->
    <a href="{wa(t["fab_msg"])}" target="_blank" rel="noopener" aria-label="{t["fab_label"]}" title="{t["fab_label"]}"
        class="wa-fab fixed z-40 w-14 h-14 rounded-full bg-whatsapp text-on-surface shadow-lg shadow-whatsapp/30 flex items-center justify-center lift-anim overlay-anim overlay-anim--claro">
        {WA_SVG.replace("w-6 h-6", "w-7 h-7")}
    </a>
    </footer>
{sc}
</body>

</html>
'''


def map_facade(lang, box_cls):
    """Mapa que solo se carga al pulsar (sin cookies de Google antes de que el usuario lo pida)."""
    t = T[lang]
    return f'''<div class="{box_cls}">
                    <div class="map-facade w-full h-full bg-surface-container-low flex flex-col items-center justify-center gap-4 p-6 text-center"
                        data-map-src="{MAP_EMBED}" data-map-title="{t["map_title"]}">
                        {icon("map", "text-on-primary-fixed-variant text-5xl")}
                        <p class="font-body-md text-body-md text-on-surface-variant max-w-xs">{t["map_note"]}</p>
                        <div class="flex flex-wrap gap-3 justify-center">
                            <button type="button" class="map-load bg-primary text-on-primary-fixed px-6 py-3 rounded-full font-label-md text-label-md press-anim overlay-anim overlay-anim--claro">{t["map_load"]}</button>
                            <a href="{MAP_OPEN}" target="_blank" rel="noopener"
                                class="border-2 border-primary text-on-primary-fixed-variant px-6 py-3 rounded-full font-label-md text-label-md inline-flex items-center gap-2 press-anim overlay-anim">{t["map_open"]}
                                {icon("open_in_new", "text-base")}</a>
                        </div>
                    </div>
                </div>'''


def page(lang, P, page_key, alt_href, title, desc, css, body, scripts, L="", here_href=None, extra_head=""):
    h = head(lang, P, title, desc, css)
    if extra_head:
        h = h.replace("</head>", extra_head + "\n</head>")
    return h + nav(lang, P, page_key, alt_href, L, here_href) + body + footer(lang, P, scripts, L)
