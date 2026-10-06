# Análisis de la Brecha Salarial y Precarización Laboral en Argentina
**Fuente:** Encuesta Permanente de Hogares (EPH - INDEC) | 1° Trimestre 2026.

##  Objetivo del Proyecto
Analizar empíricamente la estructura de ingresos de la población ocupada en Argentina mediante el procesamiento de microdatos, evaluando el impacto del género, el nivel educativo y la informalidad laboral en la brecha salarial.

##  Herramientas Utilizadas
* **Lenguaje:** Python
* **Librerías:** Pandas (limpieza y manipulación de datos), Matplotlib y Seaborn (visualización).
* **Metodología:** Uso de la Mediana salarial (aislamiento de outliers) y cruce de variables categóricas.

##  Hallazgos Principales

1. **Brecha General:** Las mujeres ocupadas perciben un 14,28% menos que los varones en el sector formal, tomando como referencia la mediana de ingresos.
2. **Penalidad Educativa:** La educación superior eleva la base salarial general, pero no elimina la brecha de género; por el contrario, la diferencia absoluta se amplía en los niveles de mayor instrucción.
3. **El Peso de la Informalidad:** La ausencia de regulación estatal (trabajo no registrado) reduce drásticamente los ingresos para ambos géneros (una caída de más del 50% respecto al sector formal). La leve reducción porcentual de la brecha en este sector (12,27%) se debe a una "igualdad hacia abajo" que precariza la base salarial y la empuja hacia límites de subsistencia.

##  Reproducción del Proyecto

Para replicar este análisis en tu entorno local, seguí estos pasos:

1. **Instalar las dependencias necesarias:**
   Asegurate de tener Python 3 instalado. Abrí tu terminal y ejecutá:
   ```bash
   pip install pandas matplotlib seaborn openpyxl