from utils.archivos import cargar_datos, guardar_datos, cargar_contador, guardar_contador
from utils.validaciones import validar_texto, validar_numero, validar_booleano

ARCHIVO = "servicios.txt"
ARCHIVO_CONTADOR = "contador_servicios.txt"


def inicializar_servicios():
    servicios = cargar_datos(ARCHIVO)
    if servicios:
        return

    servicios = [
        {"id": 1, "nombre": "Corte Clásico", "precio": 5, "activo": True},
        {"id": 2, "nombre": "Fade", "precio": 7, "activo": True},
        {"id": 3, "nombre": "Barba", "precio": 4, "activo": True}
    ]

    guardar_datos(ARCHIVO, servicios)
    guardar_contador(ARCHIVO_CONTADOR, len(servicios))


def registrar_servicio():
    servicios = cargar_datos(ARCHIVO)
    contador = cargar_contador(ARCHIVO_CONTADOR) + 1

    nombre = validar_texto("Nombre del servicio: ")
    precio = validar_numero("Precio del servicio: ")
    activo = validar_booleano("¿Servicio activo?")

    servicio = {
        "id": contador,
        "nombre": nombre,
        "precio": precio,
        "activo": activo
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
        estado = "Activo" if s["activo"] else "Inactivo"
        print(f"ID: {s['id']} | Servicio: {s['nombre']} | Precio: ${s['precio']} | Estado: {estado}")
