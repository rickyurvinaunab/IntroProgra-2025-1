import matplotlib.pyplot as plt

def mostrar_total_a_pagar(lista_personas):
    """
    Muestra un gráfico de barras con el total a pagar por cada persona.

    Argumentos:
        lista_personas (list): Lista de objetos Persona.
    """
    nombres = []
    montos = []
    for persona in lista_personas:
        total = sum([libro.costo for libro in persona.libros])
        if total > 0:
            nombres.append(f"{persona.nombre} {persona.apellido}")
            montos.append(total)
        
    if nombres:
        plt.bar(nombres, montos, color='grey')
        plt.xlabel("Persona")
        plt.ylabel("Total a pagar ($)")
        plt.title("Monto total a pagar por persona")
        plt.xticks(rotation=40)
        plt.tight_layout()
        plt.show()
    else:
        print("No hay personas con libros prestados.")
    return lista_personas   

