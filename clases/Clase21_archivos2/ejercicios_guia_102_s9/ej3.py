
# 5. Escribir un programa que pida al usuario una palabra y muestre por 
# pantalla el número de veces que
# contiene cada vocal

palabra = input("Ingresa la palabra: ")
cant_a = 0
cant_e = 0
cant_i = 0
cant_o = 0
cant_u = 0

for letra in palabra:
    if letra == "A" or letra == "a":
        cant_a += 1
    elif letra == "e" or letra == "E":
        cant_e += 1

print(cant_a)
print(cant_e)
























# palabra = input("Ingresa una palabra")

# cant_a = 0
# cant_e = 0
# cant_i = 0
# cant_o = 0
# cant_u = 0
# for letra in palabra:
#     if letra == "a" or letra == "A":
#         cant_a += 1
#     elif letra == "e" or letra == "E":
#         cant_e += 1
#     elif letra == "i" or letra == "I":
#         cant_i += 1
#     elif letra == "o" or letra == "O":
#         cant_o += 1
#     elif letra == "u" or letra == "U":
#         cant_u += 1

# print("La cantidad de a es:", cant_a)
# print("La cantidad de e es:", cant_e)
# print("La cantidad de i es:", cant_i)
# print("La cantidad de o es:", cant_o)
# print("La cantidad de u es:", cant_u)