import matplotlib.pyplot as plt
def grafico_sueldos(personas):
    """Genera un grafico utilizando los sueldos y los ruts de las personas registradas
        Args:
        personas(list):Lista de las personas con los atributos rut e ingreso mensual
    """
    rut=[]
    sueldos=[]
    for persona in personas:
        rut.append(persona.rut)
        sueldos.append(persona.ingreso_mensual)   
    plt.bar(rut,sueldos, color='gray')
    plt.title("Ingresos mensuales de los adoptantes")
    plt.xlabel("Rut")
    plt.ylabel("Sueldo en CLP")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()