class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    
    def quien_es_mayor(self, persona):
        
        if self.edad > persona.edad:
            return self
        elif persona.edad > self.edad:
            return persona
    
p1 = Persona("Ricardo", 28)
p2 = Persona("Ingrid", 29)

p3 = p1.quien_es_mayor(p2)

print(p3.nombre)
        