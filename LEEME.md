# Publicar y editar tu página

La web está preparada para GitHub Pages. No necesita instalar paquetes ni ejecutar un proceso de compilación. La dirección local 127.0.0.1 sirve para verla en tu computador; no es la dirección pública.

## Primera publicación

1. Extrae el ZIP actualizado `web-matematica.zip` en una carpeta.
2. En GitHub, crea un repositorio **público** llamado exactamente `cmartinezestay99.github.io`. Puedes marcar «Add a README file» para inicializar la rama `main`.
3. En el repositorio, selecciona **Add file → Upload files**. Arrastra los archivos HTML, `styles.css`, `theme.css`, `.nojekyll` y la carpeta `assets` del ZIP extraído. Conserva la carpeta `assets` y su contenido. No subas el ZIP ni una carpeta envolvente: `index.html` debe quedar directamente en la raíz del repositorio. Los archivos Markdown de instrucciones son opcionales.
4. Guarda la subida con **Commit changes** en `main`.
5. En **Settings → Pages**, selecciona **Deploy from a branch**, rama **main**, carpeta **/(root)** y pulsa **Save**.
6. Espera a que termine el despliegue. Settings → Pages mostrará el enlace del sitio. Puedes ver el resultado del proceso en la pestaña **Actions**.

Tu dirección será **https://cmartinezestay99.github.io/**. GitHub Pages está disponible para repositorios públicos con GitHub Free. No necesitas comprar dominio.

Si `.nojekyll` no aparece al seleccionar los archivos, puedes crearlo en GitHub con **Add file → Create new file**, ese nombre exacto y sin contenido.

## Cambios pequeños desde GitHub

Abre el archivo que quieres modificar, pulsa el lápiz **Edit**, cambia el texto y guarda con **Commit changes**. El cambio debe llegar a `main`; si trabajas en otra rama, intégralo mediante un pull request. Pages actualizará automáticamente la web después del despliegue.

| Qué quieres cambiar | Archivo |
|---|---|
| Biografía y actualidad | `index.html` |
| Investigación | `research.html` |
| Docencia | `teaching.html` |
| Apuntes y presentaciones | `resources.html` |
| Archivo LIMA215 | `lima215.html` |
| Códigos y enlaces a repositorios | `programs.html` |
| Seminario, charlas y actividades | `activities.html` |
| CV resumido | `cv.html` |
| Colores, distribución, tamaños y retrato | `theme.css` |
| Estilos base | `styles.css` |
| Foto | `assets/camilo-martinez-estay.png` |

Para cambiar una frase, modifica solo el texto dentro de las etiquetas. Ejemplo:

```html
<p>Estoy trabajando en un nuevo proyecto sobre álgebras graduadas.</p>
```

Para enlazar un repositorio real desde Programas:

```html
<a href="https://github.com/cmartinezestay99/NOMBRE-REAL">Código en GitHub</a>
```

El menú, el perfil lateral y el pie están repetidos en los ocho HTML. Si cambias el correo, el nombre o la navegación, actualízalos en todos los archivos. La foto se comparte y basta sustituir el archivo conservando su nombre; su encuadre puede necesitar un ajuste en CSS.

## Trabajar con ayuda

Puedes pedirme cambios en lenguaje natural, por ejemplo: «añade esta charla y enlaza estas diapositivas». Para modificar la versión publicada trabajaremos sobre el repositorio actualizado, evitando reemplazar cambios nuevos con una copia local antigua. Guardar un archivo local no publica nada por sí solo: los cambios deben subirse a GitHub.

Para una edición manual local, usa un editor de texto, guarda y abre `index.html` en tu navegador. Cuando esté listo, sube los archivos modificados a las mismas rutas del repositorio. Si un cambio de estilo tarda en verse, recarga con Ctrl+F5.

## Añadir tus códigos de Python

Mantén la web en este repositorio y cada proyecto de investigación en su propio repositorio. Puedes continuar usando Colab para ejecutar cuadernos y GitHub para guardar y compartir versiones. En `programs.html` se añade el enlace al repositorio y, cuando exista, al cuaderno de Colab. Cada proyecto debería incluir instrucciones, dependencias y un ejemplo pequeño reproducible.

## Documentación oficial

- [Inicio rápido de GitHub Pages](https://docs.github.com/en/pages/quickstart)
- [Configurar la rama de publicación](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [Subir archivos](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)
- [Editar archivos en GitHub](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)

Versión actual: ocho páginas, sin la sección Exploraciones. No se ha publicado todavía.
