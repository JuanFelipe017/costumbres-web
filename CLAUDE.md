# Costumbres — sitio web

Sitio de **Costumbres, joyería y artesanía colombiana**. Sitio estático bilingüe (español / inglés), sin build.

## Stack
- HTML estático + **Tailwind vía CDN** (`cdn.tailwindcss.com`, plugins forms y container-queries).
- Tokens de diseño en `Costumbres_Web/js/tailwind-config.js` (colores estilo Material 3: `primary` #6d9773, `secondary` #275667, `background` #fdf9f4; fuentes **Bricolage Grotesque** para títulos y **Be Vietnam Pro** para texto; espaciados `margin-desktop`, `margin-mobile`, `gutter`, `container-max`).
- CSS mínimo por página en `css/` (`base.css` es compartido; incluye `.organic-texture`).
- JS vanilla en `js/`: `nav.js` (menú móvil, compartido), `carrusel.js` (carrusel automático con `[data-carousel]`), un JS por página.
- Íconos: Material Symbols Outlined (Google Fonts). Banderas desde flagcdn.com.

## Estructura
```
Costumbres_Web/
  index.html  categorias.html  historia.html  contacto.html   ← español
  en/ (mismas 4 páginas)                                     ← inglés
  css/  js/  img/{hero,artesanias,joyas,local,logos}
```

## Cómo verlo
```bash
cd Costumbres_Web && python -m http.server 8000
# http://localhost:8000
```

## Reglas del proyecto
- **Español e inglés siempre sincronizados**: cualquier cambio de diseño o estructura en una página ES se replica en su par de `en/` conservando los textos en inglés (no re-traducir lo que ya existe).
- Usar los tokens de `tailwind-config.js`; no meter colores hex ni tamaños sueltos en las clases. Si falta un token, agregarlo al config.
- Mantener la identidad: paleta verde/azul natural, textura orgánica, tono artesanal colombiano.
- Cambios quirúrgicos (skill `karpathy-guidelines`): tocar solo lo pedido, sin reescribir páginas enteras.
- Después de cada cambio visual: capturas desktop + móvil con `webapp-testing`, en ES y EN.
- No agregar frameworks ni un paso de build salvo que se pida.

## Puntos conocidos a revisar
- `img/logos/icono.png` pesa ~1.4 MB y se muestra a 48 px de alto en el nav.
- Imágenes hero de 0.8–1.2 MB y `garantia-en.jpg` de 1.4 MB (vs 190 KB la versión ES); sin `loading="lazy"` / WebP.
- Tailwind Play CDN no está pensado para producción (compila en el navegador).
- `README.md` vacío.

## Skills disponibles en `.claude/skills/`
- `ui-ux-pro-max` — sistema de diseño, paletas, tipografía, reglas UX y accesibilidad (base de datos local).
- `frontend-design` — dirección estética, evitar diseño genérico.
- `karpathy-guidelines` — cambios mínimos y verificables.
- `webapp-testing` — capturas y revisión de consola con Playwright.
