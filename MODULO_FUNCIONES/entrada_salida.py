from datetime import datetime
import sys
import os

sys.path.append("..")

from MODULO_DATOS.datos import *

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RUTA_JSON = os.path.join(project_root, "DB", "usuarios.json")

def registrar_entrada():
    usuario = cargar_datos(RUTA_JSON)
    documento = input("- Ingrese el documento: - ")
    print("")
    contador = 0
    for i in usuario["employees"]:
        if documento == i["num_document"] and not i["exit"]:
            contador += 1
            i["payout"] = False
            i["time_work"] += 1
            i["exit"] = True
            
            print(" - - Entrada Registrada con éxito - - ")
            return guardar_datos(usuario, RUTA_JSON)  
    if contador == 0:
        print(" - El documento no existe o ya ingresó a la empresa - ")
    
def registrar_salida():
    usuario = cargar_datos(RUTA_JSON)
    documento = input("- Ingrese el documento: - ")
    print("")
    contador = 0
    for i in usuario["employees"]:
        if documento == i["num_document"]:
            contador += 1
            i["time_work"] > 0
            i["exit"] = False
            
            print("- - Salida Registrada con éxito - -")
            return guardar_datos(usuario, RUTA_JSON)  
    if contador == 0:
        print(" - El documento no existe o ya salió de la empresa - ")
    


            

            # for i in usuario["employees"]:
            #     if(i["exit"] == False):
            #         print("YO")


             



# json salida:boolean 
# entrada: verificar doc, validar exit=false, payout:false, time_work +1 y si si el exit=true
# salida: verificar el doc, time_work>0 y exit:false