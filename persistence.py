import json
from data import tareas

ARCHIVO = "tareas.json"


def guardar_datos():
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=4, ensure_ascii=False)


def cargar_datos():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            tareas.clear()
            tareas.extend(json.load(archivo))
    except FileNotFoundError:
        pass