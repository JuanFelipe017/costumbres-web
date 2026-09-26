from common import *

S = {
    "es": {
        "title": "Nuestra historia | Costumbres",
        "desc": "Piezas hechas a mano con técnicas tradicionales colombianas. Conoce cómo trabajamos y visita nuestro local en el centro histórico de Bogotá.",
        "hero_alt": "Ilustración conceptual de artesanías colombianas, tramas y fibras ancestrales",
        "h1": "Tejiendo el alma de Colombia",
        "lead": "Más que objetos, creamos puentes entre el pasado ancestral y el diseño contemporáneo. Cada pieza cuenta una historia de resistencia, manos sabias y la tierra que nos sostiene.",
        "rhythm_h": "El Ritmo de la Tierra",
        "rhythm_p": "Cada pieza se teje o se forja a mano, hilo a hilo, gota de plata a gota de plata. No trabajamos en serie: el tiempo de creación lo marca el detalle, no el afán.",
        "quote_short": "“El arte que no se apura, perdura.”",
        "fiber_h": "Fibras Naturales",
        "fiber_p": "Caña flecha, werregue, fique, algodón y paja: materiales naturales trabajados con técnicas que han pasado de generación en generación.",
        "stats": [("8", "Técnicas artesanales"), ("100%", "Hecho a mano")],
        "img_main_alt": "Máscaras decorativas artesanales pintadas a mano",
        "img_small_alt": "Juegos de mesa artesanales",
        "make_h": "Lo que Tejemos y Forjamos",
        "make_p": "Cuatro familias de productos, todas hechas a mano, todas con el mismo cuidado.",
        "make": [("chaquira", "Chaquira", "Collares y aretes"), ("fibra", "Tejido en Fibra", "Pulseras y cestería"),
                 ("joyeria", "Joyería", "Plata y oro"), ("decoracion", "Arte Decorativo", "Para el hogar")],
        "store_h": "Conoce Nuestro Local",
        "store_p": "En el corazón del centro histórico de Bogotá, cada vitrina cuenta una historia distinta.",
        "store_alts": ["Vitrina de joyería y artesanías en el local de Costumbres",
                       "Mochilas, sombreros y artesanías exhibidas en la entrada del local",
                       "Fachada colonial de la Casona del Museo en el centro histórico de Bogotá"],
        "quote": "“Cuando tejemos, no solo cruzamos hilos. Estamos cruzando pensamientos, oraciones y la memoria de nuestros abuelos para que no se pierdan en el tiempo.”",
        "cite": "— Equipo Costumbres",
    },
    "en": {
        "title": "Our Story | Costumbres",
        "desc": "Handmade pieces crafted with traditional Colombian techniques. Learn how we work and visit our store in Bogotá's historic center.",
        "hero_alt": "Illustration of Colombian handcrafts, ancestral weaves and fibers",
        "h1": "Weaving the soul of Colombia",
        "lead": "More than objects, we build bridges between ancestral heritage and contemporary design. Every piece tells a story of resilience, wise hands, and the land that sustains us.",
        "rhythm_h": "The Rhythm of the Land",
        "rhythm_p": "Every piece is woven or forged by hand, thread by thread, drop of silver by drop of silver. We don't work at scale: the pace of creation is set by the detail, not by haste.",
        "quote_short": "“Art that isn't rushed, endures.”",
        "fiber_h": "Natural Fibers",
        "fiber_p": "Caña flecha, werregue palm, fique, cotton and straw: natural materials worked with techniques passed down through generations.",
        "stats": [("8", "Artisan techniques"), ("100%", "Handmade")],
        "img_main_alt": "Hand-painted decorative handcrafted masks",
        "img_small_alt": "Handcrafted board games",
        "make_h": "What We Weave and Forge",
        "make_p": "Four families of products, all handmade, all with the same care.",
        "make": [("chaquira", "Beadwork", "Necklaces & earrings"), ("fibra", "Fiber Weaving", "Bracelets & basketry"),
                 ("joyeria", "Jewelry", "Silver & gold"), ("decoracion", "Decorative Art", "For the home")],
        "store_h": "Visit Our Store",
        "store_p": "In the heart of Bogotá's historic center, every display case tells a different story.",
        "store_alts": ["Jewelry and handcraft display case at the Costumbres store",
                       "Bags, hats and handcrafts displayed at the store entrance",
                       "Colonial facade of the Casona del Museo in Bogotá's historic center"],
        "quote": "“When we weave, we don't just cross threads. We cross thoughts, prayers, and the memory of our grandparents, so they are never lost to time.”",
        "cite": "— The Costumbres Team",
    },
}


def body(lang, P):
    s = S[lang]
    stats = "\n".join(f'''                        <div>
                            <p class="font-display-lg text-headline-lg text-primary">{n}</p>
                            <p class="text-on-surface-variant font-body-md">{l}</p>
                        </div>''' for n, l in s["stats"])
    make = "\n".join(f'''                        <a href="categorias.html#{a}"
                            class="flex flex-col items-center justify-center text-center space-y-2 p-6 bg-white/60 backdrop-blur-md rounded-xl border border-white/60 hover:bg-white/90 transition-colors group lift-anim">
                            <span class="font-headline-md text-headline-md text-primary">{n}</span>
                            <span class="text-label-md font-label-md text-on-surface-variant group-hover:text-on-primary-fixed-variant group-hover:underline underline-offset-4 transition-colors">{sub}</span>
                        </a>''' for a, n, sub in s["make"])
    store = "\n".join(f'''                <div class="rounded-2xl overflow-hidden aspect-[4/5] zoom-anim" data-visor="local">
                    <img class="w-full h-full object-cover"
                        alt="{alt}" src="{P}img/local/{f}.jpg" {LAZY} />
                </div>''' for alt, f in zip(s["store_alts"], ["f02", "f04", "f03"]))
    return f'''    <main id="contenido" class="pt-20">
        <!-- Hero Section -->
        <section class="relative h-[65vh] min-h-[500px] flex items-center px-margin-mobile md:px-margin-desktop py-12 overflow-hidden">
            <div class="absolute inset-0 z-0">
                <img src="{P}img/hero/hero-historia.jpg" fetchpriority="high"
                    alt="{s["hero_alt"]}"
                    class="w-full h-full object-cover object-center contrast-110 saturate-110 brightness-105" />
                <div class="absolute inset-0 bg-[radial-gradient(circle,_rgba(255,255,255,0.7)_0%,_transparent_70%)]"></div>
            </div>
            <div class="relative z-10 max-w-3xl mx-auto text-center" data-anim="hero">
                <h1 class="font-display-lg text-display-lg-mobile md:text-display-lg text-on-surface leading-tight mb-6 drop-shadow-sm">
                    {s["h1"]}
                </h1>
                <p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl mx-auto text-balance">
                    {s["lead"]}
                </p>
            </div>
        </section>
        <!-- The Process: Asymmetric Grid -->
        <section class="py-24 px-margin-mobile md:px-margin-desktop" data-reveal>
            <div class="grid grid-cols-1 md:grid-cols-12 gap-gutter items-center">
                <div class="md:col-span-5 space-y-8 order-2 md:order-1">
                    <div class="space-y-4">
                        <h2 class="font-headline-lg text-headline-lg text-primary">{s["rhythm_h"]}</h2>
                        <p class="font-body-lg text-body-lg text-on-surface-variant">
                            {s["rhythm_p"]}
                        </p>
                    </div>
                    <div class="flex items-center gap-4 py-2">
                        <div class="w-12 h-0.5 bg-primary shrink-0" aria-hidden="true"></div>
                        <p class="font-headline-md text-headline-md text-on-surface-variant italic">
                            {s["quote_short"]}
                        </p>
                    </div>
                    <div class="p-8 bg-surface-container-low rounded-xl border border-primary/10 relative overflow-hidden">
                        <div class="relative z-10">
                            {icon("eco", "text-primary mb-4 text-4xl")}
                            <h3 class="font-headline-md text-headline-md mb-2">{s["fiber_h"]}</h3>
                            <p class="text-on-surface-variant">{s["fiber_p"]}</p>
                        </div>
                        <div class="absolute top-0 right-0 p-4 opacity-5" aria-hidden="true">
                            <span class="material-symbols-outlined text-9xl">energy_savings_leaf</span>
                        </div>
                    </div>
                    <div class="grid grid-cols-2 gap-6 pt-2">
{stats}
                    </div>
                </div>
                <div class="md:col-span-7 order-1 md:order-2 relative">
                    <div class="aspect-[4/5] md:aspect-square rounded-2xl overflow-hidden shadow-sm" data-visor>
                        <img class="w-full h-full object-cover" alt="{s["img_main_alt"]}"
                            src="{P}img/artesanias/f137.jpg" {LAZY} />
                    </div>
                    <div class="absolute -bottom-10 -left-10 w-48 h-48 hidden md:block">
                        <img class="w-full h-full object-cover rounded-full border-8 border-background shadow-lg"
                            alt="{s["img_small_alt"]}" src="{P}img/artesanias/f117.jpg" {LAZY} />
                    </div>
                </div>
            </div>
        </section>
        <!-- Lo que tejemos: enlaces a cada categoría -->
        <section class="py-20 bg-surface-container-high/30">
            <div class="px-margin-mobile md:px-margin-desktop text-center mb-16" data-reveal>
                <h2 class="font-headline-lg text-headline-lg text-primary mb-4">{s["make_h"]}</h2>
                <p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl mx-auto">{s["make_p"]}</p>
            </div>
            <div class="max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop">
                <div class="relative rounded-3xl overflow-hidden bg-surface-container flex items-center justify-center p-4 md:p-8">
                    <div class="relative z-10 w-full grid grid-cols-2 md:grid-cols-4 gap-4" data-anim="stagger">
{make}
                    </div>
                </div>
            </div>
        </section>
        <!-- Nuestro Local: fotos reales del showroom -->
        <section class="py-20 px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto">
            <div class="text-center mb-12" data-reveal>
                <h2 class="font-headline-lg text-headline-lg text-primary mb-4">{s["store_h"]}</h2>
                <p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl mx-auto">{s["store_p"]}</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-gutter" data-anim="stagger">
{store}
            </div>
        </section>
        <!-- Quote Section -->
        <section class="py-24 px-margin-mobile md:px-margin-desktop text-center" data-reveal>
            <figure class="max-w-3xl mx-auto">
                <span class="material-symbols-outlined text-primary text-6xl opacity-20 mb-8" aria-hidden="true"
                    style="font-variation-settings: 'FILL' 1;">format_quote</span>
                <blockquote class="font-headline-lg text-headline-lg italic text-on-surface leading-tight mb-8">
                    {s["quote"]}
                </blockquote>
                <figcaption class="font-label-md text-label-md text-on-primary-fixed-variant">{s["cite"]}</figcaption>
            </figure>
        </section>
    </main>
'''


def build(lang):
    P = "" if lang == "es" else "../"
    alt = "en/historia.html" if lang == "es" else "../historia.html"
    s = S[lang]
    return page(lang, P, "historia", alt, s["title"], s["desc"], ["historia", "visor"], body(lang, P), ["nav", "visor"])
