import flet as ft
import json

# Función para cargar los datos de personal desde un archivo JSON
def cargar_datos():
    try:
        with open('personal.json', 'r') as archivo:
            try:
                return json.load(archivo)
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []

# Función para guardar los datos de personal en un archivo JSON
def guardar_datos(datos):
    with open('personal.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)

# Función para mostrar la lista de personal
def mostrar_personal():
    datos = cargar_datos()
    lista_personal.controls.clear()
    for persona in datos:
        lista_personal.controls.append(
            ft.Row([
                ft.Text(persona['nombre']),
                ft.Text(persona['cargo']),
                ft.Text(persona['telefono']),
                ft.Text(persona['correo']),
                ft.Text(persona['edad']),
                ft.TextButton('Editar', on_click=lambda e, p=persona: editar_persona(e, p)),
                ft.TextButton('Eliminar', on_click=lambda e, p=persona: eliminar_persona(e, p))
            ])
        )
    page.update()

# Función para crear una nueva persona
def crear_persona(e):
    nombre = nombre_input.value
    cargo = cargo_input.value
    telefono = telefono_input.value
    correo = correo_input.value
    edad = edad_input.value
    if nombre and cargo and telefono and correo and edad:
        datos = cargar_datos()
        datos.append({'nombre': nombre, 'cargo': cargo, 'telefono': telefono, 'correo': correo, 'edad': edad})
        guardar_datos(datos)
        mostrar_personal()
        nombre_input.value = ''
        cargo_input.value = ''
        telefono_input.value = ''
        correo_input.value = ''
        edad_input.value = ''
        page.update()

# Función para editar una persona existente
def editar_persona(e, persona):
    nombre_input.value = persona['nombre']
    cargo_input.value = persona['cargo']
    telefono_input.value = persona['telefono']
    correo_input.value = persona['correo']
    edad_input.value = persona['edad']
    datos = cargar_datos()
    datos.remove(persona)
    guardar_datos(datos)
    mostrar_personal()

# Función para eliminar una persona
def eliminar_persona(e, persona):
    datos = cargar_datos()
    datos.remove(persona)
    guardar_datos(datos)
    mostrar_personal()

def main(p: ft.Page):
    global nombre_input, cargo_input, telefono_input, correo_input, edad_input, lista_personal, page
    page = p

    page.title = "Gestión de Personal"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    nombre_input = ft.TextField(label="Nombre")
    cargo_input = ft.TextField(label="Cargo")
    telefono_input = ft.TextField(label="Teléfono")
    correo_input = ft.TextField(label="Correo Electrónico")
    edad_input = ft.TextField(label="Edad")
    crear_boton = ft.ElevatedButton("Crear", on_click=crear_persona)

    lista_personal = ft.Column([], auto_scroll=True, expand=True, scroll=True, spacing=10)

    page.add(
        ft.Column([
            nombre_input,
            cargo_input,
            telefono_input,
            correo_input,
            edad_input,
            crear_boton,
            ft.Divider(),
            lista_personal
        ], spacing=20)
    )

    mostrar_personal()

ft.app(target=main)