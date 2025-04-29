# Crea una función llamada area_triangulo(base, altura) que 
# retorne el área del triangulo redondeado a 2 decimales. 
# Base y altura son entregadas como parámetros

def area_triangulo(base, altura):
    return round(base*altura/2, 2)

#Ejemplo 1
print(area_triangulo(5.23,10))

#Ejemplo 2
area =  area_triangulo(67, 89.34)
print(area)