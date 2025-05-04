
#Pensar en donde almacenar los datos
matriz = []
canti_personas = int(input("Ingrese la cantidad de personas a registrar: "))
for i in range(canti_personas):
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
suma_4 = 0
cantidad_muj = 0
suma_edad_1 = 0
cant_empleados = 0
suma_salario = 0

for item in matriz:
    # Numero de hombres casados de edad mayor de 20 que ganen mas de 1000
    if item[3] == 'casado' and item[0]>25 and item[2]>1000 and item[1]=='h':
        suma_1 += 1
    # numero de hombres solteros de ojos marrones en edad entre 20 y 45 que ganen mas de 2000
    elif item[3]=='soltero' and item[0]>=20 and item[0]<=45 and item[2]>2000 and item[4]=='marrones':
        suma_2 += 1
    # numero de mujeres solteras de ojos azules en edad mayor de 30 que ganen mas de 4000
    elif item[1]=='m' and item[4]=='azules' and item[0]>=30 and item[2]>=4000 and item[3]=='soltera':
        suma_3 += 1
    # numero de hombres menores de 40, ojos azules que ganen mas de 3000
    elif item[1]=='h' and item[0]<40 and item[4]=='azules' and item[2]>3000:
        suma_4 += 1

    # promedio de edad de mujeres casadas de ojos negros que ganan mas de 15000
    if item[1] == "m" and item[3]=="casado" and item[4]=="negros" and item[2]>1500:
        suma_edad_1 += item[0]
        cantidad_muj += 1

    # Promedio de salaio de empleados con edad mayor a 40 anios y salario mayor a 5000
    if item[0]>40 and item[2] > 5000:
        suma_salario += item[2]
        cant_empleados += 1

print("El numero de honbres casados de edad mayor a 25 anios que ganan mas de 1000 es:", suma_1)
print("El numero de hombres solteros de ojos marrones en edad entre 20 y 45 anios que ganan mas de 2000 es:", suma_2)
print("El numero de mujeres solteras de ojos azules de edad igual a 30 anios que ganan mas de 4000 es:", suma_3)
print("El numero de hombres menores de 40 ap=nios, ojos azules que ganan mas de 3000 es:", suma_3)

if cantidad_muj>0:
    print("El promedio de edad de mujeres casadas de ojos negros que ganen mas de 1500 es:", round(suma_edad_1/cantidad_muj, 2))

if cant_empleados>0:
    print("El promedio de salario de empleados con edad mayor a 40 anios y salario mayor a 5000 es: ", round(suma_salario/cant_empleados, 2))

