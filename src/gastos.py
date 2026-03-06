from datos import gastos

def registrar_gasto():
    nombre = input("Nombre del gasto: ")
    valor = float(input("Valor del gasto: "))

    gasto = {
        "nombre": nombre,
        "valor": valor
    }

    gastos.append(gasto)

    print("Gasto registrado correctamente")


def ver_gastos():
    if len(gastos) == 0:
        print("No hay gastos registrados")
        return

    for g in gastos:
        print(g["nombre"], "-", g["valor"])


def total_gastos():
    total = 0

    for g in gastos:
        total += g["valor"]

    print("Total gastado:", total)


def promedio_gastos():
    if len(gastos) == 0:
        print("No hay gastos")
        return

    total = 0

    for g in gastos:
        total += g["valor"]

    promedio = total / len(gastos)

    print("Promedio de gastos:", promedio)
