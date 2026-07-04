# logica.py

from datos import tareas


def agregar_tarea(descripcion):
    tarea = {
        "descripcion": descripcion,
        "completada": False
    }
    tareas.append(tarea)


def ver_tareas():
    return tareas


def completar_tarea(indice):
    tareas[indice]["completada"] = True


def eliminar_tarea(indice):
    return tareas.pop(indice)