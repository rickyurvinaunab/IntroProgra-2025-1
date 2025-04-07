cantidad_ventanas = int(input("Ingrese la cantidad de ventanas: "))
area_total_ventanas = 0.0

for i in range(1, cantidad_ventanas + 1):
    print("Ventana", i)
    ancho = float(input("Ancho (m): "))
    alto = float(input("Alto (m): "))
    area = ancho * alto
    area_total_ventanas += area

transmision_luz = float(input("Ingrese el porcentaje de transmision de luz del vidrio (0 a 100): "))

area_luz_efectiva = area_total_ventanas * (transmision_luz / 100)

print("Area total de ventanas:", round(area_total_ventanas, 2), "m2")
print("Area efectiva de luz que entra:", round(area_luz_efectiva, 2), "m2")