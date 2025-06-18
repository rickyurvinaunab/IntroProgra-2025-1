
import os
import matplotlib.pyplot as plt
from gestion.gestion_personas import cargar_personas, buscar_persona_por_rut, \
    ARCHIVO_HISTORIAL_PAGOS
from utilidades import pedir_rut, normalizar_rut
from datetime import datetime


def mostrar_grafico_historial_pagos(rut_a_graficar=None):
    """
    Genera y muestra un grafico de linea del historial de pagos de una persona.
    Si no se proporciona un RUT, pide uno al usuario.
    """
    if rut_a_graficar is None:
        rut_entrada = pedir_rut("Ingrese el RUT de la persona cuyo historial de pagos desea ver: ")
        rut_limpio = normalizar_rut(rut_entrada)
    else:
        rut_limpio = normalizar_rut(rut_a_graficar)

    persona = buscar_persona_por_rut(rut_limpio)
    if persona is None:
        print("Persona no encontrada con el RUT: " + rut_limpio)
        return

    historial_pagos = []
    if not os.path.exists(ARCHIVO_HISTORIAL_PAGOS):
        print("No hay historial de pagos registrado aun.")
        return

    # Cargar el historial de pagos
    archivo = open(ARCHIVO_HISTORIAL_PAGOS, "r", encoding="utf-8")
    for linea in archivo:
        partes = linea.strip().split(";")
        if len(partes) == 3:  # Formato: RUT;Fecha;Monto
            historial_rut = normalizar_rut(partes[0])
            if historial_rut == rut_limpio:
                fecha_str = partes[1]
                monto_pago = int(partes[2])
                historial_pagos.append({"fecha": fecha_str, "monto": monto_pago})
    archivo.close()

    if len(historial_pagos) == 0:
        print("No hay registros de pagos para " + persona.nombre + " " + persona.apellido + ".")
        return

    # Preparar datos para el grafico
    fechas = []
    montos = []

    # 'Decorar': Crear tuplas que Python puede ordenar naturalmente.
    # Cada tupla contendrá (fecha_en_datetime, monto_pago, diccionario_original_pago).
    # Al ordenar tuplas, Python compara los elementos en orden: primero la fecha, luego el monto, etc.
    pagos_para_ordenar = []
    for pago in historial_pagos:
        fecha_dt = datetime.strptime(pago["fecha"], "%Y-%m-%d")
        pagos_para_ordenar.append((fecha_dt, pago["monto"], pago))

    # 'Ordenar': Usar el método sort() directamente en la lista de tuplas.
    # Python ordenará automáticamente por la fecha (el primer elemento de la tupla).
    pagos_para_ordenar.sort()

    # 'Desdecorar' y calcular el monto acumulado a lo largo del tiempo
    monto_acumulado = 0
    for pago_tupla in pagos_para_ordenar:
        # El primer elemento de la tupla es la fecha datetime
        fechas.append(pago_tupla[0])
        # El segundo elemento de la tupla es el monto
        monto_acumulado += pago_tupla[1]
        montos.append(monto_acumulado)


    plt.figure(figsize=(12, 6))
    plt.plot(fechas, montos, marker='o', linestyle='-')
    plt.xlabel("Fecha")
    plt.ylabel("Monto Total Pagado Acumulado ($)")
    plt.title("Historial de Pagos de " + persona.nombre + " " + persona.apellido + " (RUT: " + persona.rut + ")")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()