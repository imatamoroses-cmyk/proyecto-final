from utils.archivos import cargar_datos, guardar_datos, cargar_contador, guardar_contador

ARCHIVO = "servicios.txt"
ARCHIVO_CONTADOR = "contador_servicios.txt"


def inicializar_servicios():
    servicios = cargar_datos(ARCHIVO)
    if servicios:
        return

    servicios = [
        {"id": 1, "nombre": "Corte clásico", "precio": 5.00},
        {"id": 2, "nombre": "Fade", "precio": 7.00},
        {"id": 3, "nombre": "Corte + Barba", "precio": 10.00}
    ]

    guardar_datos(ARCHIVO, servicios)
    guardar_contador(ARCHIVO_CONTADOR, len(servicios))


def registrar_servicio():
    servicios = cargar_datos(ARCHIVO)
    contador = cargar_contador(ARCHIVO_CONTADOR) + 1

    nombre = input("Nombre del servicio: ").strip()
    precio = input("Precio del servicio: ").strip()

    if not nombre or not precio:
        print("Datos inválidos.")
        return

    try:
        precio = float(precio)
    except ValueError:
        print("El precio debe ser numérico.")
        return

    servicio = {
        "id": contador,
        "nombre": nombre,
        "precio": precio
    }

    servicios.append(servicio)
    guardar_datos(ARCHIVO, servicios)
    guardar_contador(ARCHIVO_CONTADOR, contador)

    print("Servicio registrado correctamente.")


def listar_servicios():
    servicios = cargar_datos(ARCHIVO)

    if not servicios:
        print("No hay servicios registrados.")
        return

    print("\nSERVICIOS REGISTRADOS")
    for s in servicios:
        print(f"ID: {s['id']} | {s['nombre']} | Precio: ${s['precio']}")
