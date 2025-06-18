import matplotlib.pyplot as plt
from gestion.gestion_personas import cargar_personas

def mostrar_grafico_montos():
    """
    Genera y muestra un grafico de barras con los montos pagados por cada persona.

    Carga los datos de las personas, extrae sus RUT y los montos pagados,
    y luego utiliza Matplotlib para visualizar esta informacion en un grafico.
    """
    personas = cargar_personas() # Carga la lista de objetos Persona
    if len(personas) == 0: # Verifica si no hay personas registradas
        print("No hay personas registradas.")
        return # Termina la funcion si no hay datos

    ruts = [] # Inicializa una lista para almacenar los RUT
    montos = [] # Inicializa una lista para almacenar los montos pagados

    # Recorre la lista de personas para extraer los RUT y los montos
    for persona in personas:
        ruts.append(persona.rut) # Agrega el RUT a la lista de RUTs
        montos.append(persona.monto_pagado) # Agrega el monto pagado a la lista de montos

    # Crea una nueva figura para el grafico con un tamaño especifico
    plt.figure(figsize=(10, 5))
    plt.bar(ruts, montos) # Crea el grafico de barras con RUTs en el eje X y montos en el eje Y
    plt.xlabel("RUT") # Etiqueta para el eje X
    plt.ylabel("Monto Pagado") # Etiqueta para el eje Y
    plt.title("Montos pagados por personas") # Titulo del grafico
    plt.xticks(rotation=45) # Rota las etiquetas del eje X para mejor legibilidad
    plt.tight_layout() # Ajusta automaticamente los parametros de la trama para ajustarla al area de la figura
    plt.show() # Muestra el grafico
