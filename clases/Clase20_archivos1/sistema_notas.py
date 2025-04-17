notas=[]
opcion = input("Ingrese la opcion: \n 1. Ingresar notas \n 2. Mostrar notas \n 3. Salir \n")

while opcion != "3":
    if opcion == "1":
        alumno=input("Ingrese el nombre del alumno: ")
        nota = int(input("Ingrese la nota del set: "))
        notas.append([alumno,nota])
    elif opcion == "2":
        print("Las notas ingresadas son: ", notas)
    else:
        print("Opcion no valida")
    opcion = input("Ingrese la opcion: \n 1. Ingresar notas \n 2. Mostrar notas \n 3. Salir \n")