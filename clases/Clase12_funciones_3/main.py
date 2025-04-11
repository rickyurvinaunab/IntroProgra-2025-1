from cimc import calcular_imc
from clas_imc import clasificar_imc


a = float(input())
b =  float(input())

imc = calcular_imc(a,b)
clasificacion = clasificar_imc(imc)

print("El imc es: ", imc)
print("Tu clasificacion es: ", clasificacion)
