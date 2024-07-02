import sys

sys.path.append("..")


from MODULO_FUNCIONES.usuario import *
from MODULO_FUNCIONES.entrada_salida import *
from MODULO_NOMINA.funciones import *

def menu():
    print("*************************")
    print("**Bienvenid@ a PayMatic**")
    print("*************************")
    while True:
        print("")
        print("1. Modulo Usuarios")
        print("2. Modulo de Nómina")
        print("3. Modulo de Entradas/Salidas")
        print("4. Cerrar Programa")
        print("")

        opcion = input("Selecciona una opcion: ")
        print("")

        if opcion == "1":
            menu_usuario()
        elif opcion == "2":
            menu_nómina()
        elif opcion == "3":
            menu_entrada_salida()
        elif opcion == "4":
            print("")
            print("Programa Finalizado.")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def menu_usuario():
    print("Módulo Usuarios")
    print("")
    while True:
        print("")
        print("1- Agregar usuario")
        print("2- Modificar usuario")
        print("3- Eliminar usuario")
        print("4- Listar usuarios")
        print("5- Regresar")
        print("")

        opcion = input("Selecciona una opcion: ")
        print("")

        if opcion == "1":
            agregar()
        elif opcion == "2":
            modificar()
        elif opcion == "3":
            eliminar()
        elif opcion == "4":
            leer()
        elif opcion == "5":
            print("")
            print("Regreseando...")
            menu()
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def menu_nómina():
    print("Módulo Nómina")
    print("")
    while True:
        print("")
        print("1- Informe")
        print("2- Pagar sueldo")
        print("3- Regresar")
        print("")

        opcion = input("Selecciona una opcion: ")
        print("")

        if opcion == "1":
            informe()
        elif opcion == "2":
            pagar()
        elif opcion == "3":
            print("")
            print("Regreseando...")
            menu()
            print("")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")

def menu_entrada_salida():
    print("-- Ingrese la opcion deseada: --")
    while True:
        print("")
        print("1. Para registrar ingreso")
        print("2. Para registrar salida")
        print("3. Para volver al menú anterior")
        print("")

        opcion = input("Selecciona una opcion: ")
        print("")

        if opcion == "1":
            registrar_entrada()
        elif opcion == "2":
            registrar_salida()
        elif opcion == "3":
            print("")
            print("")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")