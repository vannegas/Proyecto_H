import pandas as pd
from limpiar import cargar_datos, limpiar_nulos, limpiar_texto, limpiar_monto

# ------------------------------
# FUNCIONES DE ANÁLISIS
# ------------------------------

def pregunta_1_frecuencia(df):
    print("\n--- PREGUNTA 1 ---")
    frecuencia = df["categoria"].value_counts()
    print(frecuencia)
    print("La categoría con más transacciones es:",
        frecuencia.idxmax())
    return frecuencia

def pregunta_2_agregacion(df):
    print("\n--- PREGUNTA 2 ---")
    gastos_usuario = df.groupby("nombre")["monto"].sum().sort_values(ascending=False)
    print(gastos_usuario)
    print("El usuario que más gastó fue:",
        gastos_usuario.idxmax())
    return gastos_usuario

def pregunta_3_filtrado(df):
    print("\n--- PREGUNTA 3 ---")
    conteo_pago = df["medio_pago"].value_counts()
    print(conteo_pago)
    print("Total de transacciones:", len(df))
    return conteo_pago

# ------------------------------
# EJECUCIÓN PRINCIPAL
# ------------------------------

# cargar datos
usuarios = cargar_datos("data/raw/usuarios.csv")
gastos = cargar_datos("data/raw/gastos_hormiga.csv")

if usuarios is None or gastos is None:
    print("Error al cargar datos")
    exit()

# limpiar
usuarios = limpiar_nulos(usuarios)
gastos = limpiar_nulos(gastos)

usuarios = limpiar_texto(usuarios, ["nombre", "ciudad"])
gastos = limpiar_texto(gastos, ["categoria", "medio_pago"])

gastos = limpiar_monto(gastos, "monto")

# unir datos
df = pd.merge(gastos, usuarios, on="id_usuario")

print("\nVista previa de datos:")
print(df.head())

# ejecutar preguntas
pregunta_1_frecuencia(df)
pregunta_2_agregacion(df)
pregunta_3_filtrado(df)