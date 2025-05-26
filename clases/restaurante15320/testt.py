# Escribe tu código aquí
def buscar_g(indice_f, indice_c, tablero):
    while indice_f<len(tablero):
        col = tablero[indice_f][indice_c]
        if col != 1:
            return False
        indice_f += 1
    return True

def estan_alineados_completo(tablero):
    indice_f = 0
    for fila in tablero:
        indice_c = 0
        for col in fila:
            if indice_f == 0 and col == 1:
                res_g = buscar_g(indice_f, indice_c, tablero)
                if res_g == False:
                    return False
            indice_c += 1
        indice_f += 1
    
    return True

tablero = [
    [0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1],
    [0, 2, 2, 2, 2, 0, 1],
    [0, 2, 2, 2, 2, 0, 1]
]
print(estan_alineados_completo(tablero))

tablero = [
    [0, 0, 0, 1, 0, 0, 1, 2, 0, 1, 2],
    [0, 1, 2, 1, 0, 0, 1, 2, 0, 1, 2],
    [0, 2, 1, 1, 0, 0, 1, 2, 0, 2, 1]
]
print(estan_alineados_completo(tablero))

tablero = [
    [2, 1, 1, 0, 0, 1, 2, 0],
    [2, 1, 0, 1, 0, 0, 2, 1],
    [1, 1, 2, 0, 2, 0, 1, 0],
    [0, 0, 1, 2, 1, 0, 1, 2],
    [1, 2, 1, 0, 2, 0, 0, 1],
    [1, 1, 2, 2, 0, 0, 1, 0]
]
print(estan_alineados_completo(tablero))