
class Persona:
  def __init__(self,rut,nombre,segundo,paterno,materno,fono,email,direccion,ingresos):
    """
     incia una nueva clase llamada persona con los siguientes atributos

     Args:
         rut (str): rut que tendra la persona
         nombre (str):Nombre que tendra la persona
         segundo (str): Segundo nombre de la persona
         paterno (str): Apellido paterno
         materno (str): Apellido materno
         fono (str): Telefono personal de la persona
         email (str): Email de la persona
         direccion (str): Direccion de la persona
         ingresos (float): Ingresos en clp de la persona para luego hacer una convencion
    """
    self.nombre= nombre
    self.segundo= segundo
    self.rut= rut
    self.paterno= paterno
    self.materno= materno
    self.fono= fono
    self.email= email
    self.direccion= direccion 
    self.ingresos= ingresos
    self.mascotas=[] #lista de mascotas que la persona adopto
  def __str__(self):
     """
     Devuelva los atributos de la persona en modo str para vizualizar su estado

     Returns:
         Nombre: str(self.nombre)
         Segundo nombre: str(self.nombre)
         y asi sucesivamente
     """
     return  "Rut" +  str(self.rut)+ "\n"+"Nombre:" + str(self.nombre) + "\n" +"Segundo nombre:" + str(self.segundo) +"\n"+ "Apellido paterno:" + str(self.paterno) + "\n" +"Segundo apellido:"+ str(self.materno) + "\n" +"Telefono:" + str(self.fono)+"\n"+ "Email:"+ str(self.email)+"\n" + "Direccion:" + str(self.direccion)+ "\n"
class Mascota:

  def __init__(self, nombre_m,tipo,color,peso,fecha,observacion,adoptante):
    self.nombre_m= nombre_m
    self.tipo= tipo
    self.color=color
    self.peso= peso
    self.fecha= fecha
    self.observacion=observacion
    self.adoptante= adoptante #personas que adoptan la mascota
  def __str__(self):
     """
     Devuelve los atributos de la mascota para ver el estado del objeto
     
     Returns:
         Nombre: str(self.nombre)
         Tipo: str(self.tipo)
         y asi sucesivamente
     """
     return "Nombre:" + str(self.nombre_m) + "\n" +"Tipo:" + str(self.tipo) +"\n"+ "Color:" + str(self.color) + "\n" +"Peso:"+ str(self.peso) + "\n" + "Fecha:"+ str(self.fecha)+"\n" + "Observacion:" + str(self.observacion)+ "\n"

