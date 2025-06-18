class Empresa:
    """Representa una empresa que contrata con los datos pedidos por el usuario y los estudiantes que esten vinculados a dicha empresa."""
    
    def __init__(self, rutt, nombre, telefono, emaill, direccion):
        """
        Se inicia un procedimiento de recolectar datos de una empresa.
        
        Argumentos:
            rutt (str): RUT de la empresa.
            nombre (str): Nombre de la empresa.
            telefono (str): Teléfono de contacto de la empresa.
            emaill (str): Email de contacto de la empresa.
            direccion (str): Dirección de la empresa.
        """
        self.rutt=rutt
        self.nombre = nombre
        self.telefono= telefono
        self.emaill= emaill
        self.direccion= direccion
        self.estudiantes =[]
       
    def ingresar_empresa(self):
        
        """pedira los datos de la empresa dependiendo lo que ponga el usuario"""
        
        print("\n---Ingresar nueva empresa---")
        self.rutt = input("RUT de la empresa: ")
        self.nombre = input("Nombre de la empresa: ")
        self.telefono = input("Teléfono de contacto: ")
        self.emaill = input("Email de contacto: ")
        self.direccion = input("Dirección: ")
       
    def mostrar_datosdeempresa(self):
        
        """Se mostrara en la terminal del codigo los datos completos de la empresa."""
        
        print("\n----------Datos de las empresas----------")
        print("Nombre de la empresa: " + self.nombre)
        print("Rut: " + self.rutt)
        print("Numero telefonico de contacto: " + self.telefono)
        print("Email de contacto: " + self.emaill)
        print("Direccion de la empresa: " + self.direccion)
        print("-----------------------------------------")
