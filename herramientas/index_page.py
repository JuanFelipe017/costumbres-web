from common import *

S = {
    "es": {
        "title": "Costumbres | Joyería y artesanía colombiana en Bogotá",
        "desc": "Joyería con certificado de garantía y artesanías colombianas hechas a mano: chaquira, werregue, sombrero vueltiao, mochila wayúu y más. Visítanos en el centro histórico de Bogotá o escríbenos por WhatsApp.",
        "hero_alt": "Collar artesanal en chaquira, hecho a mano, con patrones geométricos de colores",
        "eyebrow": "Legado ancestral",
        "h1": "El Corazón de Colombia en tus Manos",
        "lead": "Piezas únicas tejidas con la sabiduría de generaciones, trayendo el alma de nuestros pueblos a tu hogar contemporáneo.",
        "cta1": "Explorar Catálogo", "cta2": "Nuestra Historia",
        "cat_h": "Catálogo de Tesoros",
        "cat_p": "Una selección curada de piezas maestras, desde las orillas del río Sinú hasta las montañas de la Sierra Nevada.",
        "cat_all": "Ver todas las colecciones",
        "ask": "Consultar precio por WhatsApp",
        "wa_msg": "Hola, Costumbres. Quiero consultar el precio de: ",
        "items": [
            ("Réplicas Precolombinas", "Orfebrería", "Réplicas en orfebrería, hechas a mano",
             "Réplicas artesanales de figuras antropomorfas de orfebrería precolombina", "Réplica artesanal"),
            ("Joyería con Certificado", "Joyería", "Aretes en plata con esmeralda",
             "Aretes en plata con esmeralda y anillo en su estuche", None),
            ("Individuales Tejidos", "Fibra", "Tejido en fibra natural",
             "Individuales tejidos a mano en fibra con patrones circulares de colores", None),
            ("Set de Pulseras", "Fibra", "Tejido en fibra y metal",
             "Pulseras artesanales tejidas en fibra con hilos dorados", None),
            ("Arte Decorativo", "Decoración", "Paneles artesanales para pared",
             "Arte decorativo artesanal con círculos de colores en relieve", None),
        ],
        "visit_eyebrow": "Nuestra casa",
        "visit_h": "Visítanos en el Centro Histórico",
        "visit_p": "Ven a sentir las texturas y conocer las historias detrás de cada pieza en nuestro espacio showroom en Bogotá.",
        "chat": "Chatea con nosotros",
        "chat_msg": "Hola, Costumbres. Quiero más información sobre sus piezas.",
    },
    "en": {
        "title": "Costumbres | Colombian Jewelry & Handcrafts in Bogotá",
        "desc": "Jewelry with a warranty certificate and handmade Colombian crafts: beadwork, werregue baskets, sombrero vueltiao, Wayúu bags and more. Visit us in Bogotá's historic center or message us on WhatsApp.",
        "hero_alt": "Handmade beaded necklace with colorful geometric patterns",
        "eyebrow": "Ancestral legacy",
        "h1": "The Heart of Colombia in Your Hands",
        "lead": "One-of-a-kind pieces woven with generations of wisdom, bringing the soul of our people into your modern home.",
        "cta1": "Explore Catalog", "cta2": "Our Story",
        "cat_h": "Catalog of Treasures",
        "cat_p": "A curated selection of master pieces, handmade with care from silver, fiber, and beadwork.",
        "cat_all": "View all collections",
        "ask": "Ask for the price on WhatsApp",
        "wa_msg": "Hi Costumbres, I'd like to ask about the price of: ",
        "items": [
            ("Pre-Columbian Replicas", "Metalwork", "Handmade metalwork replicas",
             "Handcrafted replicas of pre-Columbian anthropomorphic goldwork figures", "Handcrafted replica"),
            ("Jewelry with Certificate", "Jewelry", "Silver earrings with emerald",
             "Silver earrings with emerald and a ring in its box", None),
            ("Woven Placemats", "Fiber", "Natural fiber weaving",
             "Handwoven fiber placemats with colorful circular patterns", None),
            ("Bracelet Set", "Fiber", "Fiber and metal weaving",
             "Handcrafted bracelets woven in fiber with golden thread", None),
            ("Decorative Art", "Decor", "Handcrafted wall panels",
             "Decorative handcrafted art with raised colorful circles", None),
        ],
        "visit_eyebrow": "Our home",
        "visit_h": "Visit Us in the Historic Center",
        "visit_p": "Come feel the textures and discover the stories behind every piece in our showroom in Bogotá.",
        "chat": "Chat with us",
        "chat_msg": "Hi Costumbres, I'd like more information about your pieces.",
    },
}

IMGS = ["artesanias/f11.jpg", "joyas/f03.jpg", "artesanias/f20.jpg", "artesanias/f46.jpg", "artesanias/f60.jpg"]
# (layout del contenedor, clase del marco de la imagen, color de la etiqueta, color del punto)
LAYOUT = [
    ("md:col-span-8", "aspect-[16/9]", "text-on-primary-fixed-variant", "bg-primary"),
    ("md:col-span-4 flex flex-col", "flex-grow aspect-[4/5]", "text-tertiary", "bg-tertiary-fixed-dim"),
    ("md:col-span-4", "aspect-square", "text-secondary", "bg-secondary"),
    ("md:col-span-4", "aspect-square", "text-tertiary", "bg-tertiary-fixed-dim"),
    ("md:col-span-4", "aspect-square", "text-secondary", "bg-secondary"),
]


def card(lang, P, i):
    s = S[lang]
    name, cat, sub, alt, badge = s["items"][i]
    wrap, frame, cat_color, dot = LAYOUT[i]
    badge_html = ""
    if badge:
        badge_html = f'''
                        <div class="absolute top-6 left-6">
                            <span class="bg-tertiary-fixed text-on-tertiary-fixed px-3 py-1 rounded-full font-label-md text-label-md">{badge}</span>
                        </div>'''
    return f'''                <a href="{wa(s["wa_msg"] + name)}" target="_blank" rel="noopener"
                    class="{wrap} group block rounded-3xl lift-anim zoom-anim">
                    <div class="relative {frame} overflow-hidden rounded-3xl earth-shadow mb-6">
                        <img class="w-full h-full object-cover"
                            alt="{alt}" src="{P}img/{IMGS[i]}" {LAZY} />{badge_html}
                    </div>
                    <div>
                        <span class="inline-flex items-center gap-2 font-label-md text-label-md {cat_color} mb-2">
                            <span class="w-2 h-2 rounded-full {dot}" aria-hidden="true"></span>{cat}
                        </span>
                        <h3 class="font-headline-md text-headline-md text-on-surface mb-1">{name}</h3>
                        <p class="text-on-surface-variant font-body-md">{sub}</p>
                        <span class="mt-3 inline-flex items-center gap-2 font-label-md text-label-md text-on-primary-fixed-variant group-hover:underline underline-offset-4">{s["ask"]}</span>
                    </div>
                </a>'''


def body(lang, P):
    s, t, d = S[lang], T[lang], D[lang]
    cards = "\n".join(card(lang, P, i) for i in range(5))
    return f'''    <main id="contenido" class="pt-20">
        <!-- Hero Section -->
        <section class="relative h-[85vh] flex items-center justify-center overflow-hidden">
            <div class="absolute inset-0 z-0">
                <img alt="{s["hero_alt"]}" fetchpriority="high"
                    class="w-full h-full object-cover contrast-105 saturate-105 brightness-100" src="{P}img/hero/hero-inicio.jpg" />
                <!-- Sombra radial clara en el centro para aislar el texto -->
                <div class="absolute inset-0 bg-[radial-gradient(circle,_rgba(255,255,255,0.6)_0%,_transparent_70%)]"></div>
            </div>

            <div class="relative z-10 text-center px-margin-mobile md:px-margin-desktop max-w-4xl mx-auto" data-anim="hero">
                <span class="font-label-md text-label-md text-on-primary-fixed-variant bg-surface-container-low/80 backdrop-blur px-4 py-1 rounded-full mb-6 inline-block border border-outline-variant/30">
                    {s["eyebrow"]}
                </span>

                <!-- Tipografía oscura para máxima legibilidad -->
                <h1 class="font-display-lg text-display-lg-mobile md:text-display-lg text-on-surface mb-8 leading-tight drop-shadow-sm">
                    {s["h1"]}
                </h1>
                <p class="font-body-lg text-body-lg text-on-surface-variant mb-10 max-w-2xl mx-auto text-balance">
                    {s["lead"]}
                </p>

                <div class="flex flex-col md:flex-row gap-4 justify-center">
                    <a class="{BTN_PRIMARY}" href="categorias.html">{s["cta1"]}</a>
                    <a class="{BTN_OUTLINE}" href="historia.html">{s["cta2"]}</a>
                </div>
            </div>
        </section>
        <!-- Product Grid: Catálogo de Tesoros -->
        <section
            class="py-24 px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto woven-pattern rounded-[40px] my-12">
            <div class="flex flex-col md:flex-row justify-between md:items-end mb-16 gap-6" data-reveal>
                <div class="max-w-xl">
                    <h2 class="font-headline-lg text-headline-lg text-on-surface mb-4">{s["cat_h"]}</h2>
                    <p class="font-body-md text-body-md text-on-surface-variant">{s["cat_p"]}</p>
                </div>
                <a href="categorias.html" class="text-on-primary-fixed-variant font-label-md text-label-md flex items-center gap-2 group py-2 hover:underline underline-offset-4">
                    {s["cat_all"]}
                    {icon("arrow_forward", "motion-safe:group-hover:translate-x-1 transition-transform duration-300")}
                </a>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-12 gap-gutter" data-anim="stagger">
{cards}
            </div>
        </section>
        <!-- Visit Us Section -->
        <section class="py-24 px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-16 items-center" data-anim="stagger">
                <div class="space-y-10">
                    <div>
                        <span class="font-label-md text-label-md text-on-primary-fixed-variant mb-4 block">{s["visit_eyebrow"]}</span>
                        <h2 class="font-display-lg text-display-lg-mobile md:text-headline-lg text-on-surface">{s["visit_h"]}</h2>
                        <p class="font-body-lg text-body-lg text-on-surface-variant mt-6">{s["visit_p"]}</p>
                    </div>
                    <div class="space-y-6">
                        <div class="flex items-start gap-4">
                            {icon("location_on", "text-primary text-3xl")}
                            <div>
                                <p class="font-headline-md text-on-surface">{d["address"]}</p>
                                <p class="text-on-surface-variant">{d["city"]}</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-4">
                            {icon("schedule", "text-primary text-3xl")}
                            <div>
                                <p class="font-headline-md text-on-surface">{d["days"]}</p>
                                <p class="text-on-surface-variant">{d["hours"]}</p>
                            </div>
                        </div>
                    </div>
                    <div class="pt-6 space-y-4">
                        <a class="{BTN_WA}" href="{wa(s["chat_msg"])}" target="_blank" rel="noopener">
                            {WA_SVG}
                            {s["chat"]}
                        </a>
                        <p class="font-body-md text-label-md text-on-surface-variant max-w-md">{t["consent"]}</p>
                    </div>
                </div>
                {map_facade(lang, "relative rounded-3xl overflow-hidden earth-shadow h-80 md:h-[500px]")}
            </div>
        </section>
    </main>
'''


def build(lang):
    P = "" if lang == "es" else "../"
    alt = "en/index.html" if lang == "es" else "../index.html"
    s = S[lang]
    return page(lang, P, "index", alt, s["title"], s["desc"], ["index"], body(lang, P), ["nav", "mapa"])
