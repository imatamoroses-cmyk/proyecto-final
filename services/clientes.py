from utils.archivos import (
    cargar_datos,
    guardar_datos,
    cargar_contador,
    guardar_contador
)

from utils.validaciones import (
    validar_texto,
    validar_telefono,
    validar_cedula
)

ARCHIVO = "clientes.txt"
ARCHIVO_CONTADOR = "contador_clientes.txt"


def inicializar_clientes():
    clientes = cargar_datos(ARCHIVO)
    if clientes:
        return

    clientes = [
        {
            "id": 1,
            "cedula": "0102030405",
            "nombre": "Juan Perez",
            "telefono": "0991234567"
        },
        {
            "id": 2,
            "cedula": "0607080910",
            "nombre": "Carlos Mena",
            "telefono": "0987654321"
        }
    ]

    guardar_datos(ARCHIVO, clientes)
    guardar_contador(ARCHIVO_CONTADOR, len(clientes))


def registrar_cliente():
    clientes = cargar_datos(ARCHIVO)
    contador = cargar_contador(ARCHIVO_CONTADOR) + 1

    print("\n=== REGISTRO DE CLIENTE ===")

    cedula = validar_cedula("Cédula del cliente: ")
    nombre = validar_texto("Nombre del cliente: ")
    telefono = validar_telefono("Teléfono del cliente: ")

    # Validar que la cédula no se repita
    for c in clientes:
        if c["cedula"] == cedula:
            print(" Error: Ya existe un cliente con esa cédula.")
            return

    cliente = {
        "id": contador,
        "cedula": cedula,
        "nombre": nombre,
        "telefono": telefono
    }

    clientes.append(cliente)
    guardar_datos(ARCHIVO, clientes)
    guardar_contador(ARCHIVO_CONTADOR, contador)

    print(" Cliente registrado correctamente.")


def listar_clientes():
    clientes = cargar_datos(ARCHIVO)

    if not clientes:
        print(" No hay clientes registrados.")
        return

    print("\n=== CLIENTES REGISTRADOS ===")
    for c in clientes:
        print(
            f"ID: {c['id']} | "
            f"Cédula: {c['cedula']} | "
            f"Nombre: {c['nombre']} | "
            f"Teléfono: {c['telefono']}"
        )
