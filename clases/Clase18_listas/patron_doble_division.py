texto = "De r.urvinacordova@uandresbello.edu Sat Jan  5 09:14:16 2025"
palabras = texto.split()
#['De','r.urvinacordova@uandresbello.edu','Sat','Jan','5','09:14:16','2025']
email = palabras[1]
#'r.urvinacordova@uandresbello.edu'
piezas = email.split('@')
#['r.urvinacordova','uandresbello.edu']
print(piezas[1])