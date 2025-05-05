# Se importan las funciones desde el modulo evaluacion
from evaluacion import calcular_npe, nota_minima_examen, nota_final

# Se crean listas vacias para guardar las notas
solemnes = []
controles = []

# Se pide al usuario ingresar las 3 notas solemnes una por una
print("Ingrese las 3 notas solemnes:")
for i in range(1, 4):
    nota = float(input("Nota solemne " + str(i) + ": "))
    solemnes.append(nota)

# Se pide al usuario ingresar las 3 notas de controles una por una
print("Ingrese las 3 notas de controles:")
for i in range(1, 4):
    nota = float(input("Nota control " + str(i) + ": "))
    controles.append(nota)

# Se llama a la funcion para calcular el NPE
npe = calcular_npe(solemnes, controles)

# Se muestra el resultado del NPE
print("Su NPE es:", round(npe, 2))

# Se calcula la nota minima de examen
nota_necesaria = nota_minima_examen(npe)

# Se muestra la nota de examen que necesita para aprobar
print("Para aprobar con nota 4.0 necesita sacar al menos:", round(nota_necesaria, 2), "en el examen.")

# Se pregunta si ya tiene la nota del examen
if npe < 5:
    print("Como su NPE es menor a 5, debe rendir examen.")
    nota_examen = float(input("Ingrese la nota del examen: "))
    nota_final = nota_final(npe, nota_examen)
    print("Su nota final es:", round(nota_final, 2))

    # Se verifica si aprueba o no
    if nota_final >= 4:
        print("¡Felicidades! Usted aprueba la asignatura.")
    else:
        print("Lo sentimos, usted no aprueba la asignatura.")
else:
    print("No necesita rendir examen.")
    print("Su nota final es:", round(npe, 2))
    print("Usted aprueba la asignatura.")

