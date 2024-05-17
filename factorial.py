# 1) Pedir un número y guardarlo en una variable
numero = int(input("Ingresa un número: "))
# 2) Inicializar otra variable con valor 1
resultado = 1
# 3) Elaborar un contador que inicie en 2 y termine en el número ingresado
for i in range(2, numero + 1):
resultado *= i
# Imprimir el resultado
print("El factorial de", numero, "es", resultado)
