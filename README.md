# Contar nombres
def contar_nombres(lista, nombre):
    contador = 0
    for item in lista:
        if item == nombre:
            contador += 1
    return contador

# Ejemplo de uso
nombres = ["Juan", "María", "Pedro", "María", "María", "Ana", "María"]
nombre_buscar = "María"
repeticiones = contar_nombres(nombres, nombre_buscar)
print(f"El nombre '{nombre_buscar}' se repite {repeticiones} veces en la lista.")

