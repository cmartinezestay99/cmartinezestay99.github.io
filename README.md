# Página académica de Camilo Martínez Estay

Sitio estático para GitHub Pages, sin framework ni proceso de compilación.

- [Sitio publicado](https://cmartinezestay99.github.io/)
- [Guía de edición](LEEME.md)
- [Borradores de redacción en inglés](en/README.md)

La fotografía personal se incluye únicamente en `index.html` de la raíz. Los contenidos académicos se editan directamente en cada HTML. La paleta y distribución están en `theme.css`; las reglas base y de impresión, en `styles.css`.

Para verificar enlaces y estructura: `python tools/check_site.py`.
Para previsualizar: `python -m http.server 8765` y abrir `http://127.0.0.1:8765/`.
