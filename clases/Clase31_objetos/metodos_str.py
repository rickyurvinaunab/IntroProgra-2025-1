class Persona:
    def __init__(self, nombre, apellido, edad, rut):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.rut = rut
        
    def __str__(self):
        return self.nombre+" "+self.apellido +"-"+str(self.edad)+ "años - "+str(self.rut)
    


# Creamos instancias de la clase Persona
persona_ricardo = Persona("Ricardo", "Urvina", 28, 27999999)

print(persona_ricardo)