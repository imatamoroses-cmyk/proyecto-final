from utils.archivos import cargar_datos, guardar_datos, cargar_contador, guardar_contador

ARCHIVO = "clientes.txt"
ARCHIVO_CONTADOR = "contador_clientes.txt"


def inicializar_clientes():
    clientes = cargar_datos(ARCHIVO)
    if clientes:
        return

    clientes = [
        {"id": 1, "nombre": "Juan Perez", "telefono": "0991234567"},
        {"id": 2, "nombre": "Carlos Mena", "telefono": "0987654321"},
        {"id": 3, "nombre": "Luis Andrade", "telefono": "0971122334"}
    ]

    guardar_datos(ARCHIVO, clientes)
    guardar_contador(ARCHIVO_CONTADOR, len(clientes))


def registrar_cliente():
    clientes = cargar_datos(ARCHIVO)
    contador = cargar_contador(ARCHIVO_CONTADOR) + 1

    nombre = input("Nombre del cliente: ").strip()
    telefono = input("Teléfono del cliente: ").strip()

    if not nombre or not telefono:
        print("Datos inválidos.")
        return

    cliente = {
        "id": contador,
        "nombre": nombre,
        "telefono": telefono
    }

    clientes.append(cliente)
    guardar_datos(ARCHIVO, clientes)
    guardar_contador(ARCHIVO_CONTADOR, contador)

    print("Cliente registrado correctamente.")


def listar_clientes():
    clientes = cargar_datos(ARCHIVO)

    if not clientes:
        print("No hay clientes registrados.")
        return

    print("\nCLIENTES REGISTRADOS")
    for c in clientes:
        print(f"ID: {c['id']} | Nombre: {c['nombre']} | Teléfono: {c['telefono']}")
