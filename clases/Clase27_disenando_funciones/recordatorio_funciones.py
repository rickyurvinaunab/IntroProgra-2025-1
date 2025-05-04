# Que es una funcion

def saludar():
    print("¡Hola mundo!")

#sintaxis de una funcion
def suma(a, b):
    return a + b

resultado = suma(3,4)
print(resultado)

print(suma(98,34))

#parametros y argumentos

def saludar(nombre):  # parámetro
    print("Hola", nombre)

saludar("Ana")        # argumento

#Alcance de las variables
x = 10  # global

def ejemplo():
    x = 5  # local
    print(x)

ejemplo()
print(x)

#Modificando una variable global
contador = 0

def incrementar():
    global contador
    contador += 1

# Funciones anidadas y alcance
def exterior():
    def interior():
        print("Dentro")
    interior()

exterior()