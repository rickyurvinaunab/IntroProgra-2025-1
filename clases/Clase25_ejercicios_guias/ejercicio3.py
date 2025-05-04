llamadas = []
dias = [
    "Lunes",
    "Martes",
    "Miercoles",
    "Jueves",
    "Viernes",
    "Sabado",
    "Domingo"
]
while True:

    print("Menu de opciones: ")
    print("1. Ingresar Datos ")
    print("2. Ver costos de llamdas ")
    print("3. Salir ")
    opcion = input("Ingresa la opcion (1-3): ")
    if opcion == "1":
        print("Ingreso de los datos")
        tipo_llamada = input("Ingresa el tipo de llamada: (1) Internacional, (2) Nacionala, (3) Local: ")
        duracion = int(input("Ingresa la duracion de la llamada: "))
        hora = int(input("Ingresa la hora de la llamada: "))
        dia = int(input("Ingresa el dia de la llamada: "))
        lista = [tipo_llamada, duracion, hora, dia]
        llamadas.append(lista)
    
    elif opcion == "2":
        llamadas = [
            ["1", 10, 14, 1],
            ["2", 7, 12, 2],
            ["3", 2, 23, 3],
            ["2", 3, 8, 4],
            ["3", 7, 10, 5],
            ["3", 9, 3, 6],
        ]

        if len(llamadas)!= 0:
            indice_llamada = 1
            for llamada in llamadas:
                print("Informacion de la llamada", indice_llamada)
                print("Tipo de llamada:", llamada[0])
                print("Duracion de la llamada:", llamada[1])
                print("Hora de la llamada:", llamada[2])
                print("Dia de la llamada:", dias[llamada[3]-1])
                # Calculo del costo
                costo = 0
                if llamada[0]=="1":
                    if llamada[1] > 3:
                        costo = 7.59 + (llamada[1] -3) *3.03
                    else: 
                        costo = 7.59
                elif llamada[0] == "2":
                    if llamada[1] >3:
                        costo = 1.2 +(llamada[1-3])*0.48
                    else:
                        costo = 1.20
                elif llamada[0] == "3":
                    costo = 0.60
                
                #internacionales 40% sabados a partir de las 14 y domingos todo el dia
                descuento = 0
                if (llamada[0] == "1" and llamada[3] == 6 and llamada[2]>= 14) or (llamada[0] == "1" and llamada[3] == 7):
                    print("Descuento del 40%")
                    descuento = costo * 0.4

                # Nacionales el 50% de lunes a viernes a partir de las 14 h y el doming todo el dia
                if (llamada[0] == "2" and llamada[3] >= 1 and llamada[3] <= 5 and llamada[2] >= 14) or (llamada[0] == "2" and llamada[3] == 7):
                    print("Descuento del 50%")
                    descuento = costo * 0.5

                costo = costo - descuento
                print("El costo de la llamada", indice_llamada," es:", round(costo,2))
                indice_llamada += 1
                print("-"*8)
        else:
            print("No hay llamadas")

    elif opcion == "3":
        print("Saliendo del sistema")
        break