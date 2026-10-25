import json
from common import *

S = {
    "es": {
        "title": "Categorías y técnicas artesanales | Costumbres",
        "desc": "Chaquira, tejido en fibra, joyería y arte decorativo. Conoce las técnicas y comunidades detrás de cada pieza: tamo, werregue, sombrero vueltiao, Guacamayas, mola, mochila wayúu y collar emberá.",
        "h1": "Nuestras Tradiciones",
        "lead": "Descubre el alma de Colombia a través de sus técnicas ancestrales. Cada pieza cuenta la historia de un territorio, una familia y un legado que perdura.",
        "see": "Ver piezas disponibles",
        "wa_msg": "¡Hola, Costumbres! Me interesan sus piezas de «{}». ¿Qué tienen disponible?",
        "bento": [
            ("chaquira", "Chaquira", "Hecho a mano",
             "Collares, aretes y pulseras tejidos hilo a hilo en mostacilla, con patrones geométricos de colores que le dan identidad a cada pieza.",
             "Collar artesanal en chaquira tejida a mano con patrones geométricos multicolor"),
            ("fibra", "Tejido en Fibra", None,
             "Individuales, pulseras y cestería tejidos a mano en fibra natural, con acabados artesanales de alta calidad.",
             "Individuales y pulseras tejidas a mano en fibra natural con patrones de colores"),
            ("joyeria", "Joyería con Certificado", None,
             "Anillos y aretes en plata y oro con piedras naturales, respaldados por certificado de garantía.",
             "Aretes en plata con piedra de esmeralda"),
            ("decoracion", "Arte Decorativo", "Para el hogar",
             "Piezas artesanales para pared y objetos decorativos que le dan un toque colombiano a cualquier espacio.",
             "Paneles decorativos artesanales con diseño circular de colores"),
        ],
        "tech_h": "Técnicas y Comunidades Artesanas",
        "tech_p": "Cada pieza que vendemos tiene detrás una técnica, una región y una comunidad. Esta es su historia.",
        "tech": [
            ("Tamo", "Enchapado en tamo de trigo, técnica artesanal de Nariño",
             "El enchapado en tamo de trigo es una técnica artesanal tradicional de Nariño que consiste en decorar piezas de madera con finas fibras del tallo del trigo. Sus delicados diseños representan flores, paisajes y escenas de la cultura campesina, convirtiendo cada creación en una obra única que preserva la autenticidad y el valor cultural de la región."),
            ("Werregue", "Canastos de werregue, artesanía de la comunidad Wounaan",
             "Los canastos de werregue son elaborados a mano por la comunidad indígena Wounaan del Pacífico colombiano utilizando fibras de la palma de werregue. Tejidos mediante la técnica del espiral, cada pieza refleja la conexión entre la naturaleza, el conocimiento ancestral y las tradiciones de esta comunidad."),
            ("Sombrero Vueltiao", "Sombrero Vueltiao, artesanía de Tuchín, Córdoba",
             "El sombrero vueltiao, elaborado con fibras de caña flecha, es uno de los símbolos más representativos de Colombia. Originario de Tuchín, Córdoba, sus característicos diseños geométricos reflejan la cosmovisión del pueblo Zenú y siglos de tradición artesanal transmitida de generación en generación."),
            ("Guacamayas", "Cestería en rollo de Guacamayas, Boyacá",
             "La cestería en rollo de Guacamayas, Boyacá, destaca por sus vivos colores y su cuidadosa elaboración artesanal. Realizada con paja y fibras de fique mediante la técnica del espiral, cada pieza combina creatividad, precisión y saberes tradicionales que representan la identidad cultural colombiana."),
            ("Mola", "Mola, tejido decorativo del pueblo Guna (Kuna)",
             "Las molas son tejidos decorativos elaborados por las mujeres indígenas del pueblo Guna (Kuna), quienes habitan territorios de Colombia y Panamá. Confeccionadas mediante la técnica del aplique sobre varias capas de tela, destacan por sus coloridos diseños inspirados en la naturaleza, la vida cotidiana y la cosmovisión de su comunidad."),
            ("Mochila Wayúu", "Mochila Wayúu, artesanía de La Guajira",
             "La mochila Wayúu, conocida como Susu (“lo que camina con uno”), es una de las artesanías más representativas de La Guajira. Tejida a mano con fibras de algodón o maguey mediante la técnica del crochet, cada mochila presenta diseños y colores únicos que reflejan la identidad, las tradiciones y la creatividad del pueblo Wayúu."),
            ("Manillas y Pulseras", "Manillas y pulseras artesanales tejidas a mano con fibras naturales",
             "Lleva contigo el legado y la maestría del tejido ancestral. Esta colección reúne manillas y pulseras elaboradas a mano con fibras naturales seleccionadas, destacando por sus sutiles texturas, variados grosores y patrones geométricos que reflejan la identidad cultural y el arte de nuestras comunidades."),
            ("Collar Emberá", "Collar Emberá, artesanía de la comunidad Emberá Chamí",
             "El collar Emberá, elaborado a mano por la comunidad Emberá Chamí de Risaralda, representa la riqueza cultural de Colombia. Sus coloridos diseños tejidos con chaquiras expresan la identidad, las tradiciones y el legado ancestral de sus artesanos, convirtiendo cada pieza en una manifestación única de su patrimonio."),
        ],
        "cta_h": "¿Buscas algo en especial?",
        "cta_p": "Escríbenos y te ayudamos a encontrar la pieza perfecta.",
        "cta_btn": "Contáctanos",
    },
    "en": {
        "title": "Categories & Artisan Techniques | Costumbres",
        "desc": "Beadwork, fiber weaving, jewelry and decorative art. Discover the techniques and communities behind every piece: tamo, werregue, sombrero vueltiao, Guacamayas, mola, Wayúu bags and Emberá necklaces.",
        "h1": "Our Traditions",
        "lead": "Discover the soul of Colombia through its ancestral techniques. Every piece tells the story of a territory, a family, and a legacy that endures.",
        "see": "See available pieces",
        "wa_msg": "Hi Costumbres! I'm interested in your \u201c{}\u201d pieces. What do you have available?",
        "bento": [
            ("chaquira", "Beadwork", "Handmade",
             "Necklaces, earrings and bracelets woven thread by thread in glass beads, with colorful geometric patterns that give each piece its own identity.",
             "Handwoven beaded necklace with multicolor geometric patterns"),
            ("fibra", "Fiber Weaving", None,
             "Placemats, bracelets and baskets handwoven in natural fiber, with high-quality artisanal finishes.",
             "Handwoven placemats and bracelets in natural fiber with colorful patterns"),
            ("joyeria", "Jewelry with Certificate", None,
             "Rings and earrings in silver and gold with natural stones, backed by a warranty certificate.",
             "Silver earrings with emerald stone"),
            ("decoracion", "Decorative Art", "For the home",
             "Wall pieces and decorative objects that bring a Colombian touch to any space.",
             "Decorative handcrafted panels with colorful circular design"),
        ],
        "tech_h": "Techniques & Artisan Communities",
        "tech_p": "Every piece we sell carries a technique, a region, and a community behind it. This is their story.",
        "tech": [
            ("Wheat Straw Veneer (Tamo)", "Wheat straw veneer, traditional handicraft from Nariño",
             "Wheat Straw Veneer is a traditional handicraft from Nariño that uses thin wheat straw fibers to decorate wooden pieces with intricate floral, landscape, and rural-inspired designs. Each handcrafted creation is unique and preserves the authenticity and cultural heritage of the region."),
            ("Werregue", "Werregue basket woven by the Wounaan community",
             "Werregue Baskets are handwoven by the Wounaan Indigenous community of Colombia's Pacific region using fibers from the werregue palm. Crafted with the traditional spiral weaving technique, each basket reflects a deep connection to nature, ancestral knowledge, and cultural traditions."),
            ("Sombrero Vueltiao", "Sombrero Vueltiao woven in caña flecha, Zenú people",
             "The Sombrero Vueltiao is one of Colombia's most iconic cultural symbols. Handwoven from caña flecha fibers by the Zenú people, its distinctive geometric patterns reflect Indigenous heritage and centuries of artisanal tradition passed down through generations."),
            ("Guacamayas", "Guacamayas coiled basketry, Boyacá",
             "Guacamayas Basketry is a traditional craft from Boyacá known for its vibrant colors and meticulous craftsmanship. Made from straw and fique fibers using a spiral coiling technique, each piece combines creativity, precision, and traditions passed down through generations."),
            ("Mola", "Mola, decorative textile made by the Guna (Kuna) people",
             "Molas are decorative handmade textiles created by the Indigenous Guna (Kuna) women of Colombia and Panama. Made using the reverse appliqué technique with multiple layers of fabric, their colorful designs are inspired by nature, everyday life, and the community's worldview."),
            ("Wayúu Bag", "Handwoven Wayúu bag, La Guajira",
             "The Wayúu Bag, known as Susu (“what walks with you”), is one of the most representative handicrafts of La Guajira. Handwoven using cotton or maguey fibers with the crochet technique, each bag features unique patterns and vibrant colors that reflect the Wayúu people's identity, traditions, and creativity."),
            ("Bracelets & Wristbands", "Handwoven bracelets made with natural fibers",
             "Carry the legacy and mastery of ancestral weaving with you. This collection brings together handmade bracelets and wristbands crafted from carefully selected natural fibers, standing out for their subtle textures, varied thicknesses, and geometric patterns that reflect the cultural identity and artistry of our communities."),
            ("Emberá Necklace", "Beaded necklace by the Emberá Chamí community",
             "The Emberá Beaded Necklace is handcrafted by the Emberá Chamí community of Risaralda. Woven with colorful beads, each necklace reflects the artisans' identity, traditions, and ancestral heritage, making every piece a unique expression of Colombian culture."),
        ],
        "cta_h": "Looking for something specific?",
        "cta_p": "Write to us and we'll help you find the perfect piece.",
        "cta_btn": "Contact Us",
    },
}

BENTO_IMG = ["artesanias/f01.jpg", "artesanias/f20.jpg", "joyas/f04.jpg", "artesanias/f60.jpg"]
CAROUSELS = [
    ["f50", "f51", "f52", "f53", "f54", "f55", "f56", "f59"],
    ["f95", "f96", "f97", "f99", "f107", "f108", "f109", "f112"],
    ["f70", "f69", "f71", "f74", "f77", "f76"],
    ["f30", "f10", "f18", "f22", "f31", "f33", "f26"],
    ["f128", "f129", "f130", "f127", "f131", "f126", "f132"],
    ["f93", "f91", "f92", "f136"],
    ["f38", "f39", "f41", "f44", "f45", "f04"],
    ["f02", "f01", "f03"],
]

CARD = "group relative overflow-hidden rounded-xl border border-primary/5 bg-surface-container-low lift-anim zoom-anim ring-anim"
IMG = "w-full h-full object-cover"


def bento(lang, P, i):
    s = S[lang]
    bid, name, eyebrow, text, alt = s["bento"][i]
    href = wa(s["wa_msg"].format(name))
    eb = f'\n                        <span class="font-label-md text-label-md text-on-tertiary-fixed-variant mb-2">{eyebrow}</span>' if eyebrow else ""
    see = f'<span class="mt-auto pt-2 inline-flex items-center gap-2 font-label-md text-label-md text-on-primary-fixed-variant group-hover:underline underline-offset-4">{WA_ICON_SM}{s["see"]}</span>'
    img = f'<img class="{IMG}" alt="{alt}" src="{P}img/{BENTO_IMG[i]}" {LAZY} />'
    if i in (0, 3):  # tarjetas anchas con imagen a un lado
        direction = "md:flex-row" if i == 0 else "md:flex-row-reverse"
        return f'''            <!-- Categoría: {name} -->
            <a id="{bid}" href="{href}" target="_blank" rel="noopener"
                class="lg:col-span-8 scroll-mt-28 {CARD}">
                <div class="flex flex-col {direction} h-full">
                    <div class="md:w-1/2 h-64 md:h-auto overflow-hidden">
                        {img}
                    </div>
                    <div class="md:w-1/2 p-8 flex flex-col justify-center">{eb}
                        <h2 class="font-headline-lg text-headline-md text-on-surface mb-4">{name}</h2>
                        <p class="font-body-md text-body-md text-on-surface-variant mb-6">{text}</p>
                        {see.replace("mt-auto pt-2 ", "")}
                    </div>
                </div>
            </a>'''
    return f'''            <!-- Categoría: {name} -->
            <a id="{bid}" href="{href}" target="_blank" rel="noopener"
                class="lg:col-span-4 scroll-mt-28 flex flex-col {CARD}">
                <div class="h-64 overflow-hidden">
                    {img}
                </div>
                <div class="p-8 flex-grow flex flex-col">
                    <h2 class="font-headline-md text-headline-md text-on-surface mb-2">{name}</h2>
                    <p class="font-body-md text-body-md text-on-surface-variant mb-4">{text}</p>
                    {see}
                </div>
            </a>'''


def tech(lang, P, i):
    name, alt, text = S[lang]["tech"][i]
    srcs = [f"{P}img/artesanias/{f}.jpg" for f in CAROUSELS[i]]
    data = json.dumps(srcs, separators=(",", ":"))
    return f'''                <!-- {i + 1}. {name} -->
                <article class="rounded-xl overflow-hidden border border-primary/5 bg-surface-container-low">
                    <div class="relative aspect-square overflow-hidden" data-carousel='{data}'>
                        <img class="carousel-img absolute inset-0 w-full h-full object-cover opacity-100"
                            alt="{alt}" src="{srcs[0]}" {LAZY} />
                        <img class="carousel-img absolute inset-0 w-full h-full object-cover opacity-0"
                            alt="{alt}" src="{srcs[0]}" aria-hidden="true" {LAZY} />
                    </div>
                    <div class="p-8">
                        <h3 class="font-headline-md text-headline-md text-on-surface mb-3">{name}</h3>
                        <p class="font-body-md text-body-md text-on-surface-variant">{text}</p>
                    </div>
                </article>'''


def body(lang, P):
    s = S[lang]
    bentos = "\n".join(bento(lang, P, i) for i in range(4))
    techs = "\n".join(tech(lang, P, i) for i in range(8))
    return f'''    <main id="contenido" class="pt-32 pb-12 max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop relative">
        <!-- Page Header -->
        <section class="mb-12" data-reveal>
            <h1 class="font-display-lg text-display-lg-mobile md:text-display-lg text-primary mb-4 leading-tight">
                {s["h1"]}</h1>
            <p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl">
                {s["lead"]}
            </p>
            <div class="weaving-divider mt-8 w-1/3" aria-hidden="true"></div>
        </section>
        <!-- Categories Bento Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-gutter" data-anim="stagger">
{bentos}
        </div>
        <!-- Técnicas y Comunidades Artesanas -->
        <section class="mt-24 mb-8">
            <div class="text-center mb-12" data-reveal>
                <h2 class="font-headline-lg text-headline-lg text-primary mb-4">{s["tech_h"]}</h2>
                <p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl mx-auto">
                    {s["tech_p"]}
                </p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-gutter max-w-4xl mx-auto" data-anim="stagger">
{techs}
            </div>
        </section>
        <!-- Call to action -->
        <section
            class="mt-24 bg-primary-container rounded-xl p-12 text-center text-on-primary-container overflow-hidden relative" data-reveal>
            <div class="relative z-10">
                <h2 class="font-headline-lg text-headline-md md:text-headline-lg mb-4">{s["cta_h"]}</h2>
                <p class="font-body-lg text-body-lg mb-8">{s["cta_p"]}</p>
                <a href="contacto.html"
                    class="bg-surface text-on-primary-fixed-variant px-8 py-3 rounded-full font-bold flex items-center gap-2 mx-auto w-fit press-anim overlay-anim">
                    {icon("chat")}
                    {s["cta_btn"]}
                </a>
            </div>
            <!-- Organic decorative element -->
            <div class="absolute top-0 right-0 -mr-20 -mt-20 w-64 h-64 bg-tertiary opacity-10 rounded-full blur-3xl" aria-hidden="true">
            </div>
        </section>
    </main>
'''


def build(lang):
    P = "" if lang == "es" else "../"
    alt = "en/categorias.html" if lang == "es" else "../categorias.html"
    s = S[lang]
    return page(lang, P, "categorias", alt, s["title"], s["desc"], ["categorias", "visor"], body(lang, P), ["nav", "carrusel", "visor"])
