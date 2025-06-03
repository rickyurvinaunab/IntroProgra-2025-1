class Persona:
    def __init__(self, nombre, edad, rut):
        self.nombre = nombre #esto es un atirbuto
        self.edad = edad
        self.rut = rut
    
    def __str__(self):
        return self.nombre +" - "+self.rut
    
    def saludar(self): # Esto es un metodo
        print("Hola mi nombre es:", self.nombre, "y mi edad es:", self.edad)


rosales = Persona("Benjamin","19","28888888")
rosales.saludar()
print(rosales)

isi = Persona("Isi","19","29999999")
isi.saludar()
print(isi)
