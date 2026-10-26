import pandas as pd

df = pd.read_excel("usu_individual_T126.xlsx")

# Mismos filtros que en el análisis: ocupados con ingreso positivo
df = df[(df["ESTADO"] == 1) & (df["P47T"] > 0)].copy()

df["Sexo"] = df["CH04"].map({1: "Varón", 2: "Mujer"})
df["Edad"] = df["CH06"].astype(int)
df["Ingreso_Total"] = df["P47T"].round().astype(int)

mapa_educacion = {
    1: "1. Primario Inc.",
    2: "2. Primario Comp.",
    3: "3. Secundario Inc.",
    4: "4. Secundario Comp.",
    5: "5. Superior Inc.",
    6: "6. Superior Comp.",
}
df["Nivel Educativo"] = df["NIVEL_ED"].map(mapa_educacion).fillna("Sin dato")

# Condición laboral: solo asalariados con respuesta válida
df["Condición Laboral"] = df["PP07H"].map(
    {1: "Formal (Registrado)", 2: "Informal (No Registrado)"}
)
df.loc[df["CAT_OCUP"] != 3, "Condición Laboral"] = None
df["Condición Laboral"] = df["Condición Laboral"].fillna("No asalariado / sin dato")

df["Grupo de edad"] = pd.cut(
    df["Edad"],
    bins=[0, 24, 34, 44, 54, 64, 120],
    labels=["Hasta 24", "25-34", "35-44", "45-54", "55-64", "65 y más"],
)

salida = df[["Sexo", "Edad", "Grupo de edad", "Nivel Educativo",
             "Condición Laboral", "Ingreso_Total"]]
salida.to_excel("eph_ocupados_powerbi.xlsx", index=False)

print(f"Filas exportadas: {len(salida)}  (deberían ser 15182)")
print(salida.head())