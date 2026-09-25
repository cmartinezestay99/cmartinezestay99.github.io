# De Google Drive / Colab a tu página

Si escribes y ejecutas Python en Google Colab, tus archivos suelen ser cuadernos `.ipynb` guardados en Drive. Puedes seguir trabajando allí: no necesitas convertirlos a otro formato para compartirlos en GitHub.

## Flujo recomendado

1. Escoge un cuaderno que quieras compartir.
2. Desde el menú Archivo de Colab, descarga el cuaderno en formato `.ipynb` (también se puede descargar desde Drive).
3. Crea un repositorio en GitHub para el proyecto e incorpora el cuaderno. Añade un README que explique el problema matemático, qué calcula y cómo ejecutar el ejemplo.
4. Incluye las dependencias y los datos necesarios. Los archivos que solo están en tu Drive y las bibliotecas instaladas en una sesión no viajan automáticamente con el cuaderno.
5. En `programs.html` añade un enlace al archivo en GitHub y otro para abrirlo en Colab.

Formato del enlace de Colab, reemplazando REPOSITORIO y CUADERNO por los nombres reales:

`https://colab.research.google.com/github/cmartinezestay99/REPOSITORIO/blob/main/CUADERNO.ipynb`

Así, los visitantes pueden leer el código en GitHub y ejecutarlo en Colab. No se han añadido botones vacíos o enlaces ficticios a la web: se incorporarán cuando exista el primer cuaderno.

## Alternativa inicial

También puedes enlazar un cuaderno de Colab compartido para lectura. Es una forma rápida de empezar; GitHub facilita además mantener versiones del código y relacionarlas con los trabajos de investigación.

Si en Drive guardas scripts `.py` en lugar de cuadernos, pueden subirse al repositorio como tales, junto a sus instrucciones de uso.

## Qué preparar para un ejemplo de investigación

- Una explicación breve del objeto matemático y del propósito del cálculo.
- Un ejemplo pequeño con entradas y resultados esperados.
- Las bibliotecas y archivos necesarios para ejecutarlo desde una sesión nueva.
- La relación con el manuscrito o artículo, si corresponde.

Fuentes: https://research.google.com/colaboratory/faq.html y https://github.com/googlecolab/open_in_colab


## Propuesta para tus archivos actuales

Mantén Colab como entorno para experimentar. Usa un repositorio de GitHub por proyecto para conservar versiones y presentar el código: uno para categoría NT y otro para Hom-Lie. Los nombres de repositorio se decidirán al crearlos.

En Drive se identificaron estas versiones para empezar:
- Hom Lie dim 4 - Python: https://colab.research.google.com/drive/1gtlrbaxCQ6W5Xb4FIG0lNa0qadpo0yAZ
- Categoría NT_ version final.ipynb: https://drive.google.com/file/d/1_34xb7IYpzIVJhGrdQzZ3HI338zH0oDR/view

Se revisaron las celdas y las descripciones; no se ejecutaron ni se validaron los resultados matemáticos. La versión NT tiene metadatos de colaboración, por lo que la autoría y la licencia deben quedar correctamente documentadas al preparar su versión pública. Los archivos originales y sus permisos no se modificaron. Esta guía es para ti y no está enlazada desde el menú público.
