# Ingreso de datos
arriendo = float(input("Ingrese el valor del arriendo: "))
dias_atraso = int(input("Ingrese la cantidad de dias de atraso: "))

if dias_atraso > 0:
    multa = arriendo * 0.10
else:
    multa = 0.0

total_pagar = arriendo + multa

print("Monto de la multa:", round(multa, 2))
print("Total a pagar:", round(total_pagar, 2))