import os
import matplotlib.pyplot as plt
from gestion.gestion_personas import cargar_personas, buscar_persona_por_rut, ARCHIVO_HISTORIAL_PAGOS
from utilidades import pedir_rut, normalizar_rut
from datetime import datetime


def mostrar_grafico_deudas():
    """
    Genera y muestra un grafico de barras con los montos adeudados por cada persona (general).

    Carga todas las personas registradas, filtra aquellas con deuda pendiente
    y visualiza sus RUTs y montos adeudados en un grafico de barras.
    """
    personas = cargar_personas() # Carga la lista de objetos Persona
    if len(personas) == 0: # Verifica si no hay personas registradas
        print("No hay personas registradas para mostrar deudas.")
        return # Termina la funcion si no hay datos

    ruts = [] # Lista para almacenar los RUT de personas con deuda
    deudas = [] # Lista para almacenar los montos adeudados

    # itera sobre cada persona para identificar las que tienen deuda
    for persona in personas:
        if persona.monto_adeudado > 0: # Si la persona tiene un monto adeudado mayor que 0
            ruts.append(persona.rut) # Agrega el RUT a la lista
            deudas.append(persona.monto_adeudado) # Agrega el monto adeudado a la lista

    if len(deudas) == 0: # Si despues de filtrar, no hay deudas pendientes
        print("No hay deudas pendientes para mostrar en el grafico. Todos al dia!")
        return # Termina la funcion

    plt.figure(figsize=(10, 5)) # Crea una nueva figura para el grafico
    plt.bar(ruts, deudas, color='salmon') # Crea el grafico de barras con RUT en X y deudas en Y
    plt.xlabel("RUT") # Etiqueta para el eje X
    plt.ylabel("Monto Adeudado ($)") # Etiqueta para el eje Y
    plt.title("Deudas Pendientes por Persona (General)") # Titulo del grafico
    plt.xticks(rotation=45, ha="right") # Rota las etiquetas del eje X para mejor legibilidad
    plt.tight_layout() # Ajusta el diseno para evitar superposiciones
    plt.show() # Muestra el grafico


def mostrar_grafico_deuda_pagado_por_usuario(rut_a_graficar=None):
    """
    Genera y muestra un grafico de barras que compara el monto adeudado
    y el monto total pagado acumulado para una persona especifica.

    Puede recibir un RUT como parametro o solicitarlo al usuario.
    Muestra la deuda actual y el monto total pagado por el usuario.

    Args:
        rut_a_graficar (str, optional): El RUT de la persona a graficar.
                                        Si es None, se pedira al usuario.
    """
    if rut_a_graficar is None: # Si no se proporciona un RUT, lo solicita al usuario
        rut_entrada = pedir_rut("Ingrese el RUT de la persona cuyo estado de deuda/pagos desea ver: ")
        rut_limpio = normalizar_rut(rut_entrada) # Normaliza el RUT ingresado
    else:
        rut_limpio = normalizar_rut(rut_a_graficar) # Normaliza el RUT proporcionado

    persona = buscar_persona_por_rut(rut_limpio) # Busca la persona por el RUT normalizado
    if persona is None: # Si la persona no es encontrada
        print("Persona no encontrada con el RUT: " + rut_limpio)
        return # Termina la funcion

    # Datos para el grafico: categorias y sus valores correspondientes
    categorias = ['Deuda Actual', 'Monto Pagado Acumulado']
    valores = [persona.monto_adeudado, persona.monto_pagado]
    colores = ['red', 'green']  # Rojo para deuda, verde para monto pagado

    plt.figure(figsize=(8, 6)) # Crea una nueva figura para el grafico
    plt.bar(categorias, valores, color=colores) # Crea el grafico de barras
    plt.ylabel("Monto ($)") # Etiqueta para el eje Y
    plt.title("Estado de Deuda y Pagos de " + persona.nombre + " " + persona.apellido + " (RUT: " + persona.rut + ")") # Titulo del grafico
    plt.grid(axis='y') # Agrega lineas de cuadricula solo en el eje Y
    plt.tight_layout() # Ajusta el diseno
    plt.show() # Muestra el grafico


def mostrar_grafico_historial_pagos(rut_a_graficar=None):
    """
    Genera y muestra un grafico de linea del historial de pagos acumulado de una persona.

    Carga el historial de pagos desde el archivo, lo filtra por el RUT especificado,
    ordena los pagos por fecha y calcula el monto acumulado a lo largo del tiempo
    para su visualizacion.

    Args:
        rut_a_graficar (str, optional): El RUT de la persona cuyo historial de pagos
                                        desea ver. Si es None, se pedira al usuario.
    """
    if rut_a_graficar is None: # Si no se proporciona un RUT, lo solicita al usuario
        rut_entrada = pedir_rut("Ingrese el RUT de la persona cuyo historial de pagos desea ver: ")
        rut_limpio = normalizar_rut(rut_entrada)
    else:
        rut_limpio = normalizar_rut(rut_a_graficar)

    persona = buscar_persona_por_rut(rut_limpio) # Busca la persona por el RUT
    if persona is None: # Si la persona no es encontrada
        print("Persona no encontrada con el RUT: " + rut_limpio)
        return

    historial_pagos = [] # Inicializa la lista para el historial de pagos
    if not os.path.exists(ARCHIVO_HISTORIAL_PAGOS): # Verifica si el archivo de historial existe
        print("No hay historial de pagos registrado aun.")
        return

    archivo = open(ARCHIVO_HISTORIAL_PAGOS, "r", encoding="utf-8") # Abre el archivo del historial de pagos
    for linea in archivo: # Itera sobre cada linea del archivo
        partes = linea.strip().split(";") # Divide la linea en partes
        if len(partes) == 3:  # Formato esperado: RUT;Fecha;Monto
            historial_rut = normalizar_rut(partes[0]) # Normaliza el RUT de la linea
            if historial_rut == rut_limpio: # Si el RUT de la linea coincide con el buscado
                fecha_str = partes[1] # Extrae la fecha
                monto_pago = int(partes[2]) # Extrae el monto del pago y lo convierte a entero
                historial_pagos.append({"fecha": fecha_str, "monto": monto_pago}) # Agrega el pago al historial
    archivo.close() # Cierra el archivo

    if len(historial_pagos) == 0: # Si no se encontraron pagos para la persona
        print("No hay registros de pagos para " + persona.nombre + " " + persona.apellido + ".")
        return

    fechas = [] # Lista para almacenar las fechas de los pagos (objetos datetime)
    montos = [] # Lista para almacenar los montos acumulados

    pagos_para_ordenar = [] # Lista temporal para ordenar los pagos por fecha
    for pago in historial_pagos: # Convierte las fechas de cadena a objetos datetime para poder ordenar
        pagos_para_ordenar.append((datetime.strptime(pago["fecha"], "%Y-%m-%d"), pago["monto"], pago))

    pagos_para_ordenar.sort() # Ordena los pagos por fecha

    monto_acumulado = 0 # Inicializa el monto acumulado
    for pago_tupla in pagos_para_ordenar: # Itera sobre los pagos ordenados para calcular el acumulado
        fechas.append(pago_tupla[0]) # Agrega la fecha al eje X
        monto_acumulado += pago_tupla[1] # Suma el monto actual al acumulado
        montos.append(monto_acumulado) # Agrega el monto acumulado al eje Y

    plt.figure(figsize=(12, 6)) # Crea una nueva figura para el grafico de linea
    plt.plot(fechas, montos, marker='o', linestyle='-') # Crea el grafico de linea
    plt.xlabel("Fecha") # Etiqueta para el eje X
    plt.ylabel("Monto Total Pagado Acumulado ($)") # Etiqueta para el eje Y
    plt.title("Historial de Pagos de " + persona.nombre + " " + persona.apellido + " (RUT: " + persona.rut + ")") # Titulo
    plt.grid(True) # Muestra la cuadricula
    plt.xticks(rotation=45) # Rota las etiquetas del eje X
    plt.tight_layout() # Ajusta el diseno
    plt.show() # Muestra el grafico