#Este script muestra el ejemplo de algunas funciones built-in de Python

#Función len()
#La función len() devuelve la longitud de un objeto iterable.
#Ejemplo:
lista=[1,2,3,4,5]
print("La longitud de la lista es:", len(lista))
#La función len() también se puede usar con strings
cadena="Hola mundo"
print("La longitud de la cadena es:", len(cadena))

#Función max()
#La función max() devuelve el elemento más grande de un objeto iterable.
#Ejemplo:
lista=[1,2,3,4,5]
print("El elemento más grande de la lista es:", max(lista))
#La función max() también se puede usar con strings
cadena="Hola mundo"
print("El elemento más grande de la cadena es:", max(cadena))

#Función round()
#La función round() redondea un número a un número entero.
#Ejemplo:
numero=3.1416
print("El número redondeado es:", round(numero))

#Función isinstance()
#La función isinstance() devuelve True si el objeto especificado es del tipo especificado, de lo contrario, devuelve False.
#Ejemplo:
numero=3
print("¿El número es un entero?", isinstance(numero,int))
#La función isinstance() también se puede usar con strings
cadena="Hola mundo"
print("¿La cadena es un string?", isinstance(cadena,str))

