import pandas as pd

print("Cargando la base de datos individual... (Puede demorar unos segundos)")
# Leemos el archivo Excel de personas
df_ind = pd.read_excel("usu_individual_T126.xlsx")

# Imprimimos la cantidad de filas y columnas
print(f"La base se cargó correctamente.")
print(f"Total de personas encuestadas: {df_ind.shape[0]}")
print(f"Total de variables (columnas): {df_ind.shape[1]}")

# Mostramos las variables básicas demográficas según el diccionario
# CH04: Sexo | CH06: Edad | ESTADO: Condición de actividad
columnas_basicas = ['CODUSU', 'CH04', 'CH06', 'ESTADO', 'P47T']
print("\nPrimeras 5 filas de muestra:")
print(df_ind[columnas_basicas].head())

# 1. Filtrar solo a las personas ocupadas (ESTADO = 1)
df_ocupados = df_ind[df_ind['ESTADO'] == 1].copy()

# 2. Eliminar las "no respuestas" (-9) y quedarnos estrictamente con ingresos positivos
df_ocupados = df_ocupados[df_ocupados['P47T'] > 0]

# 3. Mapear los códigos numéricos a texto usando el diccionario del INDEC
# CH04: 1 = Varón, 2 = Mujer
df_ocupados['Sexo'] = df_ocupados['CH04'].map({1: 'Varón', 2: 'Mujer'})
# CH06 es la Edad, la renombramos para mayor claridad
df_ocupados.rename(columns={'CH06': 'Edad', 'P47T': 'Ingreso_Total'}, inplace=True)

print(f"\n--- Limpieza Finalizada ---")
print(f"Total de ocupados con ingresos válidos: {len(df_ocupados)}")
print("\nMuestra de los datos limpios:")
print(df_ocupados[['CODUSU', 'Sexo', 'Edad', 'Ingreso_Total']].head())

# 1. Agrupar por sexo y calcular promedio (mean) y mediana (median)
resumen_ingresos = df_ocupados.groupby('Sexo')['Ingreso_Total'].agg(['mean', 'median']).round(2)

# 2. Renombrar las columnas para que el cuadro final sea presentable
resumen_ingresos.columns = ['Ingreso Promedio', 'Ingreso Mediano']

print("\n--- RESUMEN DE INGRESOS POR GÉNERO ---")
print(resumen_ingresos)

# 3. Calcular la brecha salarial porcentual basándonos en la Mediana
mediana_varon = resumen_ingresos.loc['Varón', 'Ingreso Mediano']
mediana_mujer = resumen_ingresos.loc['Mujer', 'Ingreso Mediano']

brecha_porcentual = ((mediana_varon - mediana_mujer) / mediana_varon) * 100

print(f"\nBrecha Salarial Estimada: En esta muestra, las mujeres perciben un {brecha_porcentual:.1f}% menos que los varones (tomando la mediana).")

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# 1. Configurar el estilo del gráfico
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 6))

# 2. Crear el gráfico de barras apuntando a la Mediana
# (resumen_ingresos ya lo creamos en el paso anterior)
ax = sns.barplot(
    x=resumen_ingresos.index, 
    y=resumen_ingresos['Ingreso Mediano'], 
    palette="pastel"
)

# 3. Función para formatear el eje Y como dinero ($1,000,000)
def formato_moneda(x, pos):
    return f'${x:,.0f}'.replace(',', '.')

ax.yaxis.set_major_formatter(FuncFormatter(formato_moneda))

# 4. Títulos y etiquetas descriptivas
plt.title('Ingreso Mediano por Género en Argentina\n(Población Ocupada - EPH 1° Trimestre 2026)', fontsize=14, fontweight='bold')
plt.xlabel('Género', fontsize=12)
plt.ylabel('Ingreso Mediano (AR$)', fontsize=12)

# 5. Agregar el valor exacto arriba de cada barra
for p in ax.patches:
    ax.annotate(f'${p.get_height():,.0f}'.replace(',', '.'), 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='bottom', 
                fontsize=11, color='black', fontweight='bold',
                xytext=(0, 5), textcoords='offset points')

# 6. Guardar y mostrar
plt.tight_layout()
plt.savefig('brecha_salarial_genero.png', dpi=300)
print("\n--- Visualización ---")
print("Gráfico generado exitosamente y guardado como 'brecha_salarial_genero.png'")

plt.show()

# --- PASO 5: ANÁLISIS POR NIVEL EDUCATIVO ---

# 1. Filtrar solo los niveles educativos válidos (del 1 al 6 según el diccionario)
df_educacion = df_ocupados[df_ocupados['NIVEL_ED'].isin([1, 2, 3, 4, 5, 6])].copy()

# 2. Mapear los códigos numéricos a categorías de texto legibles
mapa_educacion = {
    1: '1. Primario Inc.',
    2: '2. Primario Comp.',
    3: '3. Secundario Inc.',
    4: '4. Secundario Comp.',
    5: '5. Superior Inc.',
    6: '6. Superior Comp.'
}
df_educacion['Nivel Educativo'] = df_educacion['NIVEL_ED'].map(mapa_educacion)

# 3. Agrupar cruzando Nivel Educativo y Sexo para calcular la mediana salarial
resumen_edu = df_educacion.groupby(['Nivel Educativo', 'Sexo'])['Ingreso_Total'].median().reset_index()

# 4. Imprimir la tabla en consola
print("\n--- INGRESO MEDIANO POR GÉNERO Y NIVEL EDUCATIVO ---")
print(resumen_edu.to_string(index=False))

# --- PASO 6: VISUALIZACIÓN DEL CRUCE EDUCATIVO ---

plt.figure(figsize=(12, 7))
sns.set_theme(style="whitegrid")

# 1. Crear el gráfico de barras agrupadas (hue='Sexo' divide las barras)
ax = sns.barplot(
    data=resumen_edu,
    x='Nivel Educativo',
    y='Ingreso_Total',
    hue='Sexo',
    palette="pastel"
)

# 2. Reutilizar la función de formato moneda para el eje Y
ax.yaxis.set_major_formatter(FuncFormatter(formato_moneda))

# 3. Títulos, etiquetas y rotación del eje X para mejor lectura
plt.title('Ingreso Mediano por Nivel Educativo y Género\n(Población Ocupada - EPH 1° Trim 2026)', fontsize=15, fontweight='bold')
plt.xlabel('Máximo Nivel Educativo Alcanzado', fontsize=12)
plt.ylabel('Ingreso Mediano (AR$)', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Género')

# 4. Guardar y mostrar
plt.tight_layout()
plt.savefig('brecha_educacion_genero.png', dpi=300)
print("\n--- Visualización ---")
print("Gráfico generado exitosamente y guardado como 'brecha_educacion_genero.png'")

plt.show()

# --- PASO 7: IMPACTO DE LA INFORMALIDAD LABORAL ---

# 1. Filtrar solo a los asalariados (Obrero o empleado -> CAT_OCUP = 3)
df_asalariados = df_ocupados[df_ocupados['CAT_OCUP'] == 3].copy()

# 2. Quedarnos solo con respuestas válidas sobre descuento jubilatorio (1 = Sí, 2 = No)
df_asalariados = df_asalariados[df_asalariados['PP07H'].isin([1, 2])]

# 3. Traducir los códigos a etiquetas claras
df_asalariados['Condición Laboral'] = df_asalariados['PP07H'].map({1: 'Formal (Registrado)', 2: 'Informal (No Registrado)'})

# 4. Agrupar por condición laboral y sexo para calcular la mediana
resumen_informalidad = df_asalariados.groupby(['Condición Laboral', 'Sexo'])['Ingreso_Total'].median().reset_index()

# 5. Mostrar en consola
print("\n--- INGRESO MEDIANO: FORMALIDAD VS INFORMALIDAD ---")
print(resumen_informalidad.to_string(index=False))

# --- PASO 8: VISUALIZACIÓN DE LA INFORMALIDAD ---

plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

# 1. Crear el gráfico de barras agrupadas
ax2 = sns.barplot(
    data=resumen_informalidad,
    x='Condición Laboral',
    y='Ingreso_Total',
    hue='Sexo',
    palette="pastel"
)

# 2. Formato del eje Y
ax2.yaxis.set_major_formatter(FuncFormatter(formato_moneda))

# 3. Títulos y etiquetas
plt.title('Ingreso Mediano por Condición Laboral y Género\n(Asalariados - EPH 1° Trim 2026)', fontsize=14, fontweight='bold')
plt.xlabel('Condición Laboral', fontsize=12)
plt.ylabel('Ingreso Mediano (AR$)', fontsize=12)
plt.legend(title='Género')

# 4. Agregar etiquetas de datos sobre las barras
for p in ax2.patches:
    ax2.annotate(f'${p.get_height():,.0f}'.replace(',', '.'), 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='bottom', 
                fontsize=11, color='black', fontweight='bold',
                xytext=(0, 5), textcoords='offset points')

# 5. Guardar y mostrar
plt.tight_layout()
plt.savefig('brecha_informalidad_genero.png', dpi=300)
print("\n--- Visualización ---")
print("Gráfico generado exitosamente y guardado como 'brecha_informalidad_genero.png'")

plt.show()