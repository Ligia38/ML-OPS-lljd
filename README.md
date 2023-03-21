<h1 align=center> PROYECTO I: Ingeniería de Datos y Machine Learning (ML-OPS)</h1>

Este proyecto se divide en cuatro etapas, las cuales se muestran en el siguiente diagrama:
<p align="center">
<img src="src/etapas.png"  height=400>
</p>

<h2 align=center> PRIMERA PARTE: ETL </h2>

Se realizaron las siguienter transformaciones a los datos extraidos de .csv proveniente de la carpeta `data`: </br>
1. Se generó el campo id: Cada ide está conformado por la primera letra de la plataforma seguido del show_id ya presente anteriormente en los datasets. </br> 
2. Los valores nulos del campo 'rating' fueron sustituidos por la cadena "G" (Correspondiente al maturity rating: "General for all audiences"). </br>
3. Se modificó la columna de fechas para que cumplieran con el formato AAA-MM-DD. </br>
4. Se separo el campo 'duration' en  'duration_int' y 'duration_type'.

<h2 align=center> SEGUNDA PARTE: API </h2>

Se desarrolló una API utilizando el Framework FastAPI. Las consultas disponibles son las siguientes: </br>
- / : Home </br>
- get_max_duration/year/platform/duration_type: Película con mayor duración con filtros de año, plataforma y tipo de duración. </br>
- get_score_count/platform/scored/year: Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año. </br>
- get_count_platform/platform: Cantidad de películas por plataforma. </br>
- get_actor/platform/year: Actor que  más se repite según plataforma y año. </br>

Para el despliegue de la API se utilizó rebder: https://render.com/ </br>

Link de acceso a la API: https://api-ml-ops-lljd.onrender.com </br>

Link opcional: https://api-ml-ops-lljd.onrender.com/docs </br>
<p align="center">
<img src="src/FastAPI.png"  height=400>
</p>


<h2 align=center> PRÓXIMAS MEJORAS </h2>
- Explicación del modelo SVD. </br>
- Evaluación del modelo de recomendación.</br>
- Optimización de hiperámetros.</br>
- Creación de una SPA (Single Page Aplication) del proyecto utilizando React. </br>