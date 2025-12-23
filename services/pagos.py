from utils.archivos import cargar_datos, guardar_datos, cargar_contador, guardar_contador

ARCHIVO = "pagos.txt"
ARCHIVO_CONTADOR = "contador_pagos.txt"


def inicializar_pagos():
    pagos = cargar_datos(ARCHIVO)
    if pagos:
        return

    pagos = [
        {"id": 1, "cita_id": 1, "monto": 7.00, "pagado": True},
        {"id": 2, "cita_id": 2, "monto": 5.00, "pagado": True}
    ]

    guardar_datos(ARCHIVO, pagos)
    guardar_contador(ARCHIVO_CONTADOR, len(pagos))


def registrar_pago():
    pagos = cargar_datos(ARCHIVO)
    contador = cargar_contador(ARCHIVO_CONTADOR) + 1

    cita_id = input("ID de la cita: ").strip()
    monto = input("Monto a pagar: ").strip()

    if not cita_id.isdigit():
        print("El ID de la cita debe ser numérico.")
        return

    try:
        monto = float(monto)
    except ValueError:
        print("El monto debe ser numérico.")
        return

    pago = {
        "id": contador,
        "cita_id": int(cita_id),
        "monto": monto,
        "pagado": True
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
        estado = "Pagado" if p["pagado"] else "Pendiente"
        print(f"ID: {p['id']} | Cita: {p['cita_id']} | Monto: ${p['monto']} | {estado}")

