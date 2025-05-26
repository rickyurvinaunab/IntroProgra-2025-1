class Persona:
    def __init__(self, nombre, apellido, edad, rut):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.rut = rut


# Creamos instancias de la clase Persona
persona_ricardo = Persona("Ricardo", "Urvina", 28, 27999999)
persona_ingrid = Persona("Ingrid", "Medina", 29, 28999998)

# Para acceder a los atributos de un objeto, se utiliza la notación de punto

print(persona_ricardo.nombre)
# Ricardo
print(persona_ricardo.edad)
# 28

print(persona_ingrid.nombre)
# Ingrid
print(persona_ingrid.edad)
# 29



        
        