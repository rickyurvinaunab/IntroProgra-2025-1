# Crea una función llamada area_rectangulo(base, altura) que retorne el área del rectángulo 
# redondeado a 2 decimales. Base y altura son entregadas como parámetros

def area_rectangulo(base, altura):
    return round(base*altura, 2)

#Ejemplo 1
print(area_rectangulo(5,10))

#Ejemplo 2
area =  area_rectangulo(67.454,89)
print(area)