num1 = int(input())
num2 = int(input())

for numero_a_revisar in range(num1, num2+1):
    if numero_a_revisar%2 == 0:
        suma_divisores = 0
        # print(numero_a_revisar)
        for divisor in range(1, numero_a_revisar):
            if numero_a_revisar % divisor == 0:
                suma_divisores += divisor
        if suma_divisores >= 16:
            print("Encontre una estrella brillante!")
            print('Coordenadas', suma_divisores, num1)


