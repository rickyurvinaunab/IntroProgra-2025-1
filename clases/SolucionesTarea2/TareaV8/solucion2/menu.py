from clase_empresa import Empresa
from clase_arrendatarios import Arrendatario
import matplotlib.pyplot as plt
# Listas globales
empresas = []
personas = []
def menu():
    """
    Esta funcion muestra el menu principal.
    """   
    while True:
        print("Bienvenido a la gestión de arriendos")
        print("---------------------------------------")
        print("1. Ingresar datos de las empresas arrendadoras")
        print("2. Ingresar datos de las personas arrendatarias")
        print("3. Generar Arriendo")
        print("4. Desvincular arriendo")
        print("5. Visualizar datos de las empresas arrendadoras")
        print("6. Visualizar datos de las personas arrendatarias")
        print("7. Visualizar gráfico del monto a pagar de las personas arrendatarias")
        print("8. Salir del programa")

        opcion=input("A que sistema deseas acceder: ") 
        if opcion=="1":
            print("Opcion 1: Ingresar datos de las empresas arrendadoras")
            rut_empresa = input("Ingresa el rut de la empresa: ")
            nombre_empresa = input("Ingresa el nombre de la empresa: ")
            phono_empresa = input("Ingresa el phono de la empresa: ")
            email_empresa = input("Ingresa el email de la empresa: ")
            direccion = input("Ingresa la direccion de la empresa: ")
            precio = float(input("Ingresa el precio de arrendamiento: "))
            empresa = Empresa(nombre_empresa, rut_empresa, phono_empresa, email_empresa, direccion, precio)
            empresas.append(empresa)
            print("Se registro con exito")
       
        elif opcion=="2":
            print("Opcion 2: Ingresar datos de las personas arrendatarias")
            rut_arrendador = input("Ingresa el rut del arrendatario: ")
            nombre1 = input("Ingresa el primer nombre del arrendatario: ")
            nombre2 = input("Ingresa el segundo nombre del arrendatario : ")
            apellidop = input("Ingresa el apellido paterno del arrendatario: ")
            apellidoa = input("Ingresa el apellido materno del arrendatario: ")
            phono = input("Ingresa el phono del arrendatario: ")
            email = input("Ingresa el email del arrendatario : ")
            nacimiento = input("Ingresa la fecha de nacimiento del arrendatario: ")
            ingreso = float(input("Ingresa los ingresos mensuales del arrendatario: "))
            arriendo = float(input("Ingresa el monto a pagar (UF): "))
            if 20 <= arriendo <= 25:
                persona = Arrendatario(rut_arrendador, nombre1, nombre2, apellidop, apellidoa, phono, email, nacimiento, ingreso, arriendo)
                personas.append(persona)
                print("Se registro con exito")
            else:
                print("El monto a pagar debe estar entre 20 y 25 UF")
        
        elif opcion=="3":
            print("Opcion 3: Generar arriendo")
            buscar_rut = input("Ingresa el rut del arrendatario: ")
            encontrado = False
            for persona in personas:
                if persona.rut_arrendador == buscar_rut:
                    encontrado = True
                    print("Empresas disponibles: ")
                    for empresa in empresas:
                        print("Nombre: "+ empresa.nombre_empresa +"- Rut: "+empresa.rut_empresa)
                    rut_empresa = input("Ingresa el rut de la empresa donde desea arrendar: ")
                    empresa_encontrada = False
                    for empresa in empresas:
                        if empresa.rut_empresa == rut_empresa:
                            persona.generar_arriendo(empresa)
                            print("La arriendo fue vinculado con: "+ empresa.nombre_empresa)
                            empresa_encontrada = True 
                            break
                    if empresa_encontrada == False:
                        print("No se encontro ninguna empresa")
                    break
            if encontrado == False:
                print("No se encontro un arrendatario con ese rut")
    
        elif opcion=="4":
            print("Opcion 4: Desvincular arriendo")
            buscar_rut = input("Ingresa el rut del arrendatario: ")
            for persona in personas:
                if persona.rut_arrendador == buscar_rut:
                    if len(persona.empresas) == 0: 
                        print("No tiene empresas vinculadas")
                    else:
                        print("Empresas vinculadas")
                        for empresa in persona.empresas:
                            print("Nombre: "+ empresa.nombre_empresa +"- Rut: "+empresa.rut_empresa)
                        rut_empresa = input("Ingresa el rut de la empresa donde desea desvincular: ")
                        for empresa in persona.empresas:
                            if empresa.rut_empresa == rut_empresa:
                                persona.desvincular_arriendo(empresa)
                                break
                        else:
                            print("No se encontro ninguna empresa")
                    break
            else:
                print("No se encontro un arrendatario con ese rut") 
         
        elif opcion=="5":
            print("Opcion 5: Visualizar datos de las empresas arrendadoras")
            if len(empresas) == 0:  
                print("No hay empresas registradas")
            else:
                for empresa in empresas:
                    print("---------------------------------------")
                    print("Nombre de la empresa: "+ empresa.nombre_empresa)
                    print("Rut: "+ empresa.rut_empresa)
                    print("Phono: "+ empresa.phono_empresa)
                    print("Email: "+ empresa.email_empresa)
                    print("Direccion: "+ empresa.direccion)
                    print("Arrendatarios vinculados: ")
                    if len(empresa.arrendatarios) == 0:
                        print("No hay arrendatarios vinculados")
                    else:
                        for arrendatario in empresa.arrendatarios:
                            print("-"+ arrendatario.nombre1 + " " + arrendatario.apellidop +" "+ "(Rut: "+ arrendatario.rut_arrendador+ ")")
    
        elif opcion=="6":
            print("Opcion 6: Visualizar datos de las personas arrendatarias")
            if len(personas) == 0:  
                print("No hay personas registradas")
            else:
                for persona in personas:
                    print("---------------------------------------")
                    print("Nombre completo: "+ persona.nombre1 + persona.nombre2 + persona.apellidop + persona.apellidoa)
                    print("Rut: "+ persona.rut_arrendador)
                    print("Phono: "+ persona.phono)
                    print("Email: "+ persona.email)
                    print("Fecha de nacimiento: "+ persona.nacimiento)
                    print("ingreso mensual: "+ str(persona.ingreso))
                    print("Monto de arriendo: "+ str(persona.arriendo) +"UF")
                    print("Empresas vinculadas: ")
                    if len(persona.empresas) == 0:
                        print("No esta vinculado a ninguna empresa")
                    else:
                        for empresa in persona.empresas:
                            print("-"+ empresa.nombre_empresa +" "+ "(Rut: "+ empresa.rut_empresa+ ")")

        elif opcion=="7":
            print("Opcion 7: Visualizar gráfico del monto a pagar de las personas arrendatarias")
            if len(personas) == 0:
                print("No hay personas registradas")
            else:
                nombres = [p.nombre1 + " " + p.apellidop for p in personas]
                montos = [p.arriendo for p in personas]
                plt.bar(nombres, montos, color = "blue")
                plt.title("Monto de arriendo (UF)")
                plt.xlabel("Arrendatarios")
                plt.ylabel("Monto (UF)")
                plt.show()

        elif opcion=="8":
            print("Saliendo del programa...")
            break 
        else:
            print("Ingresa una opcion valida")

menu()
