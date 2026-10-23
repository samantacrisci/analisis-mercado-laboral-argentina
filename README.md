# Análisis de la Brecha Salarial y Precarización Laboral en Argentina
**Fuente:** Encuesta Permanente de Hogares (EPH - INDEC) | 1° Trimestre 2026.

##  Objetivo del Proyecto
Analizar empíricamente la estructura de ingresos de la población ocupada en Argentina mediante el procesamiento de microdatos, evaluando el impacto del género, el nivel educativo y la informalidad laboral en la brecha salarial.

##  Herramientas Utilizadas
* **Lenguaje:** Python
* **Librerías:** Pandas (limpieza y manipulación de datos), Matplotlib y Seaborn (visualización).
* **Metodología:** Uso de la Mediana salarial (aislamiento de outliers) y cruce de variables categóricas.

##  Hallazgos Principales

## Hallazgos principales

**Muestra:** 15.182 personas ocupadas con ingresos válidos (de 43.739 encuestadas).

1. **Brecha general:** las mujeres ocupadas perciben un 18,0% menos que los varones, tomando la mediana del ingreso total individual ($820.000 vs. $1.000.000).
2. **La educación no cierra la brecha:** en todos los niveles educativos la mediana de las mujeres es menor. La diferencia en pesos es mayor en los niveles más altos (de $82.150 en Primario incompleto a $332.500 en Superior completo), aunque en términos porcentuales la brecha no crece: ronda el 30% en Secundario completo y baja al 20% en Superior completo.
3. **El peso de la informalidad:** entre asalariados, el trabajo no registrado reduce la mediana de ingresos más de un 50% para ambos géneros (54% en mujeres y 55% en varones). La brecha porcentual es de 14,3% entre registrados y 12,3% entre no registrados: baja levemente porque los ingresos de ambos géneros se achatan hacia abajo.

##  Reproducción del Proyecto

Para replicar este análisis en tu entorno local, seguí estos pasos:

1. **Instalar las dependencias necesarias:**
   Asegurate de tener Python 3 instalado. Abrí tu terminal y ejecutá:
   ```bash
   pip install pandas matplotlib seaborn openpyxl

   ## Limitaciones

- La variable de ingreso utilizada es el **ingreso total individual** (`P47T`), que incluye todas las fuentes de ingreso y no solo el salario de la ocupación principal.
- No se controla por horas trabajadas, edad ni rama de actividad, por lo que la brecha es **bruta** y no ajustada.
- No se aplicaron ponderadores muestrales de la EPH: los resultados describen la muestra analizada.
- La EPH releva aglomerados urbanos, no la totalidad del país.
- Los porcentajes de brecha se calculan sobre la mediana; las comparaciones por nivel educativo y condición de registro se hacen sobre subgrupos más pequeños, por lo que son menos estables.
