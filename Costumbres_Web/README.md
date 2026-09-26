# Costumbres — sitio web

Sitio estático bilingüe (español en la raíz, inglés en `en/`) de Costumbres, joyería y artesanía colombiana. No tiene backend: las ventas se hacen por WhatsApp o en la tienda. Se puede publicar tal cual en Cloudflare Pages (sin paso de build; carpeta de salida: `Costumbres_Web`).

## Ver en local

```bash
python -m http.server 8000
```

Abrir http://localhost:8000

## Datos pendientes antes de publicar

Buscar y reemplazar en **todas** las páginas (ES y EN):

| Qué | Texto a buscar | Dónde aparece |
|---|---|---|
| Número de WhatsApp | `573000000000` | Botones, tarjetas de productos, páginas legales |
| Razón social | `[RAZÓN SOCIAL]` / `[LEGAL BUSINESS NAME]` | Footer, privacidad, términos |
| NIT | `[000.000.000-0]` | Footer, privacidad, términos |
| Dirección | `Calle 16 # 5-24, Local 11` | Inicio, contacto, footer, legales (confirmar que sea la real) |
| Horario | `10:00` | Inicio, contacto (confirmar horario real) |
| Facebook / TikTok | comentario `PENDIENTE` en el footer | Footer |
| Dominio | comentario en el `<head>` | Agregar `og:image`, `canonical` y `hreflang` con URL absoluta |

Además:
- Pedir **autorización escrita** a las personas que aparecen en las fotos del local (`img/local/`).
- Confirmar con quien entregó las ilustraciones de `img/hero/` que se pueden usar comercialmente.
- Revisar las páginas `privacidad.html` y `terminos.html` con un abogado o contador.

## Estructura

```
index.html  categorias.html  historia.html  contacto.html   páginas principales
privacidad.html  terminos.html                              política de datos/cookies y términos/garantía
en/                                                          las mismas 6 páginas en inglés
css/   base.css (compartido) + uno por página
js/    tailwind-config.js (tokens), nav.js, carrusel.js, mapa.js, reveal.js, contacto.js
img/   hero, artesanias, joyas, local, logos (icono-96/192 y logo-320 son copias livianas)
```
