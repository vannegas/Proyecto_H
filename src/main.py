from carga import cargar_gastos_hormiga

def menu():

    df = cargar_gastos_hormiga()

    if df is None:
        
        print("Error: No se pudieron cargar los datos.")
        return

    while True:

        print("\n--- CONTROL DE GASTOS HORMIGA ---")
        print("1. Ver gastos")
        print("2. Total de gastos")
        print("3. Promedio de gastos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(df)

        elif opcion == "2":
            total = df["monto"].sum()
            print("Total gastado:", total)

        elif opcion == "3":
            promedio = df["monto"].mean()
            print("Promedio de gastos:", promedio)

        elif opcion == "4":
            print("Saliendo del sistema")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()