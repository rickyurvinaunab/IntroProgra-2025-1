# Problema a Resolver
# Contexto: Sistema de Gestión de Viajes Turísticos
# Una agencia de viajes desea llevar un registro digital de las personas que contratan viajes turísticos. Cada persona puede contratar uno o varios viajes. Se desea implementar un sistema que permita registrar los datos de las personas y los viajes, calcular estadísticas y visualizar información relevante para la toma de decisiones.
# Clases:
# Clase Persona
# -	rut
# -	nombre
# -	lista_viajes 
# Clase Viaje
# •	destino (str)
# •	duración en días (int)
# •	costo (int)
# •	temporada (str: alta, media, baja)
# El programa debe tener un menú que permita al usuario seleccionar una de las siguientes opciones:
# 1.	Crear lista de viajes
# 2.	Registrar nueva persona y su(s) viaje(s) contratado(s)
# 3.	Visualizar todas las personas y sus viajes
# 4.	Visualizar el destino más contratado y su ganancia total
# 5.	Visualizar la persona que más ha contratado viajes.
# 6.	Visualizar cual es el promedio de duración de los viajes en días.
# 7.	Visualizar promedio de gasto total por persona según temporada
# 8.	Mostrar gráfico de total gastado por cada persona
# 9.	Salir del programa
# Notas adicionales:
# - Validar que el costo esté entre $100.000 y $2.000.000.
# - Para el gráfico, mostrar el total gastado por cada persona (nombre en eje X, gasto en eje Y).
# - Los datos del destino más contratado deben guardarse y actualizarse en un archivo llamado destino_mas_contratado.txt.

class Persona:

    def __init__(self, rut, nombre):
        self.rut = rut
        self.nombre = nombre
        self.lista_viajes = []
    
    def __str__(self):
        return self.nombre+" con rut: "+self.rut+" tiene: " +str(len(self.lista_viajes)) +" viajes"

    def agregar_viaje(self, viaje):
        self.lista_viajes.append(viaje)
    
    def visualizar_viajes(self):
        print("Los viajes de la persona "+self.nombre+" son: ")
        for viaje in self.lista_viajes:
            print(viaje)
    
class Viaje:

    def __init__(self,destino, duracion,costo, temporada):
        self.destino = destino
        self.duracion = duracion
        self.costo = costo
        self.temporada = temporada
    
    def __str__(self):
        return f"El viaje con destino {self.destino} tiene una duracion de {self.duracion} y un costo de {self.costo} y su temporada es: {self.temporada}"

lista_personas = []
lista_viajes = []
viaje = Viaje("Ecuador",10,150000, "alta")
viaj2 = Viaje("Colombia",15,225000, "media")
viaj3 = Viaje("Ecuador",12,300000, "alta")
lista_viajes.append(viaje)
lista_viajes.append(viaj2)
lista_viajes.append(viaj3)

def ver_destino_mas_contratado(lista_personas, lista_viajes):
    # 1. Crear la lista de nombres de viajes
    # 2. Contar cuantas veces ese viaje se realizo
    # Para contar recorri la lista de nombre de viajes
    # Por cada uno de estos nombres recorri la lista de personas
    # Por cada persona recorri los viajes de la persona
    # Si un nombre del viaje de la persona coincide con el viaje que estoy iterando, sumo en uno el contador
    # Modifico la lista de nombres de los viajes para crear una lista de listas con el nombre y el contador
    # Ahora recorrer esta lista auxiliar para encontrar el viaje que tiene mas veces realizado
    
    list_viajes_aux = []
    # list_viajes_aux = ["Ecuador","Colombia","Brasil"]
    for viaje in lista_viajes:
        list_viajes_aux.append(viaje.nombre)

    indice_v = 0
    for viaje in list_viajes_aux:
        contador = 0
        for persona in lista_personas:
            for viaje_persona in persona.lista_viajes:
                if viaje == viaje_persona.nombre:
                    contador+= 1
        list_viajes_aux[indice] = [viaje,contador]
        indice_v += 1
    # list_viajes_aux = [["Ecuador",2],["Colombia",3],["Brasil",0]]
    max_viaje = 0
    nombre_viaje = ""
    costo_viaje = 0
    for viaje in list_viajes_aux:
        if viaje[1] >= max_viaje:
            max_viaje = viaje[1]
            nombre_viaje = viaje[0]

    for viaje in lista_viajes:
        if viaje == nombre_viaje:
            costo_viaje = viaje.costo
    
    ganacia_total = costo_viaje * max_viaje
    print("El destino mas contradado es:" + nombre_viaje + "con una cantidad de: "+str(max_viaje)+" y su ganancia total es de: "+str(ganacia_total))
    
while True:

    print("1.	Crear lista de viajes")
    print("2.	Registrar nueva persona y su(s) viaje(s) contratado(s)")
    print("3.	Visualizar todas las personas y sus viajes")
    print("4.	Visualizar el destino más contratado y su ganancia total")
    print("5.	Visualizar la persona que más ha contratado viajes.")
    print("6.	Visualizar cual es el promedio de duración de los viajes en días.")
    print("7.	Visualizar promedio de gasto total por persona según temporada")
    print("8.	Mostrar gráfico de total gastado por cada persona")
    print("9.	Salir del programa")

    opcion = input("Ingresa una opcion: ")

    if opcion == "1":
        destino = input("Ingresa el destino: ")
        duracion = input("Ingresa el duracion: ")
        costo = int(input("Ingresa el costo: "))
        temporada = input("Ingresa el temporada: (alta, media, baja)")
        viaje = Viaje(destino, duracion, costo, temporada)
        lista_viajes.append(viaje)
        print("El viaje ha sido registrado....")
    elif opcion == "2":
        rut = input("Ingresa tu rut: ")
        nombre = input("Ingresa tu nombre: ")
        persona = Persona(rut, nombre)
        lista_personas.append(persona)
        print("La persona ha sido registrada...")
        print()
        print("Los viajes disponibles a contratar son: ")
        indice = 1
        for viaje in lista_viajes:
            print("Mostrando el viaje #", indice)
            print(viaje)
            indice = indice + 1
        
        op_viaje = int(input("Ingresa el # de viaje que deseas contratar: "))
        viaje = lista_viajes[op_viaje-1]
        persona.agregar_viaje(viaje)
        print("Viaje anadido exitosamente a la persona")
    elif opcion == "3":
        for persona in lista_personas:
            print(persona)
            persona.visualizar_viajes()
    elif opcion == "4":
        ver_destino_mas_contratado(lista_personas, lista_viajes)
    elif opcion == "6":
        break



# •	destino (str)
# •	duración en días (int)
# •	costo (int)
# •	temporada (str: alta, media, baja)


            