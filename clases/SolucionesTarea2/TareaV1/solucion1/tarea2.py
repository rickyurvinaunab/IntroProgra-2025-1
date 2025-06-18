from clases import Persona #Importar la clase para que el codigo se vea mas ordenado
from clases import Mascota #Importar la clase para que el codigo se vea mas ordenado
import matplotlib.pyplot as plt
uf=39204.61 #Variable global
lista_mascotas = [] #Variable global para luego modificarla e iterar en ella
lista_personas = [] #Variable global para luego modificarla e iterar en ella
def proceso_adopcion():
    """Este proceso permite que una persona pueda adoptar una mascota"""
    print("\n--Proceso de adopcion--\n")
    rut=input("Ingrese su rut : ")
    persona_encontrada = None #esta variable sirve para almacenar la persona encontrada

    for r in lista_personas:
        if r.rut == rut:
            persona_encontrada = r  #si la persona ingresa el mismo rut, esto valida que fue encontrado
            break

    if persona_encontrada is None:
        print("\nError, usted no esta registrado, porfavor primero marque la opcion 1 para registrarse\n")
        return
    print("Bienvenido", persona_encontrada.nombre, persona_encontrada.paterno) #si esta registrado le saldra este mensaje

    """Si no hay mascotas registradas le saldra un mensaje al usuario que no hay mascotas disponibles"""
    if not lista_mascotas:  
        print("No hay mascotas disponibles para adopción.")
        return
    """
    En el caso que si hayan mascotas disponibles le saldra un mensaje y se mostraran las mascotas disponibles para adoptar.
    El usuario podra adoptar la mascota a partir del ingreso del nombre de la mascota, si esta mascota no existe le saldra un mensaje
    """
    print("Mascotas disponibles:")
    for m in lista_mascotas:
        print("Nombre:", m.nombre_m, "\n Tipo:", m.tipo, "\n Color:", m.color)

    nombre_elegido = input("Ingrese el nombre de la mascota que desea adoptar: ")
    mascota_encontrada = None
    for m in lista_mascotas:
        if m.nombre_m == nombre_elegido:
            mascota_encontrada = m
            break

    if mascota_encontrada is None:
        print("Error, no existe una mascota con ese nombre, porfavor vuelva a intentarlo")
        return nombre_elegido

    persona_encontrada.mascotas.append(mascota_encontrada)  #para agregar la mascota a la persona
    lista_mascotas.remove(mascota_encontrada)  #para eliminar la mascota de la lista de mascotas disponibles
    print("Felicidades la adopcion ha sido completada")

def desvincular_mascota():
    print("\n--Desvincular mascota--\n")
    rut_ingresado = input("Ingrese su rut: ")
    persona_encontrada = None #esta variable sirve para almacenar la persona encontrada

    """for para buscar a la persona por su rut, mostrar error si no fue encontrado por su rut y mostrar error si esta persona no ha adoptado una mascota anteriormente"""
    for persona in lista_personas:
        if persona.rut == rut_ingresado:
            persona_encontrada = persona
            break

    if persona_encontrada == None:
        print("\nError, no existe una persona registrada con ese rut.\n")
        return #return para salir si no existe

    if len(persona_encontrada.mascotas) == 0: #si la persona no adopto antes le saldra mensaje error
        print("\nError, usted no ha adoptado anteriormente\n")
        return
    #for para mostrarle las mascotas que ha adoptado
    print("Mascotas adoptadas por", persona_encontrada.nombre, ":")
    for mascota in persona_encontrada.mascotas:
        print("Nombre:", mascota.nombre_m, "\n Tipo:", mascota.tipo)

    nombre_mascota_desvincular = input("\nIngrese el nombre de la mascota que desea desvincular: ")

    #Buscar la mascota en la lista persona
    mascota_a_desvincular= None #variable que servira para guardar la mascota a desvincular
    for mascota in persona_encontrada.mascotas:
        if mascota.nombre_m== nombre_mascota_desvincular:
            mascota_a_desvincular= mascota
            break

    if mascota_a_desvincular == None:
        print("\nError, no se encontro la mascota\n")
        return

    """Desvincular mascota quitar de la persona y volver a agregarla a la lista de mascotas disponibles
    """
    persona_encontrada.mascotas.remove(mascota_a_desvincular) #elimina a la mascota de su dueño
    mascota_a_desvincular.adoptante = ""  
    lista_mascotas.append(mascota_a_desvincular)  #añade a la mascota a la lista de mascotas disponibles

    print("La mascota ha sido desvinculada correctamente.\n")

def grafico_ingresos():
    """Este grafico mostrara los nombres de las personas ingresadas mostrando el ingreso que tienen en un grafico de barras
    """
    nombres = [] #lista vacia donde se guardaran los nombres
    ingresos = [] #lista vacia donde se guardaran los ingresos de la persona
    for p in lista_personas:
        nombres.append(p.nombre)
        ingresos.append(p.ingresos)
    plt.bar(nombres, ingresos, color="blue")
    plt.ylabel("Ingreso Mensual (CLP)")
    plt.xlabel("Personas")
    plt.title("Ingresos de Personas que adoptaron")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    return 
def menu():
   """
   Menu iterativo donde tenemos varias opciones que cumpliran ciertas funciones.
   Por lo que el usuario tendra que ingresar una opcion para seguir en el programa o salir de el
   ITERACION:
   print("---ADOPCION DE MASCOTAS---")
     print("1. Ingresar datos de las personas que adoptan")
     print("2. Ingresar datos de las mascotas adoptadas")
     print("3. Proceso de adopcion")
     print("4. Visualizar datos de las personas que adoptan")
     print("5. Visualizar datos de las mascotas adoptadas")
     print("6. Desvincular mascota")
     print("7. Visualizar gráfico del ingreso mensual en pesos de las personas que adoptaron mascotas")
     print("8. Salir del programa")
     ¿Que opcion deseas:?
     
     abajo estaran las funciones donde algunas de ellas necesitan parametros para ser funcionales
   
   """
   while True:
     print("---ADOPCION DE MASCOTAS---")
     print("1. Ingresar datos de las personas que adoptan")
     print("2. Ingresar datos de las mascotas adoptadas")
     print("3. Proceso de adopcion")
     print("4. Visualizar datos de las personas que adoptan")
     print("5. Visualizar datos de las mascotas adoptadas")
     print("6. Desvincular mascota")
     print("7. Visualizar gráfico del ingreso mensual en pesos de las personas que adoptaron mascotas")
     print("8. Salir del programa")
     opcion = input("¿Que opcion desea?: ")
     while opcion != "1"and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "6" and opcion !="7" and opcion != "8":
        print("Error") #Validacion del menu, en caso de que el usuario se equivoque de opcion
        opcion = (input("¿Que opcion desea?: ")) #Le volvemos a preguntar
     
     if opcion == "1":
            print("\n--INGRESO DATOS PARA ADOPCION--\n")
            rut=input("Ingrese su rut: ")
            nombre=input("Ingrese su primer nombre: ").capitalize()
            segundo =input("Ingrese su segundo nombre: ").capitalize()
            paterno=input("Ingrese su apellido paterno: ").capitalize()
            materno=input("Ingrese su apellido materno: ").capitalize()
            fono=(input("Ingrese su numero de telefono: "))
            email=input("Ingrese su email: ")
            direccion=input("Ingrese su direccion: ")
            ingresos=float(input("Ingrese su ingresos mensual en CLP: "))
            ingreso_uf = ingresos/uf #hamilton
       
            if ingreso_uf >= 15:
                persona=Persona(rut,nombre,segundo,paterno,materno,fono,email,direccion,ingresos)
                lista_personas.append(persona)
                print("\nFelicidades, usted esta apto para adoptar una mascota\n")
            elif ingreso_uf < 15:
                print("\nLo sentimos, usted no esta apto para adoptar\n")
           
     elif opcion =="2":
            print("\n--Ingreso de datos de mascota--\n")
            nombre=input("Ingrese el nombre de la mascota: ")
            tipo= input("Ingrese el tipo de mascota (gato/perro): ")
            while tipo != "gato" and tipo != "perro":#Puse and porque el bucle se me hizo infinito
                print("Error, tiene que ser gato o perro")
                tipo= input("Ingrese el tipo de mascota (gato/perro): ")
            color= input("Ingrese el color de la mascota:")
            peso= (input("Ingrese el peso de la mascota: "))
            fecha= input("Ingrese la fecha de nacimiento de la mascota: ")
            observacion=input("Ingrese una observacion de la mascota: ")
            adoptante = input("¿Quien esta adoptando esta mascota?: ")
            mascota=Mascota(nombre,tipo,color,peso,fecha,observacion,adoptante)
            lista_mascotas.append(mascota)
           
     elif opcion == "3":
        if (len(lista_mascotas)) == 0:
           print("Lo sentimos, no hay ninguna mascota registrada, vuelva a la opcion 2\n")
        else:
          proceso_adopcion()
     elif opcion == "4":
        if (len(lista_personas)) == 0:
           print("Lo sentimos, no hay ninguna persona registrada. Vuelva a la opcion 1\n")
        else:
           print("----Datos personas----")
           for i in lista_personas:
             print(i)
     elif opcion == "5":
        if (len(lista_mascotas)) == 0:
           print("Lo sentimos no hay ninguna mascota registrada, vuelva a la opcion 2\n")
        else:
          print("----Datos mascotas----")
          for x in lista_mascotas:
             print(x)
     elif opcion == "6":
            desvincular_mascota()  
     elif opcion == "7":
        grafico_ingresos()
     elif opcion == "8":
        print("Saliendo del programa")
        break  
menu()

