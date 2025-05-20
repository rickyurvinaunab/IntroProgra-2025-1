def calcular_npe(lista_notas_sol, lista_notas_con):
    s1 = lista_notas_sol[0] # nota solemene 1
    s2 = lista_notas_sol[1] # nota solemne 2
    s3 = lista_notas_sol[2] # nota solemne 3
    c1 = lista_notas_con[0] # nota control 1
    c2 = lista_notas_con[1] # nota control 1
    c3 = lista_notas_con[2] # nota control 1
    promedio_solemnes = (s1 * 0.2) +(s2 * 0.25) + (s3 * 0.3)
    promedio_controles = ((c1 +  c2 + c3)/3) * 0.25
    npe = promedio_solemnes + promedio_controles
    return npe

def nota_minima_examen(nota_presentacion_examen):
    nota_minima = (4- nota_presentacion_examen  * 0.7)/0.3
    return nota_minima

ls = [3.8, 5, 7]
lc = [6, 7, 4]
resultado = calcular_npe(ls, lc)
nme = nota_minima_examen(resultado)

print("Tu NPE es:", round(resultado, 1))
print("Tu nota minima en el examen para aprobar con 4 debe ser:", round(nme, 1))