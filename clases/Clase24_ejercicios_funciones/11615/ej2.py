# Escribe una función llamada evaluar_edad(anio) que reciba el 
# año de nacimiento de una persona. Si la persona es mayor de edad, 
# retornar “Mayor de edad”. En otro caso retonar ”Menor de edad”


def evaluar_edad(anio):
    edad = 2025 - anio
    if edad >=18:
        return "Mayor de edad"
    else:
        return "Menor de edad"

#Ejemplo 1
print(evaluar_edad(1996))
#Ejemplo 2
anio = 2009
resultado = evaluar_edad(anio)
print(resultado)
