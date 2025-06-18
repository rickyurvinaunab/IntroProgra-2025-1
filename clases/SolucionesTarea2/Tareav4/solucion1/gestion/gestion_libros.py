import os
from clases.libro import Libro
from gestion.gestion_personas import agregar_o_actualizar_persona, cargar_personas, buscar_persona_por_rut
from utilidades import pedir_texto, pedir_entero, normalizar_rut
from datetime import date

ARCHIVO_DISPONIBLES = "archivo_libros_disponibles.txt"
ARCHIVO_PRESTADOS = "archivo_libros_prestados.txt"


def verificar_archivo_libros():
    """
    Verifica la existencia de los archivos de libros disponibles y prestados.

    Si alguno de los archivos no existe, los crea para asegurar que el programa
    pueda operar con ellos sin errores de archivo no encontrado.
    """
    if not os.path.exists(ARCHIVO_DISPONIBLES): # Si el archivo de disponibles no existe
        archivo = open(ARCHIVO_DISPONIBLES, "a", encoding="utf-8")  # Lo crea en modo append con codificacion UTF-8
        archivo.close() # Cierra el archivo

    if not os.path.exists(ARCHIVO_PRESTADOS): # Si el archivo de prestados no existe
        archivo = open(ARCHIVO_PRESTADOS, "a", encoding="utf-8")  # Lo crea en modo append con codificacion UTF-8
        archivo.close() # Cierra el archivo


def _obtener_ancho_max_global_caracteristica(todos_los_libros):
    """
    Funcion auxiliar para obtener el ancho maximo de CUALQUIER cadena "Campo: Valor"
    en CUALQUIER libro de la lista. Este sera el ancho fijo para cada "columna de libro".

    Args:
        todos_los_libros (list): Una lista de objetos Libro.

    Returns:
        int: El ancho maximo calculado mas un padding.
    """
    max_ancho_global = 0 # Inicializa el ancho maximo global
    campos_a_evaluar = [ # Lista de campos a evaluar para el ancho
        "ISBN", "Titulo", "Especialidad", "Autor", "Editorial",
        "Edicion", "Año", "Costo", "Cantidad disponible"
    ]

    for libro in todos_los_libros: # Itera sobre cada libro
        for campo_nombre in campos_a_evaluar: # Itera sobre cada campo del libro
            valor_campo = ""
            # Asigna el valor del campo segun su nombre
            if campo_nombre == "ISBN":
                valor_campo = libro.isbn
            elif campo_nombre == "Titulo":
                valor_campo = libro.titulo
            elif campo_nombre == "Especialidad":
                valor_campo = libro.especialidad
            elif campo_nombre == "Autor":
                valor_campo = libro.autor
            elif campo_nombre == "Editorial":
                valor_campo = libro.editorial
            elif campo_nombre == "Edicion":
                valor_campo = libro.edicion
            elif campo_nombre == "Año":
                valor_campo = libro.anio
            elif campo_nombre == "Costo":
                valor_campo = "$" + str(libro.costo)
            elif campo_nombre == "Cantidad disponible":
                valor_campo = str(libro.cantidad)

            cadena_formateada = campo_nombre + ": " + valor_campo # Forma la cadena "Campo: Valor"

            if len(cadena_formateada) > max_ancho_global: # Actualiza el ancho maximo si la cadena actual es mas larga
                max_ancho_global = len(cadena_formateada)

    return max_ancho_global + 2  # Añade 2 espacios extra para el padding


def libro_desde_linea(linea):
    """
    Crea un objeto Libro a partir de una linea de texto formateada.

    La linea de texto debe contener 9 partes separadas por ";",
    que corresponden a los atributos del libro.

    Args:
        linea (str): Una cadena de texto que representa un libro.

    Returns:
        Libro or None: Un objeto Libro si la linea es valida, de lo contrario None.
    """
    partes = linea.strip().split(";") # Divide la linea por ";"
    if len(partes) != 9: # Si la cantidad de partes no es 9, la linea no es valida
        return None
    # Retorna un objeto Libro con los datos parseados
    return Libro(
        isbn=partes[0],
        titulo=partes[1],
        especialidad=partes[2],
        autor=partes[3],
        editorial=partes[4],
        edicion=partes[5],
        anio=partes[6],
        costo=int(partes[7]), # Convierte a entero
        cantidad=int(partes[8]) # Convierte a entero
    )


def cargar_libros_disponibles():
    """
    Carga los libros disponibles desde el archivo de texto.

    Verifica que el archivo exista y lo crea si es necesario.
    Lee cada linea, la convierte en un objeto Libro y los almacena en una lista.

    Returns:
        list: Una lista de objetos Libro disponibles.
    """
    verificar_archivo_libros() # Asegura que los archivos existan
    libros = [] # Inicializa una lista vacia para los libros
    archivo = open(ARCHIVO_DISPONIBLES, "r", encoding="utf-8") # Abre el archivo en modo lectura
    for linea in archivo: # Itera sobre cada linea
        libro = libro_desde_linea(linea) # Intenta crear un libro desde la linea
        if libro is not None: # Si el libro se creo correctamente
            libros.append(libro) # Añade el libro a la lista
    archivo.close() # Cierra el archivo
    return libros # Retorna la lista de libros


def guardar_libros_disponibles(libros):
    """
    Guarda la lista de libros disponibles en el archivo de texto.

    Sobrescribe el contenido actual del archivo con la informacion
    actualizada de los libros.

    Args:
        libros (list): Una lista de objetos Libro a guardar.
    """
    archivo = open(ARCHIVO_DISPONIBLES, "w", encoding="utf-8") # Abre el archivo en modo escritura (sobrescribe)
    for libro in libros: # Itera sobre cada libro
        archivo.write(libro.a_linea_txt() + "\n") # Escribe la representacion en linea del libro
    archivo.close() # Cierra el archivo


def mostrar_libros_disponibles():
    """
    Muestra la informacion de todos los libros que estan disponibles,
    organizados en columnas y alineados para una mejor visualizacion.

    Carga los libros disponibles y los imprime en grupos de 3,
    asegurando una presentacion ordenada con anchos de columna fijos.
    """
    libros = cargar_libros_disponibles() # Carga los libros disponibles
    if len(libros) == 0: # Si no hay libros
        print("No hay libros disponibles.")
        return # Termina la funcion

    # Obtiene el ancho maximo necesario para la presentacion de las caracteristicas de los libros
    ancho_columna_libro_global = _obtener_ancho_max_global_caracteristica(libros)

    campos_presentacion = [ # Define el orden y los nombres de los campos a mostrar
        "ISBN", "Titulo", "Especialidad", "Autor", "Editorial",
        "Edicion", "Año", "Costo", "Cantidad disponible"
    ]

    i = 0
    while i < len(libros): # Itera a traves de la lista de libros
        grupo_libros = libros[i: i + 3] # Toma grupos de hasta 3 libros

        for campo_nombre in campos_presentacion: # Para cada campo a presentar
            linea_caracteristica_compuesta = "" # Inicializa la linea para este campo en el grupo
            for idx_libro_en_grupo, libro_en_grupo in enumerate(grupo_libros): # Itera sobre los libros en el grupo
                valor_campo = ""
                # Asigna el valor del campo del libro actual
                if campo_nombre == "ISBN":
                    valor_campo = libro_en_grupo.isbn
                elif campo_nombre == "Titulo":
                    valor_campo = libro_en_grupo.titulo
                elif campo_nombre == "Especialidad":
                    valor_campo = libro_en_grupo.especialidad
                elif campo_nombre == "Autor":
                    valor_campo = libro_en_grupo.autor
                elif campo_nombre == "Editorial":
                    valor_campo = libro_en_grupo.editorial
                elif campo_nombre == "Edicion":
                    valor_campo = libro_en_grupo.edicion
                elif campo_nombre == "Año":
                    valor_campo = libro_en_grupo.anio
                elif campo_nombre == "Costo":
                    valor_campo = "$" + str(libro_en_grupo.costo)
                elif campo_nombre == "Cantidad disponible":
                    valor_campo = str(libro_en_grupo.cantidad)

                entrada_columna_base = campo_nombre + ": " + valor_campo # Formato "Campo: Valor"

                # Calcula y añade espacios para alinear la columna
                espacios_a_rellenar = ancho_columna_libro_global - len(entrada_columna_base)
                entrada_columna_rellenada = entrada_columna_base + (" " * espacios_a_rellenar)

                linea_caracteristica_compuesta += entrada_columna_rellenada # Añade al acumulador de la linea

                if idx_libro_en_grupo < len(grupo_libros) - 1: # Si no es el ultimo libro del grupo, añade un separador
                    linea_caracteristica_compuesta += " | "

            print(linea_caracteristica_compuesta) # Imprime la linea completa de caracteristicas

        # Calcula la longitud del separador de grupo y lo imprime
        longitud_separador_grupo = ancho_columna_libro_global * len(grupo_libros)
        longitud_separador_grupo += (len(grupo_libros) - 1) * 3 if len(grupo_libros) > 1 else 0

        print("\n" + "=" * longitud_separador_grupo + "\n")

        i += 3 # Avanza al siguiente grupo de 3 libros


def mostrar_libros_prestados():
    """
    Muestra la informacion de todos los libros que se encuentran prestados (para administradores).

    Carga y lee el archivo de prestamos. Para cada prestamo, extrae y muestra
    la informacion relevante del libro, el RUT de la persona y la fecha.
    """
    verificar_archivo_libros() # Asegura que el archivo de prestados exista
    archivo = open(ARCHIVO_PRESTADOS, "r", encoding="utf-8") # Abre el archivo en modo lectura
    lineas = archivo.readlines() # Lee todas las lineas
    archivo.close() # Cierra el archivo

    if len(lineas) == 0: # Si no hay lineas en el archivo
        print("No hay libros prestados.")
    else:
        print("\n===== TODOS LOS LIBROS PRESTADOS =====")
        for linea in lineas: # Itera sobre cada linea (prestamo)
            partes = linea.strip().split(";") # Divide la linea
            # Asegurarse de que la linea tenga el formato esperado (libro 9 partes + rut 1 parte + fecha 1 parte = 11 partes)
            if len(partes) == 11:
                print("--------------------")
                print("ISBN: " + partes[0])
                print("Titulo: " + partes[1])
                print("Prestado a RUT: " + partes[9])
                print("Fecha de prestamo: " + partes[10])
            else: # Si el formato no es el esperado
                print("--------------------")
                print("Formato de prestamo invalido: " + linea.strip())


def mostrar_libros_prestados_por_rut(rut_usuario):
    """
    Muestra la informacion de los libros que se encuentran prestados a un RUT especifico.

    Filtra los prestamos del archivo por el RUT del usuario y los muestra.

    Args:
        rut_usuario (str): El RUT de la persona de la que se quieren ver los prestamos.
    """
    verificar_archivo_libros() # Asegura que el archivo de prestados exista
    archivo = open(ARCHIVO_PRESTADOS, "r", encoding="utf-8") # Abre el archivo en modo lectura
    lineas = archivo.readlines() # Lee todas las lineas
    archivo.close() # Cierra el archivo

    prestamos_encontrados = [] # Lista para almacenar los prestamos de la persona
    for linea in lineas: # Itera sobre cada linea de prestamos
        partes = linea.strip().split(";") # Divide la linea
        if len(partes) == 11:  # Verificar formato
            prestamo_rut = normalizar_rut(partes[9])  # El RUT de la persona prestada es la parte 9
            if prestamo_rut == normalizar_rut(rut_usuario): # Si el RUT coincide
                prestamos_encontrados.append(linea) # Añade la linea a la lista de encontrados

    if len(prestamos_encontrados) == 0: # Si no se encontraron prestamos para el RUT
        print("No tienes libros prestados en este momento.")
    else:
        print("\n===== TUS LIBROS PRESTADOS =====")
        for linea in prestamos_encontrados: # Itera sobre los prestamos encontrados
            partes = linea.strip().split(";")
            print("--------------------")
            print("ISBN: " + partes[0])
            print("Titulo: " + partes[1])
            print("Fecha de prestamo: " + partes[10])


def registrar_prestamo(rut_logueado_opcional=None):
    """
    Registra el prestamo de un libro a un cliente.

    Solicita el ISBN del libro. Si el libro esta disponible y el cliente
    no excede el limite de deuda, registra el prestamo, actualiza el stock
    y los datos de la persona.

    Args:
        rut_logueado_opcional (str, optional): El RUT del usuario actualmente logueado.
                                                Si es None, se pedira el RUT al usuario.
    """
    libros = cargar_libros_disponibles() # Carga la lista de libros disponibles
    isbn = pedir_texto("Ingrese el ISBN del libro que desea prestar: ") # Solicita el ISBN del libro
    libro_encontrado = None # Variable para el libro encontrado

    for libro in libros: # Busca el libro por ISBN
        if libro.isbn == isbn:
            libro_encontrado = libro
            break

    if libro_encontrado is None: # Si el libro no fue encontrado
        print("El libro no esta disponible.")
        return # Termina la funcion

    if libro_encontrado.cantidad == 0: # Si no hay ejemplares disponibles
        print("No hay ejemplares disponibles de ese libro.")
        return # Termina la funcion

    rut_persona = ""
    if rut_logueado_opcional is not None: # Si se proporciona un RUT logueado
        rut_persona = normalizar_rut(rut_logueado_opcional) # Usa el RUT logueado
        print("\n-------------------------------\nRegistrando prestamo para el usuario logueado: " + rut_persona)
    else: # Si no hay RUT logueado, lo pide al usuario
        rut_persona = normalizar_rut(pedir_texto("Ingrese el RUT de la persona que pide el prestamo: "))

    persona_solicitante = buscar_persona_por_rut(rut_persona) # Busca la persona por RUT

    if persona_solicitante is not None: # Si la persona existe
        if persona_solicitante.monto_adeudado > 5000: # Verifica si tiene una deuda mayor a $5000
            print("No se puede prestar el libro.")
            print(
                "La persona " + persona_solicitante.nombre + " " + persona_solicitante.apellido + " (RUT: " + persona_solicitante.rut + ") tiene una deuda de $" + str(
                    persona_solicitante.monto_adeudado) + ".")
            print("Debe saldar su deuda para poder pedir mas libros (limite: $5000).")
            return # Termina la funcion

    # Agrega o actualiza la persona (y puede calcular deuda si es un prestamo nuevo)
    persona = agregar_o_actualizar_persona(libro_prestamo=libro_encontrado, rut_ingresado=rut_persona)

    if persona is None: # Si hubo un error al obtener la persona
        print("Error al obtener la informacion de la persona para el prestamo.")
        return # Termina la funcion

    libro_encontrado.disminuir_stock() # Disminuye el stock del libro

    if libro_encontrado.cantidad == 0: # Si el stock llega a cero, lo elimina de la lista de disponibles
        libros.remove(libro_encontrado)

    guardar_libros_disponibles(libros) # Guarda la lista actualizada de libros disponibles

    # Crea la linea de registro del prestamo con ISBN, datos del libro, RUT de la persona y fecha actual
    linea = libro_encontrado.a_linea_txt() + ";" + persona.rut + ";" + str(date.today())
    archivo = open(ARCHIVO_PRESTADOS, "a", encoding="utf-8") # Abre el archivo de prestados en modo append
    archivo.write(linea + "\n") # Escribe la linea
    archivo.close() # Cierra el archivo

    print("Prestamo registrado correctamente.") # Mensaje de exito


def registrar_nuevo_libro():
    """
    Registra un nuevo libro en la base de datos o actualiza la cantidad de uno existente.

    Solicita el ISBN para verificar si el libro ya existe. Si es asi,
    pide cuantos ejemplares adicionales se desean agregar. Si no,
    solicita toda la informacion para crear un nuevo registro de libro.
    """
    libros = cargar_libros_disponibles() # Carga los libros disponibles
    isbn = pedir_texto("ISBN: ") # Solicita el ISBN

    libro_existente = None # Variable para almacenar el libro si se encuentra
    for l in libros: # Busca el libro por ISBN
        if l.isbn == isbn:
            libro_existente = l
            break

    if libro_existente is not None: # Si el libro ya existe
        print("Este libro ya existe en la base. Se actualizara la cantidad.")
        cantidad_adicional = pedir_entero("Cuantos ejemplares desea agregar? ") # Pide la cantidad a sumar
        libro_existente.cantidad += cantidad_adicional # Suma al stock existente
    else: # Si el libro no existe, solicita todos los datos para uno nuevo
        titulo = pedir_texto("Titulo: ")
        especialidad = pedir_texto("Especialidad: ")
        autor = pedir_texto("Autor: ")
        editorial = pedir_texto("Editorial: ")
        edicion = pedir_texto("Edicion: ")
        anio = pedir_texto("Ano: ")
        costo = pedir_entero("Costo del prestamo (max. $3000): ")
        if costo > 3000: # Valida el costo maximo
            print("El costo no puede superar los $3000. Se asignara $3000.")
            costo = 3000
        cantidad = pedir_entero("Cantidad de ejemplares: ")

        nuevo_libro = Libro(isbn, titulo, especialidad, autor, editorial, edicion, anio, costo, cantidad) # Crea el nuevo libro
        libros.append(nuevo_libro) # Añade el nuevo libro a la lista

    guardar_libros_disponibles(libros) # Guarda la lista actualizada de libros
    print("Libro registrado o actualizado correctamente.") # Mensaje de confirmacion


def registrar_devolucion():
    """
    Permite registrar la devolucion de un libro.

    Solicita el ISBN del libro y el RUT de la persona.
    Elimina el registro de prestamo del archivo y actualiza
    el stock del libro en el archivo de disponibles.
    """
    verificar_archivo_libros() # Asegura que los archivos existan

    isbn_devolver = pedir_texto("Ingrese el ISBN del libro a devolver: ") # Pide el ISBN
    rut_devolver = normalizar_rut(pedir_texto("Ingrese el RUT de la persona que devuelve el libro: ")) # Pide y normaliza el RUT

    lineas_a_mantener = [] # Lista para almacenar las lineas de prestamos que no se devuelven
    prestamo_encontrado_para_devolver = None # Variable para el prestamo a devolver

    archivo_prestados_lectura = open(ARCHIVO_PRESTADOS, "r", encoding="utf-8") # Abre el archivo de prestados
    for linea in archivo_prestados_lectura: # Itera sobre cada linea de prestamo
        partes = linea.strip().split(";") # Divide la linea
        if len(partes) == 11: # Si el formato es el esperado (11 partes)
            prestamo_isbn = partes[0]
            prestamo_rut = normalizar_rut(partes[9])

            # Si el ISBN y el RUT coinciden con los de la devolucion
            if prestamo_isbn == isbn_devolver and prestamo_rut == rut_devolver:
                # Crea un objeto Libro temporal con los datos del prestamo para la devolucion
                prestamo_encontrado_para_devolver = Libro(
                    isbn=partes[0],
                    titulo=partes[1],
                    especialidad=partes[2],
                    autor=partes[3],
                    editorial=partes[4],
                    edicion=partes[5],
                    anio=partes[6],
                    costo=int(partes[7]),
                    cantidad=int(partes[8]) # La cantidad aqui representa la cantidad original del libro
                )
            else:
                lineas_a_mantener.append(linea) # Si no es el prestamo a devolver, la mantiene
        else: # Si el formato de la linea no es el esperado, la mantiene (posible linea corrupta)
            lineas_a_mantener.append(linea)

    archivo_prestados_lectura.close() # Cierra el archivo de lectura

    if prestamo_encontrado_para_devolver is None: # Si no se encontro el prestamo para devolver
        print("No se encontro un prestamo para el ISBN y RUT proporcionados.")
        return # Termina la funcion

    archivo_prestados_escritura = open(ARCHIVO_PRESTADOS, "w", encoding="utf-8") # Abre el archivo de prestados en modo escritura (sobrescribe)
    for linea in lineas_a_mantener: # Escribe solo las lineas que se deben mantener
        archivo_prestados_escritura.write(linea)
    archivo_prestados_escritura.close() # Cierra el archivo de escritura

    libros_disponibles = cargar_libros_disponibles() # Carga la lista de libros disponibles
    libro_actualizado_en_disponibles = None # Variable para el libro que se actualizara

    for libro_existente in libros_disponibles: # Busca el libro en la lista de disponibles
        if libro_existente.isbn == prestamo_encontrado_para_devolver.isbn:
            libro_existente.cantidad += 1 # Incrementa la cantidad de ese libro
            libro_actualizado_en_disponibles = libro_existente
            break

    if libro_actualizado_en_disponibles is None: # Si el libro no fue encontrado en disponibles (porque su cantidad llego a 0 antes)
        prestamo_encontrado_para_devolver.cantidad = 1 # Establece su cantidad en 1
        libros_disponibles.append(prestamo_encontrado_para_devolver) # Lo agrega de nuevo a disponibles

    guardar_libros_disponibles(libros_disponibles) # Guarda la lista actualizada de libros disponibles

    print(
        "Libro '" + prestamo_encontrado_para_devolver.titulo + "' (ISBN: " + prestamo_encontrado_para_devolver.isbn + ") devuelto correctamente por " + rut_devolver + ".")