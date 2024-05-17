def imprimir_mensaje_multiples_veces(mensaje, n):
    """
    Esta función recibe un mensaje y un número entero n,
    luego imprime el mensaje n veces.
    """
    for _ in range(n):
        print(mensaje)

# Pedir al usuario que ingrese el mensaje y el número de veces
mensaje = input("Ingrese el mensaje: ")
n = int(input("Ingrese el número de veces que desea imprimir el mensaje: "))

# Llamar a la función con los parámetros proporcionados por el usuario
imprimir_mensaje_multiples_veces(mensaje, n)