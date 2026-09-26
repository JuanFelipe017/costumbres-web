from common import *

A = 'class="underline underline-offset-4 text-on-primary-fixed-variant"'
UL = '<ul class="list-disc pl-6 space-y-2">'
OL = '<ol class="list-decimal pl-6 space-y-2">'


def ident(lang):
    d = D[lang]
    lab = {"es": ("Razón social", "Dirección", "Correo", "WhatsApp"),
           "en": ("Legal name", "Address", "Email", "WhatsApp")}[lang]
    return f'''{UL}
                        <li><strong>{lab[0]}:</strong> {d["legal_name"]} — {d["nit"]}</li>
                        <li><strong>{lab[1]}:</strong> {d["address"]}, {d["city"]}</li>
                        <li><strong>{lab[2]}:</strong> <a {A} href="mailto:{EMAIL}">{EMAIL}</a></li>
                        <li><strong>{lab[3]}:</strong> <a {A} href="https://wa.me/{WA_NUMBER}" target="_blank" rel="noopener">+{WA_NUMBER}</a></li>
                    </ul>'''


PRIV = {
    "es": {
        "title": "Política de privacidad y cookies | Costumbres",
        "desc": "Cómo trata Costumbres los datos personales que recibe por WhatsApp, correo y en su tienda, tus derechos como titular y el uso de cookies en este sitio.",
        "h1": "Política de privacidad y cookies",
        "updated": "Última actualización: 26 de septiembre de 2026",
        "toc": "En esta página",
        "intro": "En Costumbres respetamos tu privacidad. Esta política explica qué datos personales recibimos, para qué los usamos y cómo puedes ejercer tus derechos, conforme a la Ley 1581 de 2012 y al Decreto 1074 de 2015 (que compila el Decreto 1377 de 2013).",
        "sections": [
            ("responsable", "Responsable del tratamiento", lambda: ident("es")),
            ("datos", "Qué datos recibimos", lambda: f'''<p>Este sitio web es informativo: no tiene formularios, registro de usuarios ni pagos en línea. Solo recibimos datos personales cuando tú decides escribirnos por WhatsApp o correo, o cuando compras en nuestra tienda:</p>
                    {UL}
                        <li>Nombre.</li>
                        <li>Número de teléfono y/o correo electrónico.</li>
                        <li>El contenido de tus mensajes, incluidas las fotos que nos envíes.</li>
                        <li>Si compras: dirección de entrega y los datos que exija la facturación electrónica.</li>
                    </ul>
                    <p>No solicitamos datos sensibles ni datos de niños, niñas o adolescentes.</p>'''),
            ("finalidades", "Para qué usamos tus datos", lambda: f'''{UL}
                        <li>Responder tus consultas y cotizaciones.</li>
                        <li>Confirmar disponibilidad, precios y reservas de piezas.</li>
                        <li>Gestionar ventas, entregas, cambios, retractos y garantías.</li>
                        <li>Emitir facturas y cumplir obligaciones legales, contables y tributarias.</li>
                        <li>Atender peticiones, quejas y reclamos.</li>
                        <li>Enviarte novedades o promociones, <strong>solo si nos lo autorizas expresamente</strong>. Puedes pedir que dejemos de enviarlas en cualquier momento.</li>
                    </ul>'''),
            ("autorizacion", "Tu autorización", lambda: '<p>Cuando nos escribes por iniciativa propia (por WhatsApp, correo o en la tienda), nos autorizas a tratar tus datos para las finalidades anteriores; por eso mostramos este aviso junto a nuestros canales de contacto y en el pie de todas las páginas. Puedes revocar esta autorización o pedir que eliminemos tus datos en cualquier momento, salvo cuando exista un deber legal o contractual de conservarlos.</p>'),
            ("derechos", "Tus derechos", lambda: f'''<p>Como titular de los datos puedes:</p>
                    {UL}
                        <li>Conocer, actualizar y rectificar tus datos personales.</li>
                        <li>Solicitar prueba de la autorización que nos diste.</li>
                        <li>Saber qué uso le hemos dado a tus datos.</li>
                        <li>Revocar la autorización y/o pedir la supresión de tus datos.</li>
                        <li>Acceder gratuitamente a tus datos.</li>
                        <li>Presentar quejas ante la Superintendencia de Industria y Comercio (SIC).</li>
                    </ul>'''),
            ("procedimiento", "Cómo ejercer tus derechos", lambda: f'<p>Escríbenos a <a {A} href="mailto:{EMAIL}">{EMAIL}</a> con el asunto «Datos personales», indicando tu nombre, tu solicitud y cómo quieres recibir la respuesta. Atenderemos las consultas en un máximo de diez (10) días hábiles y los reclamos en un máximo de quince (15) días hábiles, prorrogables en los términos de la ley. Si no quedas satisfecho, puedes acudir a la <a {A} href="https://www.sic.gov.co" target="_blank" rel="noopener">SIC</a>.</p>'),
            ("terceros", "Servicios de terceros", lambda: f'''<p>Para comunicarnos contigo usamos servicios de terceros que tratan los datos bajo sus propias políticas y pueden almacenarlos fuera de Colombia:</p>
                    {UL}
                        <li><strong>WhatsApp</strong> (Meta Platforms) para los mensajes.</li>
                        <li><strong>Outlook / Hotmail</strong> (Microsoft) para el correo.</li>
                    </ul>
                    <p>Al visitar este sitio, tu navegador también se conecta a <strong>Google Fonts</strong> (tipografías e íconos), al <strong>CDN de Tailwind CSS</strong> (estilos) y a <strong>flagcdn.com</strong> (banderas del selector de idioma). Estos servicios pueden recibir tu dirección IP y datos técnicos del navegador. No vendemos ni cedemos tus datos personales.</p>'''),
            ("conservacion", "Conservación y seguridad", lambda: '<p>Conservamos tus datos solo durante el tiempo necesario para las finalidades descritas y para cumplir obligaciones legales (por ejemplo, contables y tributarias). Adoptamos medidas razonables para protegerlos, como limitar el acceso a las personas que atienden tus solicitudes.</p>'),
            ("imagenes", "Imágenes de personas", lambda: '<p>Las fotografías de nuestro local en las que aparecen personas se publican con su autorización. Si apareces en alguna y quieres que la retiremos, escríbenos y lo haremos.</p>'),
            ("cookies", "Política de cookies", lambda: f'''<p>Este sitio <strong>no usa cookies propias, herramientas de analítica ni publicidad</strong>.</p>
                    <p>El mapa de Google Maps no se carga automáticamente: solo aparece si pulsas «Cargar mapa», y en ese momento Google puede instalar cookies según su <a {A} href="https://policies.google.com/technologies/cookies" target="_blank" rel="noopener">propia política</a>. Si prefieres no cargarlo, usa el enlace «Abrir en Google Maps».</p>
                    <p>Si en el futuro incorporamos analítica u otras cookies no esenciales, te pediremos tu consentimiento antes de activarlas y actualizaremos esta política.</p>'''),
            ("cambios", "Cambios a esta política", lambda: '<p>Podemos actualizar esta política. Publicaremos siempre la versión vigente en esta página, con su fecha de actualización.</p>'),
        ],
    },
    "en": {
        "title": "Privacy & Cookie Policy | Costumbres",
        "desc": "How Costumbres handles the personal data it receives via WhatsApp, email and in store, your rights as a data subject, and the use of cookies on this site.",
        "h1": "Privacy & cookie policy",
        "updated": "Last updated: September 26, 2026",
        "toc": "On this page",
        "intro": "At Costumbres we respect your privacy. This policy explains what personal data we receive, how we use it and how you can exercise your rights, in accordance with Colombian Law 1581 of 2012 and Decree 1074 of 2015 (which compiles Decree 1377 of 2013).",
        "sections": [
            ("responsable", "Data controller", lambda: ident("en")),
            ("datos", "What data we receive", lambda: f'''<p>This website is informational: it has no forms, user accounts or online payments. We only receive personal data when you choose to message us on WhatsApp or by email, or when you buy at our store:</p>
                    {UL}
                        <li>Name.</li>
                        <li>Phone number and/or email address.</li>
                        <li>The content of your messages, including any photos you send.</li>
                        <li>If you buy: delivery address and the details required for electronic invoicing.</li>
                    </ul>
                    <p>We do not request sensitive data or data from minors.</p>'''),
            ("finalidades", "How we use your data", lambda: f'''{UL}
                        <li>To answer your questions and quote prices.</li>
                        <li>To confirm availability, prices and reservations.</li>
                        <li>To manage sales, deliveries, exchanges, withdrawals and warranty claims.</li>
                        <li>To issue invoices and meet legal, accounting and tax obligations.</li>
                        <li>To handle requests, complaints and claims.</li>
                        <li>To send you news or promotions, <strong>only if you expressly authorize it</strong>. You can ask us to stop at any time.</li>
                    </ul>'''),
            ("autorizacion", "Your authorization", lambda: '<p>When you contact us on your own initiative (via WhatsApp, email or in store), you authorize us to process your data for the purposes above; that is why we show this notice next to our contact channels and in the footer of every page. You can revoke this authorization or ask us to delete your data at any time, unless there is a legal or contractual duty to keep it.</p>'),
            ("derechos", "Your rights", lambda: f'''<p>As the data subject you can:</p>
                    {UL}
                        <li>Access, update and correct your personal data.</li>
                        <li>Request proof of the authorization you gave us.</li>
                        <li>Be informed of how we have used your data.</li>
                        <li>Revoke your authorization and/or request deletion of your data.</li>
                        <li>Access your data free of charge.</li>
                        <li>File complaints with Colombia's Superintendencia de Industria y Comercio (SIC).</li>
                    </ul>'''),
            ("procedimiento", "How to exercise your rights", lambda: f'<p>Email us at <a {A} href="mailto:{EMAIL}">{EMAIL}</a> with the subject "Personal data", stating your name, your request and how you would like to receive our answer. We answer inquiries within ten (10) business days and claims within fifteen (15) business days, extendable as permitted by law. If you are not satisfied, you can contact the <a {A} href="https://www.sic.gov.co" target="_blank" rel="noopener">SIC</a>.</p>'),
            ("terceros", "Third-party services", lambda: f'''<p>To communicate with you we use third-party services that process data under their own policies and may store it outside Colombia:</p>
                    {UL}
                        <li><strong>WhatsApp</strong> (Meta Platforms) for messages.</li>
                        <li><strong>Outlook / Hotmail</strong> (Microsoft) for email.</li>
                    </ul>
                    <p>When you visit this site, your browser also connects to <strong>Google Fonts</strong> (typefaces and icons), the <strong>Tailwind CSS CDN</strong> (styles) and <strong>flagcdn.com</strong> (language switcher flags). These services may receive your IP address and technical browser data. We do not sell or share your personal data.</p>'''),
            ("conservacion", "Retention and security", lambda: '<p>We keep your data only as long as necessary for the purposes described and to meet legal obligations (for example, accounting and tax). We take reasonable measures to protect it, such as limiting access to the people who handle your requests.</p>'),
            ("imagenes", "Images of people", lambda: '<p>Photos of our store that show people are published with their permission. If you appear in one and want it removed, contact us and we will remove it.</p>'),
            ("cookies", "Cookie policy", lambda: f'''<p>This site <strong>does not use its own cookies, analytics or advertising</strong>.</p>
                    <p>The Google Maps map does not load automatically: it only appears if you press "Load map", at which point Google may set cookies under its <a {A} href="https://policies.google.com/technologies/cookies" target="_blank" rel="noopener">own policy</a>. If you prefer not to load it, use the "Open in Google Maps" link.</p>
                    <p>If we add analytics or other non-essential cookies in the future, we will ask for your consent before enabling them and update this policy.</p>'''),
            ("cambios", "Changes to this policy", lambda: '<p>We may update this policy. The current version will always be published on this page with its update date.</p>'),
        ],
    },
}

TERMS = {
    "es": {
        "title": "Términos y condiciones, garantía y devoluciones | Costumbres",
        "desc": "Condiciones de compra en Costumbres: precios, entregas, derecho de retracto, reversión del pago, garantía de un año, réplicas precolombinas y atención de quejas.",
        "h1": "Términos y condiciones",
        "updated": "Última actualización: 26 de septiembre de 2026",
        "toc": "En esta página",
        "intro": "Estos términos regulan el uso de este sitio web y las compras que hagas a Costumbres por WhatsApp, correo o en nuestra tienda. Se aplican la Ley 1480 de 2011 (Estatuto del Consumidor) y las demás normas colombianas vigentes.",
        "sections": [
            ("vendedor", "Quiénes somos", lambda: ident("es")),
            ("sitio", "Uso de este sitio", lambda: '<p>Este sitio es un catálogo informativo. No se hacen compras ni pagos dentro del sitio: las ventas se acuerdan por WhatsApp, por correo o en la tienda física. La disponibilidad de las piezas puede cambiar sin previo aviso.</p>'),
            ("productos", "Nuestros productos", lambda: '''<p>Nuestras piezas son hechas a mano, por lo que pueden tener pequeñas variaciones de color, tamaño y acabado frente a las fotografías. Estas variaciones son propias del trabajo artesanal y no se consideran un defecto. Si lo pides, te enviamos fotos de la pieza exacta disponible antes de comprar.</p>
                    <p><strong>Réplicas precolombinas.</strong> Las piezas de inspiración precolombina que vendemos son réplicas artesanales contemporáneas. No son piezas arqueológicas originales, que pertenecen a la Nación y no pueden comercializarse (Ley 397 de 1997 y Ley 1185 de 2008).</p>
                    <p><strong>Joyería.</strong> Antes de la compra te informamos el metal y las piedras de cada pieza, y la entregamos con su certificado de garantía.</p>'''),
            ("precios", "Precios", lambda: '<p>Los precios se informan en pesos colombianos (COP) e incluyen los impuestos aplicables. Antes de que pagues te confirmamos por escrito el precio total, incluido el costo de envío si lo hay.</p>'),
            ("compra", "Cómo comprar", lambda: f'''{OL}
                        <li>Escríbenos por WhatsApp o correo con la pieza que te interesa, o visítanos en la tienda.</li>
                        <li>Te confirmamos disponibilidad, precio total, medios de pago y opciones de entrega.</li>
                        <li>Pagas por el medio acordado.</li>
                        <li>Te entregamos la pieza con su factura o comprobante de compra.</li>
                    </ol>
                    <p>En los pedidos personalizados acordamos por escrito las características, el precio y el tiempo de entrega.</p>'''),
            ("entregas", "Entregas", lambda: '<p>Puedes recoger tu compra en la tienda o acordar un envío. El tiempo, el costo y la transportadora se confirman antes del pago. Revisa el paquete al recibirlo e infórmanos cualquier novedad lo antes posible.</p>'),
            ("retracto", "Derecho de retracto", lambda: '''<p>Si compraste a distancia (por WhatsApp, correo u otro medio no presencial), puedes retractarte de la compra dentro de los <strong>cinco (5) días hábiles</strong> siguientes a la entrega del producto (Ley 1480 de 2011, art. 47). Para hacerlo, escríbenos dentro de ese plazo y devuelve la pieza en el mismo estado en que la recibiste. Los costos de transporte de la devolución corren por tu cuenta. Te reintegramos el dinero dentro de los treinta (30) días calendario siguientes, sin descuentos ni retenciones.</p>
                    <p>El retracto no aplica, entre otros casos previstos en la ley, a piezas elaboradas según tus especificaciones o claramente personalizadas, ni a bienes de uso personal. En las compras presenciales en la tienda, los cambios se rigen por la garantía y por lo que acordemos al momento de la compra.</p>'''),
            ("reversion", "Reversión del pago", lambda: '<p>Si en una venta a distancia pagaste con tarjeta de crédito, débito u otro medio de pago electrónico, puedes solicitar la reversión del pago en los casos previstos en la ley: fraude, operación no solicitada, producto no recibido, o producto que no corresponde a lo pedido o es defectuoso (Ley 1480 de 2011, art. 51). Debes presentar la queja ante nosotros y avisar al emisor del medio de pago dentro de los cinco (5) días hábiles siguientes a la fecha en que conociste la situación, y devolver el producto si lo recibiste.</p>'),
            ("garantia", "Garantía", lambda: f'''<p>Costumbres Joyería otorga una garantía sobre sus productos por defectos de fabricación durante <strong>un (1) año</strong>, contado a partir de la fecha de compra. Esta garantía es válida bajo condiciones normales de uso y cuidado, y cubre la reparación gratuita de los defectos del producto. En caso de que el producto no admita reparación o la falla persista, se procederá a su reposición por uno idéntico o de similares características, o con la devolución del dinero pagado.</p>
                    <p>Esta garantía no cubre daños causados por accidente o uso indebido; piedras fracturadas, rayadas o extraviadas; cadenas reventadas por manipulación inadecuada, y el desgaste natural por falta de mantenimiento. Tampoco cubre deterioros originados por el contacto con sustancias como cloro, agua salada, perfumes, cremas, lacas o cualquier otro producto químico o de limpieza.</p>
                    <p>Para hacer efectiva la garantía, escríbenos a <a {A} href="mailto:{EMAIL}">{EMAIL}</a> o acércate a nuestra tienda con tu comprobante de compra. Esta garantía no reemplaza ni limita la garantía legal prevista en los artículos 7 a 17 de la Ley 1480 de 2011.</p>'''),
            ("pqr", "Peticiones, quejas y reclamos", lambda: f'<p>Escríbenos a <a {A} href="mailto:{EMAIL}">{EMAIL}</a> o por WhatsApp. Te responderemos en un máximo de quince (15) días hábiles. Si no estás conforme con la respuesta, puedes acudir a la <a {A} href="https://www.sic.gov.co" target="_blank" rel="noopener">Superintendencia de Industria y Comercio</a>.</p>'),
            ("propiedad", "Propiedad intelectual", lambda: '<p>Los textos, fotografías, logotipo y diseño de este sitio pertenecen a Costumbres o se usan con autorización de sus titulares, y no pueden reproducirse sin permiso. Los diseños y técnicas tradicionales pertenecen al patrimonio cultural de las comunidades que los crean; los nombramos para reconocer su origen.</p>'),
            ("ley", "Ley aplicable", lambda: '<p>Estos términos se rigen por las leyes de la República de Colombia.</p>'),
        ],
    },
    "en": {
        "title": "Terms & Conditions, Warranty and Returns | Costumbres",
        "desc": "Purchase terms at Costumbres: prices, deliveries, right of withdrawal, payment reversal, one-year warranty, pre-Columbian replicas and complaints.",
        "h1": "Terms and conditions",
        "updated": "Last updated: September 26, 2026",
        "toc": "On this page",
        "intro": "These terms govern the use of this website and any purchase you make from Costumbres via WhatsApp, email or at our store. Colombian Law 1480 of 2011 (Consumer Statute) and other applicable Colombian laws apply.",
        "sections": [
            ("vendedor", "Who we are", lambda: ident("en")),
            ("sitio", "Use of this site", lambda: '<p>This site is an informational catalog. No purchases or payments are made on the site: sales are arranged via WhatsApp, email or at our physical store. Availability may change without notice.</p>'),
            ("productos", "Our products", lambda: '''<p>Our pieces are handmade, so they may show small variations in color, size and finish compared with the photos. These variations are part of handcrafted work and are not considered defects. If you ask, we will send you photos of the exact piece available before you buy.</p>
                    <p><strong>Pre-Columbian replicas.</strong> The pre-Columbian-inspired pieces we sell are contemporary handcrafted replicas. They are not original archaeological pieces, which belong to the Colombian Nation and cannot be sold (Law 397 of 1997 and Law 1185 of 2008).</p>
                    <p><strong>Jewelry.</strong> Before you buy, we tell you the metal and stones of each piece, and we deliver it with its warranty certificate.</p>'''),
            ("precios", "Prices", lambda: '<p>Prices are stated in Colombian pesos (COP) and include applicable taxes. Before you pay, we confirm the total price in writing, including shipping if any.</p>'),
            ("compra", "How to buy", lambda: f'''{OL}
                        <li>Message us on WhatsApp or by email with the piece you like, or visit our store.</li>
                        <li>We confirm availability, the total price, payment methods and delivery options.</li>
                        <li>You pay using the agreed method.</li>
                        <li>We deliver the piece with its invoice or proof of purchase.</li>
                    </ol>
                    <p>For custom orders, we agree in writing on the features, price and delivery time.</p>'''),
            ("entregas", "Deliveries", lambda: '<p>You can pick up your purchase at the store or arrange shipping. Delivery time, cost and carrier are confirmed before payment. Please check the package on arrival and let us know about any issue as soon as possible.</p>'),
            ("retracto", "Right of withdrawal", lambda: '''<p>If you bought remotely (via WhatsApp, email or another non-in-person channel), you may withdraw from the purchase within <strong>five (5) business days</strong> after delivery (Law 1480 of 2011, art. 47). To do so, contact us within that period and return the piece in the same condition you received it. Return shipping costs are paid by you. We refund the money within thirty (30) calendar days, with no deductions.</p>
                    <p>Withdrawal does not apply, among other cases set by law, to pieces made to your specifications or clearly personalized, or to goods for personal use. For in-store purchases, exchanges are governed by the warranty and by what we agree at the time of purchase.</p>'''),
            ("reversion", "Payment reversal", lambda: '<p>If you paid for a remote purchase by credit card, debit card or another electronic payment method, you may request a payment reversal in the cases set by law: fraud, an unrequested transaction, a product not received, or a product that does not match your order or is defective (Law 1480 of 2011, art. 51). You must file the complaint with us and notify the payment issuer within five (5) business days of learning of the situation, and return the product if you received it.</p>'),
            ("garantia", "Warranty", lambda: f'''<p>Costumbres Jewelry grants a warranty on its products against manufacturing defects for <strong>one (1) year</strong> from the date of purchase. This warranty is valid under normal conditions of use and care, and covers the free repair of product defects. If the product cannot be repaired or the defect persists, it will be replaced with an identical item or one with similar characteristics, or the amount paid will be refunded.</p>
                    <p>This warranty does not cover damage caused by accidents or improper use; broken, scratched or lost stones; chains broken by improper handling; or natural wear and tear due to lack of maintenance. It also does not cover deterioration caused by contact with substances such as chlorine, salt water, perfumes, creams, nail polish or any other chemical or cleaning products.</p>
                    <p>To make the warranty effective, email us at <a {A} href="mailto:{EMAIL}">{EMAIL}</a> or visit our store with your proof of purchase. This warranty does not replace or limit the legal warranty set out in articles 7 to 17 of Law 1480 of 2011.</p>'''),
            ("pqr", "Requests, complaints and claims", lambda: f'<p>Email us at <a {A} href="mailto:{EMAIL}">{EMAIL}</a> or message us on WhatsApp. We will answer within fifteen (15) business days. If you are not satisfied with our answer, you can contact Colombia\'s <a {A} href="https://www.sic.gov.co" target="_blank" rel="noopener">Superintendencia de Industria y Comercio</a>.</p>'),
            ("propiedad", "Intellectual property", lambda: '<p>The texts, photos, logo and design of this site belong to Costumbres or are used with their owners\' permission, and may not be reproduced without authorization. Traditional designs and techniques belong to the cultural heritage of the communities that create them; we name them to acknowledge their origin.</p>'),
            ("ley", "Governing law", lambda: '<p>These terms are governed by the laws of the Republic of Colombia.</p>'),
        ],
    },
}


def body(lang, C):
    toc = "\n".join(f'                        <li><a {A} href="#{sid}">{h}</a></li>' for sid, h, _ in C["sections"])
    secs = "\n".join(f'''                <section id="{sid}" class="scroll-mt-28 space-y-4">
                    <h2 class="font-headline-md text-headline-md text-on-surface">{i}. {h}</h2>
                    {fn()}
                </section>''' for i, (sid, h, fn) in enumerate(C["sections"], 1))
    return f'''    <main id="contenido" class="max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop pt-32 pb-16">
        <article class="max-w-3xl">
            <h1 class="font-display-lg text-display-lg-mobile md:text-display-lg text-primary mb-4 leading-tight">{C["h1"]}</h1>
            <p class="font-label-md text-label-md text-on-surface-variant">{C["updated"]}</p>
            <p class="font-body-lg text-body-lg text-on-surface-variant mt-6">{C["intro"]}</p>
            <nav aria-labelledby="toc-titulo" class="my-10 p-6 bg-surface-container-low rounded-xl border border-primary/10">
                <h2 id="toc-titulo" class="font-label-md text-label-md text-on-surface mb-3">{C["toc"]}</h2>
                <ol class="list-decimal pl-6 space-y-1 font-body-md text-body-md">
{toc}
                </ol>
            </nav>
            <div class="space-y-10 font-body-md text-body-md text-on-surface-variant leading-relaxed">
{secs}
            </div>
        </article>
    </main>
'''


def build(lang, kind):
    P = "" if lang == "es" else "../"
    C = (PRIV if kind == "privacidad" else TERMS)[lang]
    alt = f"en/{kind}.html" if lang == "es" else f"../{kind}.html"
    return page(lang, P, kind, alt, C["title"], C["desc"], [], body(lang, C), ["nav"])
