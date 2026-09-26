# Prompts para mejorar Costumbres con Claude Code

Abre Claude Code en la carpeta `Costumbres_Web_v3` (ahí están `CLAUDE.md` y `.claude/skills/`).
Un prompt por fase. Revisa el resultado antes de pasar a la siguiente.

---

## Fase 1 — Diagnóstico (no cambia nada)
```
Usa ui-ux-pro-max y frontend-design para auditar las 4 páginas en español.
Levanta el sitio y toma capturas desktop y móvil con webapp-testing.
Dame una lista priorizada (impacto alto → bajo) de problemas de diseño, UX,
accesibilidad y rendimiento, con la página y sección exacta de cada uno.
No modifiques ningún archivo todavía.
```

## Fase 2 — Dirección de diseño
```
Con ui-ux-pro-max genera un sistema de diseño para una tienda de joyería y
artesanía colombiana, partiendo de los tokens actuales de tailwind-config.js.
Propón solo los ajustes necesarios (paleta, escala tipográfica, espaciado,
sombras, radios) y explica por qué. Muéstrame el antes/después de los tokens.
No apliques nada aún.
```

## Fase 3 — Implementación, sección por sección
```
Aplica el sistema de diseño aprobado al hero de index.html.
Sigue karpathy-guidelines: cambia solo esa sección.
Replica el cambio en en/index.html conservando los textos en inglés.
Al terminar, toma capturas desktop y móvil en ES y EN y revísalas.
```
Repite cambiando la sección/página: catálogo, "Visítanos", footer, categorías, historia, contacto.

## Fase 4 — Rendimiento
```
Optimiza las imágenes: convierte a WebP, genera tamaños adecuados para donde
se muestran (el ícono del nav se ve a 48px), agrega loading="lazy" a todo lo
que esté bajo el primer pantallazo y width/height para evitar saltos.
Dime cuánto peso se ahorró.
```

## Fase 5 — Accesibilidad y cierre
```
Revisa accesibilidad WCAG AA con las reglas de ui-ux-pro-max: contraste,
alt de imágenes, foco visible, navegación con teclado, tamaños táctiles,
prefers-reduced-motion en carruseles y animaciones. Corrige lo que falle
y verifica con webapp-testing en ES y EN.
```

---

### Tips
- Nombra la skill en el prompt si quieres asegurarte de que la use.
- Pide "no cambies nada todavía" en fases de análisis: evita reescrituras grandes.
- Si algo no te gusta: "revierte el último cambio" o usa git (`git init` antes de empezar).
