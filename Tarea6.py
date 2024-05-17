listadenombres=[]
def agregarnombre(nombre_a_agregar):
    listadenombres.append(nombre_a_agregar)

def consultarnombre(nombre_a_consultar):
    if nombre_a_consultar in listadenombres:
        return True
    else:
        return False

def eliminarnombre(nombre_a_eliminar):
    if nombre_a_eliminar in listadenombres:
        listadenombres.remove(nombre_a_eliminar)
        return True
    else:
        return False

def modificarnombre(nombre_a_modificar, nuevo_nombre):
    if nombre_a_modificar in listadenombres:
        posicion=listadenombres.index(nombre_a_modificar)
        listadenombres[posicion]=nuevo_nombre
        return True
    else:
        return False

def mostrar_lista():
    print(listadenombres)

def contar_nombres(listadenombres):
    nombre_a_contar = input("Ingresa el nombre a contar: ")
    frecuencia=listadenombres.count(nombre_a_contar)

def mostrar_menu():
    print("1. Agregar un nombre")
    print("2. Consultar un nombre")
    print("3. Eliminar un nombre")
    print("4. Modificar un nombre")
    print("5. Mostrar la lista")
    print("6. Contar nombre")
    print("7. Salir")
    opcion=int(input("Dame una opcion: "))
    return opcion

def main():
    # Programa principal
    while True:
        op=mostrar_menu()
        print(op)
        if op==1:
            nombre=input("Dame un nombre: ")
            agregarnombre(nombre)
        elif op==2:
            nombreabuscar=input("Dame un nombre a buscar: ")
            if consultarnombre(nombreabuscar):
                print("El nombre esta en la lista")
            else:
                print("El nombre no esta en la lista")
        elif op==3:
            nombreaborrar=input("Dame un nombre a borrar: ")
            if eliminarnombre(nombreaborrar):
                print("El nombre fue eliminado")
            else:
                print("El nombre no estaba en la lista")
        elif op==4:
            nombreamodificar=input("Dame un nombre a modificar: ")
            nuevonombre=input("Dame el nuevo nombre: ")
            if modificarnombre(nombreamodificar, nuevonombre):
                print("El nombre fue modificado")
            else:
                print("El nombre no estaba en la lista")
        elif op==5:
            mostrar_lista()
        elif op==6:
            nombreacontar=input("dame el nombre a contar: ")
            if contar_nombres(nombreacontar):
                print ("Nombre, nombreacontar, frecuencia, se repite, veces")
            else:
                print("El nombre no estaba en la lista") 
        elif op==8:

            break
        
        else:
            print("Opcion no valida")

def frecuencia():
    return frecuencia

if __name__=="__main__":
    main()
