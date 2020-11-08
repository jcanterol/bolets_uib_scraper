# TCD [PRA1] Bolets de les Balears

## Descripción

En este repositorio se presenta el proyecto asociado a la PRA1 de las asignatura _Tipología y Ciclo de Vida de los Datos_ del Máster en Ciencia de Datos de la Universitat Oberta de Cataluña.

Mediante técnicas de Web Scraping implementadas en Python se extrae la información contenida en la página http://bolets.uib.es/cas/index.html para generar así un catálogo micológico de las Islas Baleares en un formato unificado y adecuado para el análisis de los datos.

## Equipo

Esta práctica ha sido realizada de manera individual por **Javier Cantero Lorenzo** tras la autorización del profesor responsable de la asignatura el día 09 de Octubre de 2020.

## Ejecución

Para la ejecución del script es necesario instalar las siguientes librerías:

```
pip install requests
pip install pandas
pip install beautifulsoup4
```

## Archivos

- **src/main.py:** Archivo principal que ejecuta el servicio de scraping.
- **src/utils.py:** Funciones genéricas de consulta web y limpieza de textos.
- **src/process.py:** Funciones de preprocesado de los datos.

## Descripción del conjunto de datos

La semántica de los distintos atributos del conjunto de datos es la siguiente:

- **scientific_name:** Nombre científico oficial.
- **family:** Familia taxonómica.
- **genre:** Género taxonómico.
- **alternative_scientific_names:** Nombres científicos alternativos siguiendo otros sistemas de nomenclatura.
- **ca_common_name:** Nombres populares en catalán.
- **es_common_name:** Nombres populares en español.
- **description:** Descripción detallada.
- **additional_info:** Notas adicionales.
- **islands:** Islas del archipiélago balear en donde se encuentra la seta.
- **habitat:** Hábitats.
- **edibility:** Toxicidad alimentaria.

## Licencia

Este proyecto cuenta con licencia **CC BY-NC-SA 4.0 License**.

## Agradecimientos

Esta práctica no podría haber sido realizada de no ser por los autores del libro ‘Els bolets de les Balears’ (Micobalear, C.B.) Carles Constantino y Josep L. Siquier, quienes condujeron el peso del estudio y catálogo de la micología de las Islas Baleares.

Del mismo modo agradecer al Museu Balear de Ciències Naturals y la Universitat de les Illes Balears por la digitalización del libro anterior con el patrocinio de Obra Social Sa Nostra Caixa de Balears.
