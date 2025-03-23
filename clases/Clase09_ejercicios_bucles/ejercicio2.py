vida_restante = int(input())
dano = int(input())
disparos = int(input())


for disparo in range(disparos):
    print("BANG!")
    vida_restante = vida_restante - (dano + disparo)

print("clack, clackm boom!")
print(vida_restante)