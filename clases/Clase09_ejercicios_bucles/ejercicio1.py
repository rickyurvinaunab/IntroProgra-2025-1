
cantidad = int(input())

contador_hits = 0
for i in range(cantidad):
    palabra = input()
    if palabra == "Hit!":
        contador_hits += 1
print(contador_hits)