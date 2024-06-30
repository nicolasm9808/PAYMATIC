import sys
import os
from datetime import date

sys.path.append("..")

from MODULO_DATOS.datos import *

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RUTA_JSON = os.path.join(project_root, "DB", "usuarios.json")
RUTA_TXT = os.path.join(project_root, "DB", "pagos.txt")
FECHA_HOY = date.today()

def informe():
    usuario = cargar_datos(RUTA_JSON)

    documento = input("Ingrese el documento del empleado: ")

    for i in usuario["employees"]:
        if(documento == i["num_document"]):

            nombre = i["name"]
            apellido = i["last_name"]
            direccion = i["address"]
            afiliacion = i["entry_date"]
            telefono = i["phone"]
            dias = i["time_work"]
            pago = i["payout"]

            print("")
            print("----------------------------------------")
            print("          INFORME DE EMPLEADO           ")
            print("----------------------------------------")
            print("")
            print(f"El empleado {nombre} {apellido} identificado")
            print(f"con el número de cedula {documento} ubicado")
            print(f"en la dirección {direccion} ")
            print(f"Bucaramanga, con número de celular {telefono}")
            print(f"ingresó a la empresa el dia {afiliacion}")
            
            if(pago or dias == 0):
                print("y ha cumplido sus funciones durante varios dias")
                print("en dichos dias se recalca su compromiso")
                print("y responsabilidad con la empresa COHOSAN")
                print("")
                print("Dirigido a quien interese")
                print("Director de RRHH")
                print("----------------------------------------")
                dato= f"El empleado {nombre} {apellido} identificado \n con el número de cedula {documento} ubicado \n en la dirección {direccion} \n Bucaramanga, con número de celular {telefono} \n ingresó a la empresa el dia {afiliacion} \n y ha cumplido sus funciones durante varios dias \n en dichos dias se recalca su compromiso \n y responsabilidad con la empresa COHOSAN \n  \n Dirigido a quien interese \n Director de RRHH \n \n"
            else:
                print("y ha cumplido sus funciones con un total de")
                print(f"{dias} dias, se recalca su compromiso")
                print("y responsabilidad con la empresa COHOSAN")
                print("")
                print("Dirigido a quien interese")
                print("Director de RRHH")
                print("----------------------------------------")
                dato= f"El empleado {nombre} {apellido} identificado \n con el número de cedula {documento} ubicado \n en la dirección {direccion} \n Bucaramanga, con número de celular {telefono} \n ingresó a la empresa el dia {afiliacion} \n y ha cumplido sus funciones con un total de \n {dias} dias, se recalca su compromiso \n y responsabilidad con la empresa COHOSAN \n  \n Dirigido a quien interese \n Director de RRHH \n \n"


            documento_ruta = str(documento)
            ruta = f"{documento_ruta}.txt"
            RUTA_TXT_EMPLEADO = os.path.join(project_root, "DB", ruta)

            escribir_txt(dato, RUTA_TXT_EMPLEADO)

def pagar():
    usuario = cargar_datos(RUTA_JSON)

    documento = input("Ingrese el documento del empleado: ")

    for i in usuario["employees"]:
        if(documento == i["num_document"]):

            nombre = i["name"]
            apellido = i["last_name"]
            dias = i["time_work"]
            salario = i["daily_salary"]

            print("")
            print("----------------------------------------")
            print("            RECIBO DE PAGO              ")
            print("----------------------------------------")
            print("")
            print(f"Nombre del empleado: {nombre} {apellido}")
            print(f"Identificación: {documento}")
            print("")
            print("----------------------------------------")
            
            total = dias * salario

            if(total>0):
                print(f"Días trabajados: {dias}")
                print(f"Pago diario: {salario}")
                print("----------------------------------------")
                print(f"TOTAL A PAGAR: ${total}")
                print("----------------------------------------")
                print("")
                print("Gracias por su trabajo!")
                print("----------------------------------------")
                i["time_work"] = 0
                i["payout"] = True
                dato = f"Dia de pago: {FECHA_HOY} | Empleado: {nombre} {apellido} | Total pagado: {total}" 
                escribir_txt(dato, RUTA_TXT)
                return guardar_datos(usuario, RUTA_JSON)
            else:
                print("El empleado no ha trabajado")

            print("")
            break
