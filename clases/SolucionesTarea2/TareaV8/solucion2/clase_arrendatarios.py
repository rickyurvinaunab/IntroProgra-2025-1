class Arrendatario:
    """
    Clase que representa a una persona que arrienda.

    Atributos:
    rut_arrendador (str): rut del arrendador.
    nombre1 (str): primer nombre del arrendador.
    nombre2 (str): segundo nombre del arrendador.
    apellidop (str): apellido paterno del arrendador.
    apellidoa (str): apellido materno del arrendador.
    phono (str): telefono del arrendador.
    email (str): email del arrendador.
    nacimiento (str): fecha de nacimiento del arrendador.
    ingreso (float): ingresos mensuales del arrendador.
    arriendo (float): monto a pagar del arrendador.
    """

    def __init__(self, rut_arrendador, nombre1, nombre2, apellidop, apellidoa, phono, email, nacimiento, ingreso, arriendo):
        """
        Inicializa un nuevo arrendatario.

        Parametros:
        rut_arrendador (str): rut del arrendador.
        nombre1 (str): primer nombre del arrendador.
        nombre2 (str): segundo nombre del arrendador.
        apellidop (str): apellido paterno del arrendador.
        apellidoa (str): apellido materno del arrendador.
        phono (str): telefono del arrendador.
        email (str): email del arrendador.
        nacimiento (str): fecha de nacimiento del arrendador.
        ingreso (float): ingresos mensuales del arrendador.
        arriendo (float): monto a pagar del arrendador.
        """
        self.rut_arrendador = rut_arrendador
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        self.apellidop = apellidop
        self.apellidoa = apellidoa
        self.phono = phono
        self.email = email
        self.nacimiento = nacimiento
        self.ingreso = ingreso
        self.arriendo = arriendo
        self.empresas = [] 
        
    def generar_arriendo(self,empresa): 
        """
        Vincula al arrendatario con una empresa.
        """
        empresa.arrendatarios.append(self)
        self.empresas.append(empresa)
    
    def desvincular_arriendo(self, empresa):
        """
        Desvincula al arrendatario de una empresa
        """
        self.empresas.remove(empresa)
        empresa.arrendatarios.remove(self)
        print("El arrendatario fue desvinculado de: "+ empresa.nombre_empresa)