# Tu versión en inglés

Esta carpeta contiene solo la estructura de la web. Los textos entre corchetes son marcadores para que practiques tu propia redacción.

La entrada es `en/index.html`. El menú conserva las seis secciones de la versión española, además del CV y el archivo del curso. El selector Español / English lleva a la página equivalente.

| Qué escribir | Archivo |
|---|---|
| Presentación e intereses | `index.html` |
| Investigación | `research.html` |
| Docencia, con PMI y PAE separados | `teaching.html` |
| Apuntes y materiales | `resources.html` |
| Proyectos de código | `programs.html` |
| Charlas y actividades | `activities.html` |
| CV | `cv.html` |
| Archivo del curso | `lima215.html` |

## Cómo completar una sección

1. Abre el archivo en GitHub y selecciona Edit.
2. Sustituye los marcadores entre corchetes por tu texto, conservando las etiquetas HTML.
3. Quita `writing-placeholder` de la clase de los párrafos que completes. Por ejemplo:

```html
<p class="writing-placeholder">[Write here]</p>
```

se convierte en:

```html
<p>Tu texto en inglés.</p>
```

4. Guarda con Commit changes. GitHub Pages actualizará el sitio.

Las ocho páginas comparten el encabezado textual, el diseño y los enlaces de contacto. No incluyen fotografía: esta aparece solo en `index.html` de la raíz. Cada página inglesa muestra “English draft · In progress”; puedes quitar esa línea al terminarla. Añade enlaces reales a tus materiales cuando estén listos.

`../styles.css` y `../theme.css` controlan el diseño compartido. `scaffold.css` solo da formato a los marcadores. No hay contenido redactado automáticamente sobre tu trayectoria o tus proyectos en esta versión.

Los avisos de borrador enlazan la versión española y el CV completo en inglés. Se conservan tus marcadores para redactar personalmente. Quita `noindex, follow` y los avisos cuando la traducción esté terminada y revisada.
