class Persona:
    def __init__(self, nombre, apellido, edad, rut):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.rut = rut
    
    def saludar(self):
        return "Hola, soy" + self.nombre + "y tengo: " + str(self.edad)+ "años"
        

# Creamos instancias de la clase Persona
persona_ricardo = Persona("Ricardo", "Urvina", 28, 27999999)

saludo_ricardo = persona_ricardo.saludar()
print(saludo_ricardo)
# # Hola, soy Ricardo y tengo 28 años