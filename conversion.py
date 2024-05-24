def conversion_longitud():
    print("Seleccione la conversión de longitud que desea realizar:")
    print("1. Millas a Kilómetros")
    print("2. Kilómetros a Millas")
    print("3. Pies a Metros")
    print("4. Metros a Pies")
    print("5. Yardas a Metros")
    print("6. Metros a Yardas")
    
    opcion = int(input("Ingrese el número de la opción: "))
    
    if opcion == 1:
        millas = float(input("Ingrese la cantidad en millas: "))
        km = millas * 1.609344
        print(f"{millas} millas son {km:.2f} kilómetros.")
    elif opcion == 2:
        km = float(input("Ingrese la cantidad en kilómetros: "))
        millas = km / 1.609344
        print(f"{km:.2f} kilómetros son {millas:.2f} millas.")
    elif opcion == 3:
        pies = float(input("Ingrese la cantidad en pies: "))
        metros = pies * 0.3048
        print(f"{pies} pies son {metros:.2f} metros.")
    elif opcion == 4:
        metros = float(input("Ingrese la cantidad en metros: "))
        pies = metros / 0.3048
        print(f"{metros:.2f} metros son {pies:.2f} pies.")
    elif opcion == 5:
        yardas = float(input("Ingrese la cantidad en yardas: "))
        metros = yardas * 0.9144
        print(f"{yardas} yardas son {metros:.2f} metros.")
    elif opcion == 6:
        metros = float(input("Ingrese la cantidad en metros: "))
        yardas = metros / 0.9144
        print(f"{metros:.2f} metros son {yardas:.2f} yardas.")
    else:
        print("Opción inválida. Intente de nuevo.")

def conversion_volumen():
    print("Seleccione la conversión de volumen que desea realizar:")
    print("1. Metros cúbicos a Pies cúbicos")
    print("2. Pies cúbicos a Metros cúbicos")
    
    opcion = int(input("Ingrese el número de la opción: "))
    
    if opcion == 1:
        m3 = float(input("Ingrese la cantidad en metros cúbicos: "))
        ft3 = m3 * 35.314667
        print(f"{m3:.2f} metros cúbicos son {ft3:.2f} pies cúbicos.")
    elif opcion == 2:
        ft3 = float(input("Ingrese la cantidad en pies cúbicos: "))
        m3 = ft3 / 35.314667
        print(f"{ft3:.2f} pies cúbicos son {m3:.2f} metros cúbicos.")
    else:
        print("Opción inválida. Intente de nuevo.")

def menu_principal():
    while True:
        print("Seleccione el tipo de conversión que desea realizar:")
        print("1. Conversión de longitud")
        print("2. Conversión de volumen")
        print("3. Salir")
        
        opcion = int(input("Ingrese el número de la opción: "))
        
        if opcion == 1:
            conversion_longitud()
        elif opcion == 2:
            conversion_volumen()
        elif opcion == 3:
            print("¡Adiós!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

menu_principal()