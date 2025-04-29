# Escribe una función llamada evaluar_nota(nota) que reciba una nota (entre 1.0 y 7.0) y 
# devuelva: “Aprobado” si la nota es mayor o igual a 4.0 
# “Reprobado” en otro caso. 

def evaluar_nota(nota):
    if nota<1 or nota>7:
        return "Nota no valida"
    
    if nota>=4:
        return "Aprobado"
    else:
        return "Reprobado"

#Ejemplo 1
print(evaluar_nota(4.55))
#Ejemplo 2
nota = 3.99
print(evaluar_nota(nota))
#Ejemplo 3
nota = float(input("Ingresa la nota: "))
resultado = evaluar_nota(nota)
print(resultado)