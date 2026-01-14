from utils.archivos import cargar_datos, guardar_datos, cargar_contador, guardar_contador
from utils.validaciones import solo_letras, solo_numeros

ARCHIVO = "barberos.txt"
ARCHIVO_CONTADOR = "contador_barberos.txt"


def inicializar_barberos():
    barberos = cargar_datos(ARCHIVO)
    if barberos:
        return

    barberos = [
        {"id": 1, "nombre": "Pedro Lopez", "telefono": "0981112233", "especialidad": "Fade"},
        {"id": 2, "nombre": "Juan Mena", "telefono": "0992223344", "especialidad": "Barba"},
        {"id": 3, "nombre": "Luis Torres", "telefono": "0973334455", "especialidad": "Clasico"}
    ]

    guardar_datos(ARCHIVO, barberos)
    guardar_contador(ARCHIVO_CONTADOR, len(barberos))


def registrar_barbero():
    barberos = cargar_datos(ARCHIVO)
    contador = cargar_contador(ARCHIVO_CONTADOR) + 1

    # VALIDAR NOMBRE
    while True:
        nombre = input("Nombre del barbero: ").strip()
        if solo_letras(nombre):
            break
        print(" Error: el nombre solo debe contener letras.")

    # VALIDAR TELÉFONO
    while True:
        telefono = input("Teléfono del barbero: ").strip()
        if solo_numeros(telefono):
            break
        print(" Error: el teléfono solo debe contener números.")

    # VALIDAR ESPECIALIDAD
    while True:
        especialidad = input("Especialidad del barbero: ").strip()
        if solo_letras(especialidad):
            break
        print(" Error: la especialidad solo debe contener letras.")

    barbero = {
        "id": contador,
        "nombre": nombre,
        "telefono": telefono,
        "especialidad": especialidad
    }

    barberos.append(barbero)
    guardar_datos(ARCHIVO, barberos)
    guardar_contador(ARCHIVO_CONTADOR, contador)

    print(" Barbero registrado correctamente.")


def listar_barberos():
    barberos = cargar_datos(ARCHIVO)

    if not barberos:
        print("No hay barberos registrados.")
        return

    print("\nBARBEROS REGISTRADOS")
    for b in barberos:
        print(f"ID: {b['id']} | Nombre: {b['nombre']} | Teléfono: {b['telefono']} | Especialidad: {b['especialidad']}")
