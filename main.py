gastos = []

def registrar_gasto():
    nombre = input("Nombre del gasto: ")
    categoria = input("Categoria: ")
    valor = float(input("Valor del gasto: "))

    gasto = {
        "nombre": nombre,
        "categoria": categoria,
        "valor": valor
    }

    gastos.append(gasto)
    print("Gasto registrado correctamente")

def ver_gastos():
    print("\nLista de gastos:")
    for gasto in gastos:
        print(gasto)

def ver_total():
    total = 0
    for gasto in gastos:
        total += gasto["valor"]

    print("Total gastado:", total)

while True:

    print("\nMENU")
    print("1. Registrar gasto")
    print("2. Ver gastos")
    print("3. Ver total gastado")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_gasto()

    elif opcion == "2":
        ver_gastos()

    elif opcion == "3":
        ver_total()

    elif opcion == "4":
        print("Saliendo del sistema")
        break

    else:
        print("Opción inválida")