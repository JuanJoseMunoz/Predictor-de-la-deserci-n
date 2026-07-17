# Student Dropout Prediction

Aplicación Streamlit para una prueba piloto de predicción del riesgo de deserción estudiantil mediante Random Forest.

## Ejecución

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

La predicción individual y masiva entrena el modelo una vez por sesión a partir de los CSV incluidos en `datasets/train` y evalúa con `datasets/test`. Esto evita depender de artefactos de modelo dañados o desactualizados.

## Predicción masiva

El CSV debe incluir las 36 columnas de características del entrenamiento. La página muestra la lista exacta de columnas requeridas y permite descargar el resultado con probabilidades y clasificación.

`0` significa riesgo de deserción y `1` significa permanencia/no riesgo.
