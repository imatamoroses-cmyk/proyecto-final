import os
import json


def cargar_datos(nombre_archivo):
    ruta = os.path.join("data", nombre_archivo)

    if not os.path.exists(ruta):
        return []

    with open(ruta, "r", encoding="utf-8") as archivo:
        contenido = archivo.read().strip()
        if contenido == "":
            return []
        return json.loads(contenido)


def guardar_datos(nombre_archivo, datos):
    ruta = os.path.join("data", nombre_archivo)

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def cargar_contador(nombre_archivo):
    ruta = os.path.join("data", nombre_archivo)

    if not os.path.exists(ruta):
        return 0

    with open(ruta, "r", encoding="utf-8") as archivo:
        contenido = archivo.read().strip()
        if contenido == "":
            return 0
        return int(contenido)


def guardar_contador(nombre_archivo, valor):
    ruta = os.path.join("data", nombre_archivo)

    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write(str(valor))

