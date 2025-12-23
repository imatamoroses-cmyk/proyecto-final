from datetime import datetime

def validar_texto(mensaje):
    """
    Solicita un texto por teclado.
    Repite hasta que el usuario ingrese solo letras y espacios.
    """
    while True:
        texto = input(mensaje).strip()
        if texto.replace(" ", "").isalpha():
            return texto
        else:
            print(" Error: Ingrese solo texto válido.")


def validar_numero(mensaje):
    """
    Solicita un número entero positivo.
    Repite hasta que el valor sea correcto.
    """
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit():
            return int(valor)
        else:
            print(" Error: Ingrese solo números.")


def validar_opcion(mensaje, opciones):
    """
    Valida opciones de menú.
    'opciones' debe ser una lista de strings válidos.
    """
    while True:
        opcion = input(mensaje).strip()
        if opcion in opciones:
            return opcion
        else:
            print(" Opción inválida. Intente de nuevo.")


def validar_fecha(mensaje):
    """
    Valida una fecha en formato DD/MM/YYYY.
    """
    while True:
        fecha = input(mensaje).strip()
        try:
            datetime.strptime(fecha, "%d/%m/%Y")
            return fecha
        except ValueError:
            print(" Fecha inválida. Use DD/MM/YYYY.")


def validar_booleano(mensaje):
    """
    Valida una respuesta tipo sí/no.
    Retorna True o False.
    """
    while True:
        valor = input(f"{mensaje} (s/n): ").lower().strip()
        if valor == "s":
            return True
        elif valor == "n":
            return False
        else:
            print(" Ingrese 's' para sí o 'n' para no.")
