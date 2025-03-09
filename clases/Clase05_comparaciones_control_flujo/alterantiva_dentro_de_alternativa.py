#Escribe un programa que verifique si un año es bisiesto.
#Un año es bisiesto si es divisible por 4 (anio % 4 == 0).
#De estos años bisiestos hay que eliminar los que son divisibles
#por 100 y añadir los que son divisibles por 400.

print("Hola, bienvenido al sistema para saber si un año es bisiesto o no")
print("Para saber si un año es bisiesto o no ingresa el año a validar")

anio = int(input("Ingresa el año: "))


# Verificar si es bisiesto utilizando if anidados
if anio % 4 == 0:
    if anio % 100 == 0:
        if anio % 400 == 0:
            print("El año ", anio, " es bisiesto.")
        else:
            print("El año ", anio, " no es bisiesto.")
    else:
        print("El año", anio, " es bisiesto.")
else:
    print("El año", anio, " no es bisiesto.")