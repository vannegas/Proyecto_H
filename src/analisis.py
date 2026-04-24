import pandas as pd
from limpiar import cargar_datos, limpiar_nulos, limpiar_texto, limpiar_monto

# cargar datos
usuarios = cargar_datos("data/usuarios.csv")
gastos = cargar_datos("data/gastos_hormiga.csv")

# limpiar
usuarios = limpiar_nulos(usuarios)
gastos = limpiar_nulos(gastos)

usuarios = limpiar_texto(usuarios, ["nombre", "ciudad"])
gastos = limpiar_texto(gastos, ["categoria", "medio_pago"])

gastos = limpiar_monto(gastos, "monto")

# unir datos
df = pd.merge(gastos, usuarios, on="id_usuario")

# ------------------------------
# PREGUNTA 1
# ------------------------------
print("\n--- PREGUNTA 1 ---")
frecuencia = df["categoria"].value_counts()
print(frecuencia)

print("La categoría con más transacciones es:",
    frecuencia.idxmax())

# ------------------------------
# PREGUNTA 2
# ------------------------------
print("\n--- PREGUNTA 2 ---")

gastos_usuario = df.groupby("nombre")["monto"].sum()
print(gastos_usuario)

print("El usuario que más gastó fue:",
    gastos_usuario.idxmax())

# ------------------------------
# PREGUNTA 3
# ------------------------------
print("\n--- PREGUNTA 3 ---")

conteo_pago = df["medio_pago"].value_counts()
print(conteo_pago)

print("Total de transacciones:", len(df))