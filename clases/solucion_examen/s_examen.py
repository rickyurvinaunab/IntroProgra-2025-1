import matplotlib.pyplot as plt

class Estudiante:

    def __init__(self, rut, nombre, sexo, nivel, direccion, comuna, monto):
        self.rut = rut
        self.nombre = nombre
        self.sexo = sexo
        self.nivel = nivel
        self.direccion = direccion
        self.comuna = comuna
        self.monto = monto
    
    def __str__(self):
        return f"El estudiante con rut: "+self.rut+ " tiene un monto de:" + str(self.monto)

def ver_datos(lista_estudiantes):

    for est in lista_estudiantes:
        print(est)

def ver_comuna(lista_estudiantes):
    comunas = []
    for est in lista_estudiantes:
        if est.comuna not in comunas:
            comunas.append(est.comuna)
    
    inidce_c = 0
    for comuna in comunas:
        contador = 0
        suma = 0
        for est in lista_estudiantes:
            if comuna == est.comuna:
                contador += 1
                suma += est.monto
        comunas[inidce_c] = [comuna, contador, suma]
        inidce_c += 1
    
    max_c = 0
    nombre_c = ""
    total_max = 0
    for comuna in comunas:
        if comuna[1] >= max_c:
            max_c = comuna[1]
            nombre_c = comuna[0]
            total_max = comuna[2]
    
    texto = "La comuna que tiene mas tne es: " + nombre_c + " con un total de "+ str(max_c) + " y el monto total es: "+str(total_max) + "\n"
    archivo = open("informacion.txt", "w")
    archivo.write(texto)
    archivo.close()
    
    print("La comuna que tiene mas tne es: " + nombre_c + " con un total de "+ str(max_c) + " y el monto total es: "+str(total_max))

def ver_promedios_sexo(lista_estudiantes):
    sexos = ["M","F"]
    
    inidce_c = 0
    for sexo in sexos:
        contador = 0
        suma = 0
        promedio = 0
        for est in lista_estudiantes:
            if sexo == est.sexo:
                contador += 1
                suma += est.monto
        promedio = suma/contador
        sexos[inidce_c] = [sexo, contador, promedio, suma]
        inidce_c += 1
    
    
    print("El sexo M tiene un total de" + str(sexos[0][3])+ " y un promedio de: " + str(sexos[0][2]))
    print("El sexo F tiene un total de" + str(sexos[1][3])+ " y un promedio de: " + str(sexos[1][2]))

def ver_montos_mayores_menores(lista_estudiantes):
    min_e = 10000000
    nombre_min = ""
    sexo_min = ""
    comuna_min = ""

    max_e = 0
    nombre_max = ""
    sexo_max = ""
    comuna_max = ""

    for est in lista_estudiantes:
        if est.monto >= max_e:
            max_e = est.monto
            nombre_max = est.nombre
            sexo_max = est.sexo
            comuna_max = est.comuna
        
        if est.monto <= min_e:
            min_e = est.monto
            nombre_min = est.nombre
            sexo_min = est.nombre
            comuna_min = est.comuna
    
    print("El nombre de mayor monto es: " + nombre_max + " de la comuna: ", comuna_max, "de sexo: ", sexo_max,"con un monto total de: ", str(max_e))
    print("El nombre de menor monto es: " + nombre_min + " de la comuna: ", comuna_min, "de sexo: ", sexo_min,"con un monto total de: ", str(min_e))

def ver_grafico(lista_estudiantes):
    nombres = []
    montos = []

    for est in lista_estudiantes:
        nombres.append(est.nombre)
        montos.append(est.monto)
    
    fig, ax = plt.subplots()
    ax.bar(nombres, montos)
    plt.show()

lista_estudiantes = [
    Estudiante("1-9", "Ana Torres", "F", "universidad", "Calle 1", "sj", 30000),
    Estudiante("2-7", "Luis Pérez", "M", "colegio", "Calle 2", "sj", 25000),
    Estudiante("3-5", "Carla Díaz", "F", "universidad", "Calle 3", "macul", 40000),
    Estudiante("4-4", "Pedro Gómez", "M", "colegio", "Calle 4", "macul", 22000),
    Estudiante("5-3", "Sofía Rivas", "F", "universidad", "Calle 5", "providencia", 27000)
]
# lista_estudiantes = []
opcion = ""
while opcion == "":

    print("1. Ingrese datos")
    print("2. Ver datos")
    print("3. Ver comunas")
    print("4. Promedio por sexo")
    print("5. Ver grafico")
    print("6. Salir")

    opcion = input("Ingresa una opcion: ")

    if opcion == "1":
        rut = input("ingresa rut: ")
        nombre = input("ingresa nombre: ")
        sexo = input("ingresa sexo (F/M): ")
        nivel = input("ingresa nivel: ")
        if nivel != "colegio" and nivel !="universidad":
            print("Nivel no valido")
            continue
        direccion = input("ingresa direccion: ")
        comuna = input("ingresa comuna: ")
        monto = int(input("Ingresa el monto: "))
        if monto <= 20000 and monto >= 40000:
            print("Monto invalido")
            continue
        estudiante = Estudiante(rut, nombre, sexo, nivel, direccion, comuna, monto)
        lista_estudiantes.append(estudiante)
    elif opcion == "2":
        ver_datos(lista_estudiantes)
    elif opcion == "3":
        ver_comuna(lista_estudiantes)
    elif opcion == "4":
        ver_promedios_sexo(lista_estudiantes)
    elif opcion == "5":
        ver_grafico(lista_estudiantes)
    elif opcion == "6":
        break

    opcion = ""

   
    
        
