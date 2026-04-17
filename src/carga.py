import os
import pandas as pd

def cargar_gastos_hormiga(ruta_csv: str = None):
    """Carga el CSV de gastos hormiga y lo convierte en DataFrame."""
    if ruta_csv is None:
        ruta_csv = os.path.join(os.path.dirname(__file__), "..", "data", "raw", "gastos_hormiga.csv")
    try:
        df = pd.read_csv(ruta_csv)
        if df.empty:
            print("Advertencia: El DataFrame está vacío.")
        return df
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en {ruta_csv}")
        return None
    except Exception as e:
        print(f"Error al cargar CSV: {e}")
        return None