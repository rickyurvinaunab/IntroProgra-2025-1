class Mascota:
    """Clase que representa a la mascota"""
    def __init__(self,nombre,tipo,color,peso,fecha_de_nacimiento,observacion):
        self.nombre=nombre
        self.tipo=tipo
        self.color=color
        self.peso=peso
        self.fecha_de_nacimiento=fecha_de_nacimiento
        self.observacion=observacion
        self.adoptante=None
    def __str__(self):
        datos=("Nombre: " + str(self.nombre) +"\n" +
                "tipo: "+ self.tipo + "\n"
                "color:"+ self.color + "\n"
                "peso: " + str(self.peso)+ ("kg") + "\n"
                "fecha de nacimiento: "+ str(self.fecha_de_nacimiento)+"\n"
                "observacion: " + self.observacion + "\n"
                )
        if self.adoptante is not None:
            datos+= ("Su dueño es: " + self.adoptante.primer_nombre + " " + self.adoptante.apellido)
        else:
            datos+=("Aun no es adoptado")
        return datos
                
def ingresar_mascota():
    """Registra los datos de una mascota pidiendole sus datos y luego retornando una Mascota
        Returns:
        Mascota:Objeto de la clase mascota con los datos ingresados por el administrador
    """
    print("Registrando Mascota...")
    nombre=input("ingrese el nombre de la mascota: ")
    tipo=input("Ingrese su tipo(Gato/Perro): ")
    color=input("Ingrese el color de la mascota: ")
    peso=input("ingrese el peso en kg:")   
    fecha_de_nacimiento=input("Cuando nacio la mascota: ")
    observacion=input("¿Alguna observacion sobre la mascota?: ")
    return Mascota(nombre,tipo,color,peso,fecha_de_nacimiento,observacion)

def mostrar_mascotas(mascotas):
    """Muestra las mascotas en pantalla recorriendo la lista de mascotas"""
    if len(mascotas)>0:
        for mascota in mascotas:
            print(mascota)
            print("-----------------")
    else:
        print("Aún no se han registrado mascotas")
 