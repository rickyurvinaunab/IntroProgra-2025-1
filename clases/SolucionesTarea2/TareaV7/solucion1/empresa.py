
from Estudiantes import Estudiante
from empresa_creacion import Empresa

class Empresario:
    
    """Gestionara una lista de empresas que se registrara."""
    
    lista_empresas=[]

   
    def __init__(self):
        
        """se empezara con una lista vacía de empresas para ir agregando datos."""
        self.empresas = []
   
    def mostrar_empresa(self):
        
        """
        Se añadira una empresa a la lista.
        
        Argumento:
            empresa (Empresa): Objeto Empresa a agregar."""
            
        self.empresas = []
        self.empresas.append(self.rutt)
        self.empresas.append(self.nombre)
        self.empresas.append(self.telefono)
        self.empresas.append(self.emaill)
        self.empresas.append(self.direccion)
        print("-----------------------------------")
        print(self.empresas)
