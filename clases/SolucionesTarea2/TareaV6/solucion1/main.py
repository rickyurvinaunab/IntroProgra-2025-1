"""Codigo principal del programa de adopcion PATITAS 
    que gestiona el registro de personas, adopcion,
    la visualizacion de datos,incluyendo grafico de sueldos.
    Conteniendo 3 menus que seria el principal el de usuario y 
    el de administrador.
"""
from registrar_persona import ingresar_persona
from registrar_persona import Persona
from mascota import Mascota,ingresar_mascota
from mascota import mostrar_mascotas
from grafico import grafico_sueldos
from adoptar import adoptar_mascotas
personas=[]
mascotas=[]
def menu():
    """Muestra el menu principal y las 3 opciones"""
    print("Bienvenido a PATITAS")
    print("-----------------------------------------")
    print("1. Menu de administrador")
    print("2. Menu de Usuario")
    print("3. Salir")
def menu_principal():
    """Muestra el menu de usuario al haber elegido 2 en el menu principal"""
    print("Bienvenido al servicio de adopcion de mascotas")        
    print("-----------------------------------------")
    print("1. Registrar usuario")
    print("2. Adoptar mascotas")  
    print("3. Salir del programa")
def menu_admin():
    """Muestra el menu de administrador al haber elegido 1 en el menu principal"""
    print("Bienvenido al menu de administrador")
    print("-----------------------------------------")
    print("1. Poner mascotas en adopcion")
    print("2. Visualizar datos de las personas que adoptan")
    print("3. Visualizar datos de las mascotas adoptadas")
    print("4. Visualizar gráfico del ingreso mensual de las personas que adoptaron")
    print("5. Volver al menu principal")
while True:
    menu()
    opcion_main=input("A que menu deseas acceder: ")
    if opcion_main=="1":
        while True:
            menu_admin()
            opcion_admin= input("A que sistema deseas acceder: ")
            if opcion_admin=="1":
                print("Bienvenido al registro de mascotas para adopcion")
                mascota=ingresar_mascota()
                mascotas.append(mascota)
                print("Mascota registrada con exito")
            elif opcion_admin=="2":
                if len(personas)<=0:
                    print("No se puede visualizar ningun dato de una persona")
                else:
                    print("Visualizando datos de las personas")
                    for persona in personas:
                        print(persona)
                        print("----------------------")
            elif opcion_admin=="3":
                if len(personas)==0:
                    print("Aun no se han registrado personas")
                else:
                    mostrar_mascotas(mascotas)       
            elif opcion_admin=="4":
                if len(personas)<=0:
                    print("No podemos visualizar los sueldos, si no se han registrado personas")
                else:
                    print("Visualizando sueldos de las personas")
                    grafico=grafico_sueldos(personas)
                    print(grafico)               
            elif opcion_admin=="5":
                print("Volviendo al menu principal..")
                break
            else:
                print("ingresa una opcion valida")
                
    elif opcion_main=="2": 
        while True:
            menu_principal()  
            opcion=input("A que sistema deseas acceder: ")  
            if opcion=="1":
                print("Bienvenido al registro de personas que adoptan")
                persona=ingresar_persona()
                if persona is not None:
                    personas.append(persona)
                    print("¡¡Persona registrada con exito!!")
            elif opcion=="2":
                if len(personas)<=0:
                    print("Aun no se registran personas para adoptar")
                else:
                    print("Hora de adoptar una mascota")
                    adoptar_mascotas(personas,mascotas)              
            elif opcion=="3":
                print("Volviendo al menu...")
                break   
            else:
             print("Ingresa una opcion valida")         
    elif opcion_main=="3":
        print("Gracias por usar nuestro servicio...")
        print("Vuelva pronto...")
        break
    else:
        print("Esta opcion no es valida, seleccione otra opcion...")
