 
class Estudiante:
    """Representa a un estudiante contratado, con sus datos personales, UF, semestres acutales, carrera y universidad ."""
    

    def __init__(self, renombre, donombre, apellidopaterno, apellidomaterno, rut, numeroT, email, fda, salarioL, carrera, universidad, semestreactual):
        
        """
        Se inicia  un procedimiento de recolectar datos de un estudiante.
        
        Argumentos:
            renombre (str): Primer nombre.
            donombre (str): Segundo nombre.
            apellidopaterno (str): Apellido paterno.
            apellidomaterno (str): Apellido materno.
            rut (str): RUT del estudiante.
            numeroT (str): Teléfono de contacto.
            email (str): Correo electrónico.
            fda (str): Fecha de nacimiento (DD.MM.AA).
            salarioL (str): Salario líquido en UF.
            carrera (str): Carrera que estudia.
            universidad (str): Universidad a la que pertenece.
            semestreactual (str): Semestre actual (1-7)."""
        
        
        
        self.rut=rut
        self.primer_nombre= renombre
        self.segundo_nombre= donombre
        self.apellidop=apellidopaterno
        self.apellidom=apellidomaterno
        self.numeroT= numeroT
        self.email= email
        self.fda=fda
        self.salarioL=salarioL
        self.carrera=carrera
        self.universidad=universidad
        self.semestreactual=semestreactual
        self.empresa=""

    def mostrar_informacion(self):
        
        """Se mostrara en la terminal del codigo los datos completos del estudiante."""
        
        print('----------Datos del estudiantes----------')
        print('Nombres: ' + self.primer_nombre + " " + self.segundo_nombre)
        print('Apellidos: ' + self.apellidop + " " + self.apellidom)
        print('rut: ' + self.rut)
        print('Numero telefonico: ' + self.numeroT)
        print('email: ' + self.email)
        print('fecha de nacimiento: ' + self.fda)
        print('salario Liquido: ' + self.salarioL)
        print('carrera: ' + self.carrera)
        print('universidad: ' + self.universidad)
        print('semestre: ' + self.semestreactual)
   
    def generar_contrato(self, empresa):
        self.empresa = empresa
        empresa.estudiantes.append(self)
        print(" Vinculo generado exitosamente...")