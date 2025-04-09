corredor = input()
ligereza = int(input())
print(f"Bienvenid@ a la carrera {corredor}")
if ligereza < 50:
    print("Tienes un auto liviano")
elif ligereza >=50 and ligereza < 100:
    print("Tienes un auto mediano")
elif ligereza>=100:
    print("Tienes un auto pesado")
N = int(input())

nueva_velocidad = 0
for i in range(N):
    minima = int(input())
    maxima = int(input())
    velocidad = int(input())
    if minima<=ligereza and ligereza<=maxima:
        print(f"Ligereza valida para el neumatico de velocidad {velocidad}")
        if velocidad>nueva_velocidad:
            nueva_velocidad = velocidad
            print(f"Tu nueva velocidad es {nueva_velocidad}")

print(f"Tu velocidad para la carrera sera {nueva_velocidad}")
distancia = int(input())
print(f"Comenzando la vuelta en la pista de {distancia} metros")
tiempo = 1
distancia_acu = 0
contador = 0
velocidad = nueva_velocidad
contador_estrellas = 0
poder_estrela = False

while distancia > 0:
    poder_estrela = False
    condicion = input().strip()
    if condicion == "platano":
        velocidad_a = round(velocidad/4)
        distancia -= velocidad_a
        print(f"[ {distancia_acu} m ] Has resbalado con un platano! Tu velocidad se reduce al 25%")
        distancia_acu += velocidad_a
    elif condicion == "agua":
        velocidad_a = round(velocidad/2)
        distancia -= velocidad_a
        print(f"[ {distancia_acu} m ] Te deslizaste por el agua! Tu velocidad se reduce al 50%")
        distancia_acu += velocidad_a
    elif condicion == "caparazon":
        velocidad_a = 0
        distancia -= velocidad_a
        print(f"[ {distancia_acu} m ] Chocaste con un caparazon! Tu velocidad se reduce a 0")
        distancia_acu += velocidad_a
    elif condicion == "no hay evento":
        velocidad_a = velocidad
        distancia -= velocidad_a
        print(f"[ {distancia_acu} m ] Avanzas con normalidad")
        distancia_acu += velocidad
    elif condicion == "estrella":
        poder_estrela = True
        if contador_estrellas < 2:
            velocidad_a = round(velocidad*1.2)
            distancia -= velocidad_a
            print(f"[ {distancia_acu} m ] Recogiste una estrella! Tu velocidad aumenta un 20% y no te afectan los otros eventos")
            distancia_acu += velocidad_a
            # print(f"La velocidad actual es {velocidad_a}")
            for i in range(4):
                # velocidad_a = round(velocidad*1.2)
                print(f"La velocidad actual es {velocidad_a}")
                condicion = input()
                if condicion == "estrella":
                    print(f"[ {distancia_acu} m ] Te encontraste con una estrella, pero como ya tienes el poder activado no puedes usarla")
                elif condicion  in ["caparazon", "platano", "agua"]:
                    print(f"[ {distancia_acu} m ] Te encontraste con el evento {condicion}, pero gracias al poder de la estrella lo esquivas!")
                elif condicion == "no hay evento":
                    print(f"[ {distancia_acu} m ] Avanzas con el poder de tu estrella!")
                distancia -= velocidad_a
                distancia_acu += velocidad_a
        else:
            velocidad_a = velocidad
            distancia -= velocidad_a
            print(f"La velocidad actual es {velocidad_a}")
            print(f"[ {distancia_acu} m ] Te encontraste con una estrella, pero ya usaste el máximo permitido :(")
            distancia_acu += velocidad 
        
        contador_estrellas += 1
    
    if poder_estrela!= True:
        print(f"La velocidad actual es {velocidad_a}")
        contador += 1
        poder_estrela = False
        # poder_estrela = False

print(f"Has completado 1 vuelta en {contador} segundos!")