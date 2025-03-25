# Condiciones:
# Una ecuación de segundo grado puede no tener solución,  tener una solución única, 
# tener dos soluciones o que todos los números sean solución. 
# Si todos los factores son cero, todos los números son solución. 
# Por otra parte, si a y b son cero no tiene solución
# Si a es cero hay una única solución
# Si el discriminante es mayor de cero tiene dos soluciones
# Si el discriminante es cero tiene una solución 
# Si no se cumple ninguna condición no tiene solución
# El discriminante se calcula b**2 - 4*a*c

#Datos de entrada

a = float(input("Ingrese el primer coeficiente: "))
b = float(input("Ingrese el segundo coeficiente: "))
c = float(input("Ingrese el tercer coeficiente: "))

discriminante = b**2 - 4*a*c

# Si todos los factores son cero, todos los números son solución. 
# Por otra parte, si a y b son cero no tiene solución
# Si a es cero hay una única solución
# Si el discriminante es mayor de cero tiene dos soluciones
# Si el discriminante es cero tiene una solución 
# Si no se cumple ninguna condición no tiene solución

if (a == 0  and b == 0 and c == 0):
    print("Todos los numeros son solucion...")
elif a == 0 and b == 0:
    print("No tiene solucion..")
elif a == 0:
    print("Hay una unica solucion...")
elif discriminante > 0:
    resultado_1 = (-b + ((b**2 - 4*a*c)**0.5))/2*a
    resultado_2 = (-b - ((b**2 - 4*a*c)**0.5))/2*a
    print("Tiene dos soluciones...")
    print("las soluciones son: ", resultado_1, resultado_2)
elif discriminante == 0:
    resultado = -b / 2*a
    print("tiene una solucion...")
    print("La solucion es:", resultado)
else:
    print("No tiene solucion...")