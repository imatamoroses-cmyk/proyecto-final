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


def menu():
    while True:
        print("\n===== BARBERÍA - SISTEMA EN CONSOLA =====")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Registrar barbero")
        print("4. Listar barberos")
        print("5. Registrar servicio")
        print("6. Listar servicios")
        print("7. Registrar cita")
        print("8. Listar citas")
        print("9. Registrar pago")
        print("10. Listar pagos")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            registrar_barbero()
        elif opcion == "4":
            listar_barberos()
        elif opcion == "5":
            registrar_servicio()
        elif opcion == "6":
            listar_servicios()
        elif opcion == "7":
            registrar_cita()
        elif opcion == "8":
            listar_citas()
        elif opcion == "9":
            registrar_pago()
        elif opcion == "10":
            listar_pagos()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


def main():
    # Inicializa datos de prueba SOLO si los archivos están vacíos
    inicializar_clientes()
    inicializar_barberos()
    inicializar_servicios()
    inicializar_citas()
    inicializar_pagos()

    # Muestra el menú
    menu()


# EJECUCIÓN DEL PROGRAMA
main()


