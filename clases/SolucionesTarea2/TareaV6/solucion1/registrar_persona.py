class Persona:
    """Classe que representa a la persona"""
    def __init__(self,rut,primer_nombre,segundo_nombre,apellido,segundo_apellido,telefono,correo_electronico,direccion,ingreso_mensual):
        """Inicializa los atributos de la clase persona
        Args: 
        Rut (str): rut
        primer_nombre (str):primer nombre de la persona
        segundo_nombre (str): segundo nombre de la persona
        apellido (str)= primer apellido de la persona
        segundo_apellido (str)=segundo apellido de la persona
        telefono (str)= Telefono de la persona
        correo_electronico (str)=correo electronico de la persona
        direccion(str)= direccion de la persona
        ingreso_mensual (int)= ingreso mensual de la persona   
        mascotas (list) = lista de las mascotas de la persona
        """
        self.rut=rut
        self.primer_nombre=primer_nombre
        self.segundo_nombre=segundo_nombre
        self.apellido=apellido
        self.segundo_apellido=segundo_apellido
        self.telefono=telefono
        self.correo_electronico=correo_electronico
        self.direccion=direccion
        self.ingreso_mensual=ingreso_mensual   
        self.mascotas=[]
    def __str__(self):
        """"Retorna los datos de la persona como rut,nombres,apellidos,direccion,correo,telefono,ingresos y sus mascotas
        
            Returns:
            Primer nombre, segundo nombre,apellido,segundo apellido, telefono, correo electronico, direccion, ingreso mensual, mascotas
            """
        if len(self.mascotas)==0:
            mascotas_texto="no posee mascotas"
        else:
            mascotas_texto=""
            for mascota in self.mascotas:
                mascotas_texto += str(mascota) 
        return ("Rut: " + self.rut +"\n" +
                "Nombre: "+ self.primer_nombre + self.segundo_nombre + self.apellido + self.segundo_apellido + "\n"
                "telefono: "+ self.telefono + "\n"
                "Correo electronico: " + str(self.correo_electronico)+"\n"
                "Direccion: "+ str(self.direccion)+"\n"
                "Ingresos: " + str(self.ingreso_mensual) + "\n"
                "Mascotas: " + mascotas_texto
                )

def calcular_uf(ingreso_mensual):
    """Calcula las uf diviendo el ingreso de la persona por el valor de 1 uf
        args:
        Ingreso_mensual(int): ingreso mensual de la persona
        uf(int): valor de 1 uf"""
    uf=39204
    return ingreso_mensual/uf
def ingresar_persona():
    """Pide los datos al usuario y luego valida si es apto o no para adoptar, 
        conviertiendo su sueldo que esta en pesos,
        si este es mayor a 15 uf se registrara correctamente, si no, 
        no se le permitira adoptar ni registrarse
        returns:
        Persona: Si los ingresos cumplen con la condicion
        None: Si los ingresos no superan las 15 uf"""
    print("Registrando usuario...")
    rut=input("ingrese su rut: ")
    primer_nombre=input("ingrese su primer nombre: ")
    segundo_nombre=input("ingrese su segundo nombre: ")   
    apellido=input("ingrese su apellido paterno: ")
    segundo_apellido=input("ingrese su apellido materno: ")
    telefono=input("ingrese su telefono de contacto: ")
    correo_electronico=input("ingrese su correo electronico: ")
    direccion=input("ingrese su direccion de domicilio: ")
    ingreso_mensual=int(input("ingrese su ingreso mensual en pesos chilenos:$ "))
    ingreso_mensual_pesos=ingreso_mensual
    while ingreso_mensual<=0:
        print("ingresa un valor de ingreso valido")
        ingreso_mensual=int(input("ingrese su ingreso mensual en pesos chilenos:$ "))
    ingreso_mensual=calcular_uf(ingreso_mensual)
    if ingreso_mensual>=15:
        print("sus ingresos son validos para adoptar")
        return Persona(rut,primer_nombre,segundo_nombre,apellido,segundo_apellido,telefono,correo_electronico,direccion,ingreso_mensual_pesos)
    else:
        print("Lamentablemente, por sus ingresos, no es posible la adopcion")
        return None
