# Datos de entrada
# distancia = 150
distancia = input("Ingrese la distancia: ")
distancia = int(distancia)
consumo = float(input("Ingrese el consumo del vehiculo: "))
precio_combustible = float(input("Ingrese el precio del combustible: "))
costo_peajes = int(input("Ingrese el costo de los peajes: "))

#calculo de consumo total de gasolina
consumo_gasolina = distancia * consumo
#calculo costo combustible
costo_combustible = consumo_gasolina * precio_combustible
#calcular costo total
costo_total = costo_combustible + costo_peajes

print(costo_total)