
#Pensar en donde almacenar los datos
matriz = []
for i in range(2):
    print("-----Persona----",i+1)
    edad = int(input("Ingresa tu edad: "))
    sexo = input("Ingresa tu sexo:  (h/m)")
    salario = float(input("Ingresa tu salario: "))
    estado_civil = input("Ingresa tu estado civil: ")
    color_ojos = input("Ingresa tu color de ojos: ")
    lista = [edad, sexo, salario, estado_civil, color_ojos]
    matriz.append(lista)

suma_1 = 0
suma_2 = 0
suma_3 = 0

for item in matriz:
    if item[3] == 'casado' and item[0]>25 and item[2]>1000 and item[1]=='h':
        suma_1 += 1
    elif item[3]=='soltero' and item[0]>=20 and item[0]<=45 and item[2]>2000 and item[4]=='marrones':
        suma_2 += 1
    elif item[1]=='m' and item[4]=='azules' and item[0]>=30 and item[2]>=4000 and item[3]=='soltera':
        suma_3 += 1

print("El # de hombres pregunta 1:", suma_1)
print("El # de hombres pregunta 2:", suma_2)
print("El # de mujeres pregunta 3:", suma_3)



