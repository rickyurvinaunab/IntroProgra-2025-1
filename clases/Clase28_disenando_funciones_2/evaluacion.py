# Funcion para calcular el NPE segun la formula dada
def calcular_npe(solemnes, controles):
    # Se calcula el promedio de los 3 controles
    promedio_controles = (controles[0] + controles[1] + controles[2]) / 3

    # Se aplica la formula del NPE con los porcentajes correspondientes
    npe = solemnes[0] * 0.2 + solemnes[1] * 0.25 + solemnes[2] * 0.3 + promedio_controles * 0.25

    # Se retorna el valor del NPE
    return npe

# Funcion para calcular la nota minima de examen para aprobar con nota final 4.0
def nota_minima_examen(npe):
    # Se aplica la formula de nota minima: (4 - NPE * 0.7) / 0.3
    nota_examen = (4 - npe * 0.7) / 0.3

    # Se retorna la nota necesaria
    return nota_examen

def nota_final(npe, nota_examen):
    # Se aplica la formula de nota final: NPE * 0.7 + examen * 0.3
    nota_final = npe * 0.7 + nota_examen * 0.3

    # Se retorna la nota final
    return nota_final