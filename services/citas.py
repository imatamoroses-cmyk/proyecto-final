from utils.archivos import cargar_datos, guardar_datos, cargar_contador, guardar_contador

ARCHIVO = "citas.txt"
ARCHIVO_CONTADOR = "contador_citas.txt"


def inicializar_citas():
    citas = cargar_datos(ARCHIVO)
    if citas:
        return

    citas = [
        {"id": 1, "cliente_id": 1, "barbero_id": 1, "servicio_id": 2, "fecha": "10/12/2025"},
        {"id": 2, "cliente_id": 2, "barbero_id": 2, "servicio_id": 1, "fecha": "11/12/2025"}
    ]

    guardar_datos(ARCHIVO, citas)
    guardar_contador(ARCHIVO_CONTADOR, len(citas))


def registrar_cita():
    citas = cargar_datos(ARCHIVO)
    contador = cargar_contador(ARCHIVO_CONTADOR) + 1

    cliente_id = input("ID del cliente: ").strip()
    barbero_id = input("ID del barbero: ").strip()
    servicio_id = input("ID del servicio: ").strip()
    fecha = input("Fecha (DD/MM/YYYY): ").strip()

    if not cliente_id.isdigit() or not barbero_id.isdigit() or not servicio_id.isdigit():
        print("Los IDs deben ser numéricos.")
        return

    if not fecha:
        print("Fecha inválida.")
        return

    cita = {
        "id": contador,
        "cliente_id": int(cliente_id),
        "barbero_id": int(barbero_id),
        "servicio_id": int(servicio_id),
        "fecha": fecha
    }

    citas.append(cita)
    guardar_datos(ARCHIVO, citas)
    guardar_contador(ARCHIVO_CONTADOR, contador)

    print("Cita registrada correctamente.")


def listar_citas():
    citas = cargar_datos(ARCHIVO)

    if not citas:
        print("No hay citas registradas.")
        return

    print("\nCITAS REGISTRADAS")
    for c in citas:
        print(
            f"ID: {c['id']} | Cliente: {c['cliente_id']} | "
            f"Barbero: {c['barbero_id']} | Servicio: {c['servicio_id']} | Fecha: {c['fecha']}"
        )
