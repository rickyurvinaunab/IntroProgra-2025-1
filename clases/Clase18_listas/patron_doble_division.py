texto = "De r.urvinacordova@uandresbello.edu Sat Jan  5 09:14:16 2025"
palabras = texto.split()
email = palabras[1]
piezas = email.split('@')
print(piezas[1])