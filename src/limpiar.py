import pandas as pd

# cargar datos
def cargar_datos(ruta):
    try:
        df = pd.read_csv(ruta)
        return df
    except:
        print("Error al cargar archivo")
        return None

# eliminar nulos
def limpiar_nulos(df):
    df = df.dropna()
    return df

# texto a minusculas y sin espacios
def limpiar_texto(df, columnas):
    for col in columnas:
        if col in df.columns:
            df[col] = df[col].str.lower().str.strip()
    return df

# limpiar moneda
def limpiar_monto(df, columna):
    if columna in df.columns:
        try:
            df[columna] = df[columna].astype(float)
        except:
            # Si hay strings, limpiar
            df[columna] = df[columna].str.replace("$", "").str.replace(",", "").astype(float)
    return df