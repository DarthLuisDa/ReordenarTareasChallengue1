# 📋 Sistema de Gestión de Tareas (To-Do List)

## 📖 Descripción

Este proyecto consiste en un sistema de gestión de tareas desarrollado en Python mediante una aplicación de consola. El objetivo principal fue refactorizar un script monolítico, separando las responsabilidades en distintos módulos para mejorar la organización, la legibilidad y el mantenimiento del código.

Como mejora adicional, se implementó persistencia de datos utilizando archivos JSON, permitiendo conservar las tareas incluso después de cerrar el programa.

---

## 🎯 Objetivo del Challenge

* Aplicar el principio de modularización.
* Separar la lógica del programa en módulos independientes.
* Implementar manejo básico de errores.
* Mejorar la estructura y mantenibilidad del código.
* Mantener el mismo comportamiento del programa original.

---

## 🚀 Funcionalidades

* ✅ Agregar tareas.
* 📋 Visualizar todas las tareas.
* ✔️ Marcar tareas como completadas.
* 🗑️ Eliminar tareas.
* 💾 Guardar automáticamente las tareas en un archivo JSON.
* 📂 Cargar las tareas almacenadas al iniciar el programa.
* ⚠️ Validación de entradas para evitar errores comunes.

---

## 📂 Estructura del proyecto

```text
todo_app/
│
├── main.py              # Controla el flujo principal del programa
├── datos.py             # Almacena la lista de tareas
├── logica.py            # Contiene la lógica del negocio (CRUD)
├── interfaz.py          # Maneja la interacción con el usuario
├── persistencia.py      # Guarda y carga la información en JSON
├── tareas.json          # Archivo de persistencia de datos
└── README.md
```

---

## 🧩 Descripción de los módulos

### `main.py`

Punto de entrada del programa. Coordina el funcionamiento general del sistema y administra el menú principal.

### `datos.py`

Contiene la estructura de datos principal donde se almacenan las tareas durante la ejecución del programa.

### `logica.py`

Implementa las operaciones principales del sistema:

* Agregar tareas.
* Listar tareas.
* Completar tareas.
* Eliminar tareas.

### `interfaz.py`

Gestiona toda la interacción con el usuario mediante el uso de `print()` e `input()`, manteniendo separada la lógica del negocio.

### `persistencia.py`

Se encarga de guardar y recuperar la información desde un archivo `JSON`, permitiendo conservar las tareas entre ejecuciones.

---

## 🛠️ Tecnologías utilizadas

* Python 3
* JSON (persistencia de datos)

---

## 📌 Mejoras implementadas

Durante la refactorización se realizaron las siguientes mejoras:

* Modularización del código.
* Separación de responsabilidades.
* Manejo básico de errores mediante validaciones y excepciones.
* Persistencia de datos utilizando archivos JSON.
* Código más limpio, reutilizable y fácil de mantener.

---

## 👨‍💻 Autor

**Luis Daniel Vargas Rodríguez**

Proyecto desarrollado como parte del **Skill Challenge 1 – Refactorización modular de un sistema en consola**.
