import gastos

def menu():

    while True:

        print("\n--- CONTROL DE GASTOS HORMIGA ---")
        print("1. Registrar gasto")
        print("2. Ver gastos")
        print("3. Total de gastos")
        print("4. Promedio de gastos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gastos.registrar_gasto()

        elif opcion == "2":
            gastos.ver_gastos()

        elif opcion == "3":
            gastos.total_gastos()

        elif opcion == "4":
            gastos.promedio_gastos()

        elif opcion == "5":
            print("Saliendo del sistema")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()
