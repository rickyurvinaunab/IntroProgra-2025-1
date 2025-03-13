# Escriba un programa que pida los coeficientes de una ecuación de segundo grado (a x² + b x + c = 0) y escriba la solución.
# Se recuerda que una ecuación de segundo grado puede no tener solución, tener una solución única, tener dos soluciones o que todos los números sean solución.

# Condiciones:
# Una ecuación de segundo grado puede no tener solución,  tener una solución única, tener dos soluciones o que todos los números sean solución.
# Si todos los factores son cero, todos los números son solución. Por otra parte, si a y b son cero no tiene solución
# Si a es cero hay una única solución
# Si el discriminante es mayor de cero tiene dos soluciones
# Si el discriminante es cero tiene una solución
# Si no se cumple ninguna condición no tiene solución
# El discriminante se calcula b**2 - 4*a*c

# Solicitar al usuario los coeficientes de la ecuación
a = float(input("Ingresa el coeficiente a: "))
b = float(input("Ingresa el coeficiente b: "))
c = float(input("Ingresa el coeficiente c: "))

# Calcular el discriminante
discriminante = b**2 - 4*a*c

# Verificar si todos los coeficientes son cero
if a == 0 and b == 0 and c == 0:
    print("Todos los números son solución.")
# Verificar si a y b son cero
elif a == 0 and b == 0:
    print("No tiene solución.")
# Verificar si a es cero
elif a == 0:
    x = -c / b
    print("La solución es: ", x)
# Verificar si el discriminante es mayor de cero
elif discriminante > 0:
    x1 = (-b + discriminante**0.5) / (2*a)
    x2 = (-b - discriminante**0.5) / (2*a)
    print("Las soluciones son: ", x1, " y ", x2)
# Verificar si el discriminante es cero
elif discriminante == 0:
    x = -b / (2*a)
    print("La solución es: ", x)
# Si no se cumple ninguna condición
else:
    print("No tiene solución.")