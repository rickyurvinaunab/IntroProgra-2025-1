# total = 0
# contador = 0
# while True :
#     inp = input('Ingresa un número: ')
#     if inp == 'hecho': 
#         break
#     valor = float(inp)
#     total = total + valor     
#     contador = contador + 1

# promedio = total / contador
# print('Promedio:', promedio)

numlista = list()
while True :
    inp = input('Ingresa un número: ')
    if inp == 'hecho': 
        break
    valor = float(inp)
    numlista.append(valor)
print(numlista)
promedio = sum(numlista) / len(numlista)
print('Promedio:', promedio)