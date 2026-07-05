# logic.py
#CRUD
from data import tareas
from persistence import guardar_datos

def agregar_tarea(descripcion):
    tarea = {
        "descripcion": descripcion,
        "completada": False
    }
    tareas.append(tarea)
    guardar_datos()

def ver_tareas():
    return tareas


def completar_tarea(indice):
    tareas[indice]["completada"] = True
    guardar_datos()

def eliminar_tarea(indice):
    tarea = tareas.pop(indice)
    guardar_datos()
    return tarea