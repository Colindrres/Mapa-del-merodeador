# Programa para recopilar información de estudiantes y no estudiantes
es_estudiante = input("¿Es usted estudiante? (S/N) ").upper()

if es_estudiante == "S":
    nombre = input("Ingrese su nombre: ")
    carne = input("Ingrese su número de carne: ")
    correo = input("Ingrese su correo electrónico: ")

    print("---------------INFORMACIÓN DEL ESTUDIANTE---------------")
    print("Nombre:", nombre)
    print("Carne:", carne)
    print("Correo electrónico:", correo)

else:
    nombre = input("Ingrese su nombre: ")
    dpi = input("Ingrese su número de DPI: ")

    print("---------------INFORMACIÓN DE LA PERSONA---------------")
    print("Nombre:", nombre)
    print("DPI:", dpi)
