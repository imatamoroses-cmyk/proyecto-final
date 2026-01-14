from utils.archivos import cargar_datos, guardar_datos, cargar_contador, guardar_contador
from utils.validaciones import solo_numeros

ARCHIVO = "citas.txt"
ARCHIVO_CONTADOR = "contador_citas.txt"


def inicializar_citas():
    citas = cargar_datos(ARCHIVO)
    if citas:
        return

    citas = [
        {"id": 1, "cliente": "Juan Perez", "barbero": "Miguel Torres", "fecha": "2025-01-10", "hora": "10:00"},
        {"id": 2, "cliente": "Carlos Mena", "barbero": "Luis Mora", "fecha": "2025-01-11", "hora": "11:30"}
    ]

    guardar_datos(ARCHIVO, citas)
    guardar_contador(ARCHIVO_CONTADOR, len(citas))


def registrar_cita():
    citas = cargar_datos(ARCHIVO)
    contador = cargar_contador(ARCHIVO_CONTADOR) + 1

    cliente = input("Nombre del cliente: ").strip()
    barbero = input("Nombre del barbero: ").strip()
    fecha = input("Fecha (YYYY-MM-DD): ").strip()
    hora = input("Hora (HH:MM): ").strip()

    if not cliente or not barbero or not fecha or not hora:
        print(" Error: todos los campos son obligatorios.")
        return

    cita = {
        "id": contador,
        "cliente": cliente,
        "barbero": barbero,
        "fecha": fecha,
        "hora": hora
    }

    citas.append(cita)
    guardar_datos(ARCHIVO, citas)
    guardar_contador(ARCHIVO_CONTADOR, contador)

    print(" Cita registrada correctamente.")


def listar_citas():
    citas = cargar_datos(ARCHIVO)

    if not citas:
        print("No hay citas registradas.")
        return

    print("\nCITAS REGISTRADAS")
    for c in citas:
        print(
            f"ID: {c['id']} | Cliente: {c['cliente']} | "
            f"Barbero: {c['barbero']} | Fecha: {c['fecha']} | Hora: {c['hora']}"
        )
