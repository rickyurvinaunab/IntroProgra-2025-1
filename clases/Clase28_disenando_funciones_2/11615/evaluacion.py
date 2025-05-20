def calcular_npe(lista_s, lista_c):
    nota_solemnes = lista_s[0] * 0.2 + lista_s[1]*0.25 + lista_s[2] *0.3
    nota_controles = (sum(lista_c) / 3) * 0.25
    npe = nota_solemnes + nota_controles
    return npe

def nota_minima_examen(nota_pe):
    nota_minima = (4 - nota_pe *0.7)/0.3
    return nota_minima

#### PROGRAMA PRINCIPAL #### 
lista_s = []
for i in range(3):
    s = float(input("Ingresa la nota de la solemne "+str(i)+": "))
    lista_s.append(s)

lista_c = [4,3,5]
nota_resultado = calcular_npe(lista_s, lista_c)
nme = nota_minima_examen(nota_resultado)
print("Tu npe es:", nota_resultado)
print("Tu nota minima debe ser:", nme)





