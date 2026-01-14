from utils.archivos import cargar_datos, guardar_datos, cargar_contador, guardar_contador
from utils.validaciones import solo_numeros

ARCHIVO = "pagos.txt"
ARCHIVO_CONTADOR = "contador_pagos.txt"


def inicializar_pagos():
    pagos = cargar_datos(ARCHIVO)
    if pagos:
        return

    pagos = [
        {"id": 1, "metodo": "Efectivo", "monto": 10.00},
        {"id": 2, "metodo": "Transferencia", "monto": 15.00}
    ]

    guardar_datos(ARCHIVO, pagos)
    guardar_contador(ARCHIVO_CONTADOR, len(pagos))


def registrar_pago():
    pagos = cargar_datos(ARCHIVO)
    contador = cargar_contador(ARCHIVO_CONTADOR) + 1

    # MÉTODO DE PAGO
    metodo = input("Método de pago: ").strip()
    if not metodo:
        print(" Error: el método no puede estar vacío.")
        return

    # VALIDAR MONTO
    while True:
        monto = input("Monto del pago: ").strip()
        if solo_numeros(monto):
            monto = float(monto)
            break
        print(" Error: el monto debe ser numérico.")

    pago = {
        "id": contador,
        "metodo": metodo,
        "monto": monto
    }

    pagos.append(pago)
    guardar_datos(ARCHIVO, pagos)
    guardar_contador(ARCHIVO_CONTADOR, contador)

    print("Pago registrado correctamente.")


def listar_pagos():
    pagos = cargar_datos(ARCHIVO)

    if not pagos:
        print("No hay pagos registrados.")
        return

    print("\nPAGOS REGISTRADOS")
    for p in pagos:
        print(f"ID: {p['id']} | Método: {p['metodo']} | Monto: ${p['monto']}")
