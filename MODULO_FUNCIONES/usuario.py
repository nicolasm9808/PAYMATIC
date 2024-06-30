import sys
import os

sys.path.append("..")

from MODULO_DATOS.datos import *

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RUTA_JSON = os.path.join(project_root, "DB", "usuarios.json")

def agregar():
    usuario = cargar_datos(RUTA_JSON)

    nuevos_usu = {}
    print(" ")
    print(" AGREGAR USUARIOS ")
    print(" ")

    cantidad_usuarios = int(len(usuario["employees"]))
    estado = False
    BANDERA = False

    for i in range(0, cantidad_usuarios):
        cantidad_usuarios += 1

    nuevos_usu["id"] = int(cantidad_usuarios)

    documentos_registrados = []

    for i in usuario["employees"]:
        documentos_registrados.append(i["num_document"])
    
    
    while True:
        try:
            documento = input("Ingrese el documento: ")
            break  
        except ValueError:
            print("Por favor, ingrese un número válido para el documento.")  

    while True:
        if(documento in documentos_registrados):
            print(f"El documento {documento} ya está registrado.")
            break 
        else:     
            
            nuevos_usu["num_document"] = documento

            try:
                nombre = input("Ingrese el nombre: ")
                if not nombre:
                    print("El nombre no puede estar vacío")
                    nuevos_usu["name"] = "Usuario"
                else:
                    nuevos_usu["name"] = nombre
            except Exception:
                nombre_base = "Usuario"
                print("Error. Se asignará un nombre genérico.")
                nuevos_usu["name"] = nombre_base 

            try:
                apellido = input("Ingrese el apellido: ")
                if not apellido:
                    print("El apellido no puede estar vacío")
                    nuevos_usu["last_name"] = "Usuario"
                else:
                    nuevos_usu["last_name"] = apellido
            except Exception:
                apellido_base = "Usuario"
                print("Error. Se asignará un apellido genérico.")
                nuevos_usu["last_name"] = apellido_base     

            try:
                print("Ingrese la dirección:")
                direccion = input("(ej. Carrera 24 #12 - 65) ")

                if not direccion.replace(' ', '').replace('-', '').replace('#', '').replace('.', '').isalnum():
                    print("La dirección contiene caracteres no válidos (Se asignará una dirección genérica).")
                    nuevos_usu["address"] = "Dirección desconocida"
                else:
                    nuevos_usu["address"] = direccion
            except ValueError:
                direccion_base = "Dirección desconocida"
                print("Error. Se asignará una dirección genérica:", direccion_base)
                nuevos_usu["address"] = direccion_base

            try:
                cargo = input("Ingrese el cargo: ")
                if not cargo:
                    print("El cargo no puede estar vacío")
                    nuevos_usu["rol"] = "Cargo basico"
                else:
                    nuevos_usu["rol"] = cargo
            except Exception:
                cargo_base = "Cargo basico"
                print("Error. Se asignará un cargo genérico.")
                nuevos_usu["rol"] = cargo_base

            try:
                print("Por favor ingrese su fecha de nacimiento (ej. 01/10/1997): ")
                fecha_nacimiento = input()
                if len(fecha_nacimiento) != 10 or fecha_nacimiento[2] != '/' or fecha_nacimiento[5] != '/':
                    print("La fecha de nacimiento no cumple el formato (se asignará una fecha genérica.)")
                    nuevos_usu["birth_date"] = "01/01/2001"
                else:
                    nuevos_usu["birth_date"] = fecha_nacimiento
            except ValueError:
                fecha_nacimiento_base = "01/01/2001"
                print("La fecha de nacimiento ingresada no es válida (se asignará una fecha genérica.)")
                nuevos_usu["birth_date"] = fecha_nacimiento_base

            try:
                telefono = int(input("Ingrese el telefono: "))
                nuevos_usu["phone"] = telefono
            except ValueError:
                telefono_base = 0000000000
                print("Telefono mal escrito (se le asignara un telefono generico)")
                nuevos_usu["phone"] = telefono_base            

            try:
                print("Ingrese la fecha de afiliación (ej. 01/10/2020):")
                fecha_afiliacion = input()
                if len(fecha_afiliacion) != 10 or fecha_afiliacion[2] != '/' or fecha_afiliacion[5] != '/':
                    print("La fecha de afiliación no cumple el formato (se asignará una fecha genérica.)")
                    nuevos_usu["entry_date"] = "01/01/2024" 
                else:
                    nuevos_usu["entry_date"] = fecha_afiliacion
            except ValueError:
                fecha_afiliacion_base = "01/01/2024"
                print("Fecha de afiliacion ingresada no es válida, se asignará una fecha genérica.")
                nuevos_usu["entry_date"] =  fecha_afiliacion_base 

            nuevos_usu["time_work"] = 0

            try:
                salario = int(input("Ingrese el salario: "))
                nuevos_usu["daily_salary"] = salario
            except ValueError:
                salario_base = 0
                print("Salario mal escrito (se le asignara un salario generico)")
                nuevos_usu["daily_salary"] = salario_base 

            nuevos_usu["payout"] = estado

            nuevos_usu["removed"] = estado


            usuario["employees"].append(nuevos_usu)
            guardar_datos(usuario, RUTA_JSON)
            print("")
            print("Usuario Registrado")
            break

def modificar():
    usuario = cargar_datos(RUTA_JSON)
    
    documento = input("Ingrese el documento: ")
    print("")
    
    for i in usuario["employees"]:
        if(documento in i["num_document"]):
            print("")

            try:
                nombre = input("Ingrese el nuevo nombre: ")
                if not nombre:
                    print("El nombre no puede estar vacío (se asignara un nombre generico)")
                    i["name"] = "xxxxxxx"
                else:
                    i["name"] = nombre
            except Exception:
                nombre_base = "xxxxxxx"
                print("Nombre con mala ortografia (se asignara un nombre generico)")
                i["name"]= nombre_base

            try:
                apellido = input("Ingrese el nuevo apellido: ")
                if not apellido:
                    print("El apellido no puede estar vacío (se asignara un apellido generico)")
                    i["last_name"] = "xxxxxxx"
                else:
                    i["last_name"] = apellido
            except Exception:
                apellido_base = "xxxxxxx"
                print("Apellido con mala ortografia (se asignara un apellido generico)")
                i["last_name"]= apellido_base

            try:
                direccion = input("Ingrese la nueva dirección: ")
                if not direccion:
                    print("La dirección no puede estar vacío (se asignara una dirección generica)")
                    i["address"] = "xxxxxxx"
                else:
                    i["address"] = direccion
            except Exception:
                direccion_base = "xxxxxxx"
                print("Dirección con mala ortografia (se asignara una dirección generica)")
                i["address"]= direccion_base

            try:
                cargo = input("Ingrese el nuevo cargo: ")
                if not cargo:
                    print("El cargo no puede estar vacío (se asignara un cargo generico)")
                    i["rol"] = "xxxxxxx"
                else:
                    i["rol"] = cargo
            except Exception:
                cargo_base = "xxxxxxx"
                print("Cargo con mala ortografia (se asignara un cargo generico)")
                i["rol"]= cargo_base

            try:
                nacimiento = input("Ingrese la nueva fecha de nacimiento (ej. 01/30/2020): ")
                if len(nacimiento) != 10 or nacimiento[2] != '/' or nacimiento[5] != '/':
                    print("La fecha de nacimiento no cumple el formato (se asignará una fecha genérica.)")
                    i["birth_date"] = "01/01/2024"
                else:
                    i["birth_date"] = nacimiento
            except ValueError:
                fecha_nacimiento_base = "01/01/2024"
                print("Fecha de nacimiento incorrecta (se le asignara una fecha generica)")
                i["birth_date"] =  fecha_nacimiento_base

            try:
                telefono = int(input("Ingrese el telefono: "))
                i["phone"] = telefono
            except ValueError:
                telefono_base = 0000000000
                print("Telefono mal escrito (se le asignara un telefono generico)")
                i["phone"] = telefono_base 
            
            try:
                ingreso = input("Ingrese la nueva fecha de ingreso (ej. 01/30/2020): ")
                if len(ingreso) != 10 or ingreso[2] != '/' or ingreso[5] != '/':
                    print("La fecha de ingreso no cumple el formato (se asignará una fecha genérica.)")
                    i["entry_date"] = "01/01/2024"
                else:
                    i["entry_date"] = ingreso
            except ValueError:
                fecha_ingreso_base = "01/01/2024"
                print("Fecha de ingreso incorrecta (se le asignara una fecha generica)")
                i["entry_date"] =  fecha_ingreso_base

            try:
                salario = int(input("Ingrese el nuevo salario diario: "))
                i["daily_salary"] = salario
            except ValueError:
                salario_base = 000
                print("Salario mal escrito (se le asignara un salario generico)")
                i["daily_salary"] = salario_base 

            print("")
            print("Usuario Actualizado") 
            print("")
            return guardar_datos(usuario, RUTA_JSON)
        else:
            print(f"El usuario {documento} NO existe")
            print("")
        
def leer():
    usuario = cargar_datos(RUTA_JSON)
    contador_usuario = 0
    for i in usuario["employees"]:
        if(i["removed"] == False):
            contador_usuario += 1
            print("")
            print(f"Usuario No. {contador_usuario}")
            print("")
            for llave, valor in i.items():
                if(llave != "id" and llave != "removed"):
                    print(llave.capitalize(), "=", valor)
    
    if(contador_usuario == 0):
        print("No se han registrado usuarios")

def eliminar():
    usuario = cargar_datos(RUTA_JSON)

    contador = int(len(usuario["employees"]))
    documento = input("Ingrese el documento del usuario: ")
    print("")
    for i in usuario["employees"]:
        if(i["num_document"] == documento):
            estado = input("Ingrese 1 para eliminar y 2 de lo contrario: ")
            print("")
            if(estado == "1"):
                i["removed"] = True
                print("Usuario Eliminado")
                print("")
            elif(estado == "2"):
                i["removed"] = False
                print("Usuario No Eliminado")
                print("")
            else:
                print("Seleccione un estado correcto (ej. 1)")
                print("")
            
            return guardar_datos(usuario, RUTA_JSON)
        else:
            contador -= 1
    if(contador == 0):
        print("El usuario no existe")
