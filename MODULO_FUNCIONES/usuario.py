import sys
import os

sys.path.append("..")

from MODULO_DATOS.datos import *

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RUTA_JSON = os.path.join(project_root, "DB", "usuarios.json")

def agregar():
    usuario = cargar_datos(RUTA_JSON)
    usuario={}
    usuario["name"]=input("Ingrese el nombre: ")
    usuario["last_name"]=input("Ingrese el apellido: ")
    usuario["num_document"]=input("Ingrese el documento: ")
    usuario["birth_date"]=input("Ingrese el documento: ")
    usuario["phone"]=input("Ingrese el número de teléfono: ")
    usuario["correo"]=input("Ingrese el correo electrónico: ")
    try:
        usuario["edad"] = int(input("Ingrese la edad: "))
    except Exception:
        print("¡Valor ingresado no válido!")
        print("Se debe actualizar luego con la opción (3) Actualizar ususario")
        usuario["edad"] = 999
        exc = format_exc()
        hora = str(datetime.now())
        with open("excepciones.txt","a") as e:
            e.write(hora+"\n "+ exc+"\n ")
    try:
        usuario["estrato"] = int(input("Ingrese el estrato económico: "))
    except Exception:
        print("¡Valor ingresado no válido!")
        print("Se debe actualizar luego con la opción (3) Actualizar ususario")
        usuario["estrato"] = 999
        exc = format_exc()
        hora = str(datetime.now())
        with open("excepciones.txt","a") as e:
            e.write(hora+"\n "+ exc+"\n ")
    usuario["direccion"]=input("Ingrese la dirección: ")
    usuario["departamento"]=input("Ingrese el departamento: ")
    usuario["municipio"]=input("Ingrese el municipio: ")
    usuario["categoria"]="Cliente nuevo"
    usuario["productos"]=[]
    usuario["servicios"]=[]
    usuario["historial"]=[]
    
    datos["usuarios"].append(usuario)
    print("Usuario registrado con éxito!")
    return datos

def modificar():
    usuario = cargar_datos(RUTA_JSON);
    documentos =[]
    
    #documento = input("Ingrese el documento: ")
    
    for i in usuario["usuario"]["num_document"]:
        print(i)
        
modificar()

