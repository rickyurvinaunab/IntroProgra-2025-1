# Escribe una función llamada calcular_hipotenusa que tome las longitudes de 
# los dos catetos de un triángulo rectángulo y retorne la longitud de la hipotenusa.
import math

def calcular_hipotenusa(cateto1, cateto2):
    hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    return hipotenusa


#Ejemplo de uso
cateto1 = 3
cateto2 = 4
hipotenusa = calcular_hipotenusa(cateto1, cateto2)
print("La hipotenusa es:", hipotenusa) # 5.0