class Medicamento:
    """
    Se crea la clase medicamento con todos los atributos necesarios.
    """
    def __init__(self, nombre, componente, laboratorio, marca, tipo, precio):
        self.nombre = nombre
        self.componente = componente
        self.laboratorio = laboratorio
        self.marca = marca
        self.tipo = tipo
        self.precio = precio

    def __str__(self):
        return "Nombre: " + self.nombre + ", Componente: " + self.componente + ", Laboratorio: " + self.laboratorio + ", Marca: " + self.marca + ", Tipo: " + self.tipo + ", Precio: $" + str(self.precio)

class Farmacia:
    """
    Se crea la clase farmacia.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.medicamentos = []

    def agregar_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)

    def __str__(self):
        return "Farmacia: " + self.nombre

class Persona:
    """
    Se crea la clase persona.
    """
    def __init__(self, rut, nombre, segundo_nombre, apellido_paterno, apellido_materno):
        self.rut = rut
        self.nombre = nombre
        self.segundo_nombre = segundo_nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.medicamentos_comprados = []  

    def agregar_compra(self, medicamento, farmacia):
        self.medicamentos_comprados.append((medicamento, farmacia))

    def monto_total(self):
        total = 0
        for posicion in self.medicamentos_comprados:
            medicamento = posicion[0] 
            total = total + medicamento.precio
        return total

    def __str__(self):
        return "RUT: " + self.rut + ", Nombre: " + self.nombre + " " + self.segundo_nombre + " " + self.apellido_paterno + " " + self.apellido_materno + ", Monto a pagar: $" + str(self.monto_total())