from utils.archivos import cargar_datos, guardar_datos, cargar_contador, guardar_contador

ARCHIVO = "barberos.txt"
ARCHIVO_CONTADOR = "contador_barberos.txt"


def inicializar_barberos():
    barberos = cargar_datos(ARCHIVO)
    if barberos:
        return

    barberos = [
        {"id": 1, "nombre": "Pedro Cortez", "especialidad": "Fade", "activo": True},
        {"id": 2, "nombre": "Miguel Rojas", "especialidad": "Barba", "activo": True},
        {"id": 3, "nombre": "Andres Luna", "especialidad": "Diseños", "activo": True}
    ]

    guardar_datos(ARCHIVO, barberos)
    guardar_contador(ARCHIVO_CONTADOR, len(barberos))


def registrar_barbero():
    barberos = cargar_datos(ARCHIVO)
    contador = cargar_contador(ARCHIVO_CONTADOR) + 1

    nombre = input("Nombre del barbero: ").strip()
    especialidad = input("Especialidad: ").strip()
    activo = input("¿Activo? (s/n): ").lower() == "s"

    if not nombre or not especialidad:
        print("Datos inválidos.")
        return

    barbero = {
        "id": contador,
        "nombre": nombre,
        "especialidad": especialidad,
        "activo": activo
    }

    barberos.append(barbero)
    guardar_datos(ARCHIVO, barberos)
    guardar_contador(ARCHIVO_CONTADOR, contador)

    print("Barbero registrado correctamente.")


def listar_barberos():
    barberos = cargar_datos(ARCHIVO)

    if not barberos:
        print("No hay barberos registrados.")
        return

    print("\nBARBEROS REGISTRADOS")
    for b in barberos:
        estado = "Activo" if b["activo"] else "Inactivo"
        print(f"ID: {b['id']} | Nombre: {b['nombre']} | Especialidad: {b['especialidad']} | {estado}")
