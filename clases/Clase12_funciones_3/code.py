from calcular_imc import calcular_imc
from clasificar_imc import clasificar_imc

peso =  float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))
imc = calcular_imc(peso, altura)
print("Tu IMC es:", round(imc,2))
print("Clasificacion:", clasificar_imc(imc))