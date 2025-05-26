class NombreDeClase:
    def __init__(self, parametro1, parametro2):
        self.atributo1 = parametro1
        self.atributo2 = parametro2

    def metodo(self):
        # Código del método aquí
        print("Este es un método de la clase")

    def __str__(self):
        return "Atributo1: " + str(self.atributo1) + ", Atributo2: " + str(self.atributo2)