num1 = int(input())
num2 = int(input())

print("Buscando estrellas brillantes...")

for i in range(num1, num2+1):
    if i%2 == 0:
        suma = 0
        for j in range(1, i):
            if i % j == 0:
                suma += j
        if suma >= 16:
            print("Encontre una estrella brillante!")
            print("Coordenadas:", suma, num1)
        
