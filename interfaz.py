# interfaz.py

from logica import ver_tareas


def mostrar_menu():
    print("\n===== SISTEMA DE TAREAS =====")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")


def mostrar_tareas():
    tareas = ver_tareas()

    if len(tareas) == 0:
        print("No hay tareas registradas.")
        return

    print("\n--- Lista de tareas ---")
    for i, t in enumerate(tareas, start=1):
        estado = "✔ Completada" if t["completada"] else "✘ Pendiente"
        print(f"{i}. {t['descripcion']} - {estado}")


def pedir_numero(mensaje):
    try:
        return int(input(mensaje))
    except ValueError:
        print("❌ Debes ingresar un número válido")
        return None