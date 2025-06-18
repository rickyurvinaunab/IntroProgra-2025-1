class Empresa:
    """
    Clase que le permite a la empresa llevar la gestion de arriendos de una forma mas precisa y real de sus procesos de arrendamiento.

    Atributos:
    nombre_empresa (str): nombre de la empresa.
    rut_empresa (str): rut de la empresa.
    phono_empresa (str): telefono de la empresa.
    email_empresa (str): email de la empresa.
    direccion (str): direccion de la empresa.
    precio (float): precio del arriendo.
    """

    def __init__(self, nombre_empresa, rut_empresa, phono_empresa, email_empresa, direccion, precio):
        """
        Inicializa una nueva empresa.

        Parametros:
        nombre_empresa (str): nombre de la empresa.
        rut_empresa (str): rut de la empresa.
        phono_empresa (str): telefono de la empresa.
        email_empresa (str): email de la empresa.
        direccion (str): direccion de la empresa.
        precio (float): precio del arriendo.
        """
        self.nombre_empresa = nombre_empresa
        self.rut_empresa = rut_empresa
        self.phono_empresa = phono_empresa
        self.email_empresa = email_empresa
        self.direccion = direccion
        self.precio = precio
        self.arrendatarios = []


    def __str__(self):
        """
        Retorna el rut, nombre, phono, email y direccion de la empresa.
        """
        return "El nombre de la empresa es: " + self.nombre_empresa + " Rut: " + self.rut_empresa + " Phono: " + self.phono_empresa + " Email: " + self.email_empresa + " Direccion: " + self.direccion
    
    