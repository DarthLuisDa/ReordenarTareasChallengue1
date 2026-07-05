# main.py
# controla el flujo
from logic import (
    agregar_tarea,
    completar_tarea,
    eliminar_tarea,
    ver_tareas
)

from interface import (
    mostrar_menu,
    mostrar_tareas,
    pedir_numero
)


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            desc = input("Escribe la tarea: ")
            agregar_tarea(desc)

        elif opcion == "2":
            mostrar_tareas()

        elif opcion == "3":
         mostrar_tareas()
         num = pedir_numero("Número de tarea: ")

         if num is not None:
           indice = num - 1

           if 0 <= indice < len(ver_tareas()):
             completar_tarea(indice)
             print("✅ Tarea completada correctamente.")
           else:
             print("❌ No existe una tarea con ese número.")
        
        elif opcion == "4":
         mostrar_tareas()
         num = pedir_numero("Número de tarea: ")

         if num is not None:
           indice = num - 1

           if 0 <= indice < len(ver_tareas()):
              tarea = eliminar_tarea(indice)
              print(f"🗑️ Tarea '{tarea['descripcion']}' eliminada correctamente.")
           else:
            print("❌ No existe una tarea con ese número.")


        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()


        #Cambiamos estas 2 partes
        # elif opcion == "3":
        #    mostrar_tareas()
        #    num = pedir_numero("Número de tarea: ")
        #    if num:
        #        try:
        #            completar_tarea(num - 1)
        #        except IndexError:
        #            print("❌ Índice inválido")
        #
        #elif opcion == "4":
        #    mostrar_tareas()
        #    num = pedir_numero("Número de tarea: ")
        #    if num:
        #        try:
        #            eliminar_tarea(num - 1)
        #       except IndexError:
        #            print("❌ Índice inválido")