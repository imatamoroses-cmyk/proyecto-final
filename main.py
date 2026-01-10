from services.clientes import (
    inicializar_clientes,
    registrar_cliente,
    listar_clientes
)

from services.barberos import (
    inicializar_barberos,
    registrar_barbero,
    listar_barberos
)

from services.servicios import (
    inicializar_servicios,
    registrar_servicio,
    listar_servicios
)

from services.citas import (
    inicializar_citas,
    registrar_cita,
    listar_citas
)

from services.pagos import (
    inicializar_pagos,
    registrar_pago,
    listar_pagos
)


# -------- SUBMENÚS --------

def menu_clientes():
    while True:
        print("\n--- Menú Cliente ---")
        print("1. Insertar cliente")
        print("2. Listar clientes")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            break
        else:
            print("Opción inválida")


def menu_barberos():
    while True:
        print("\n--- Menú Barbero ---")
        print("1. Insertar barbero")
        print("2. Listar barberos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_barbero()
        elif opcion == "2":
            listar_barberos()
        elif opcion == "3":
            break
        else:
            print("Opción inválida")


def menu_servicios():
    while True:
        print("\n--- Menú Servicio ---")
        print("1. Insertar servicio")
        print("2. Listar servicios")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_servicio()
        elif opcion == "2":
            listar_servicios()
        elif opcion == "3":
            break
        else:
            print("Opción inválida")


def menu_citas():
    while True:
        print("\n--- Menú Cita ---")
        print("1. Insertar cita")
        print("2. Listar citas")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_cita()
        elif opcion == "2":
            listar_citas()
        elif opcion == "3":
            break
        else:
            print("Opción inválida")


def menu_pagos():
    while True:
        print("\n--- Menú Pago ---")
        print("1. Insertar pago")
        print("2. Listar pagos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_pago()
        elif opcion == "2":
            listar_pagos()
        elif opcion == "3":
            break
        else:
            print("Opción inválida")


# -------- MENÚ PRINCIPAL --------

def menu():
    while True:
        print("\n===== BARBERÍA - SISTEMA EN CONSOLA =====")
        print("1. Cliente")
        print("2. Barbero")
        print("3. Servicio")
        print("4. Cita")
        print("5. Pago")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_barberos()
        elif opcion == "3":
            menu_servicios()
        elif opcion == "4":
            menu_citas()
        elif opcion == "5":
            menu_pagos()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


def main():
    # Inicializa datos
    inicializar_clientes()
    inicializar_barberos()
    inicializar_servicios()
    inicializar_citas()
    inicializar_pagos()

    # Muestra el menú principal
    menu()


# -------- EJECUCIÓN --------
main()

