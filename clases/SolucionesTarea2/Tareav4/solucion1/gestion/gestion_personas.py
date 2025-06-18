import os
from clases.persona import Persona
from utilidades import pedir_rut, pedir_texto, pedir_entero
from datetime import date

ARCHIVO_PERSONAS = "archivo_personas.txt" # Define el nombre del archivo para guardar la informacion de las personas.
ARCHIVO_HISTORIAL_PAGOS = "historial_pagos.txt" # Define el nombre del archivo para guardar el historial de pagos.


def verificar_archivo_personas():
    """
    Verifica la existencia del archivo de personas.

    Si el archivo no existe, lo crea vacio para asegurar
    que las operaciones de lectura y escritura no fallen.
    """
    if not os.path.exists(ARCHIVO_PERSONAS): # Comprueba si el archivo no existe
        archivo = open(ARCHIVO_PERSONAS, "a", encoding="utf-8")  # Crea el archivo en modo 'append' con codificacion UTF-8
        archivo.close() # Cierra el archivo


def verificar_archivo_historial_pagos():
    """
    Verifica la existencia del archivo de historial de pagos.

    Si el archivo no existe, lo crea vacio para asegurar
    que se puedan registrar los pagos sin problemas.
    """
    if not os.path.exists(ARCHIVO_HISTORIAL_PAGOS): # Comprueba si el archivo no existe
        archivo = open(ARCHIVO_HISTORIAL_PAGOS, "a", encoding="utf-8") # Crea el archivo en modo 'append' con codificacion UTF-8
        archivo.close() # Cierra el archivo


def persona_desde_linea(linea):
    """
    Crea un objeto Persona a partir de una linea de texto.

    La linea debe estar formateada con atributos separados por ';'.
    Se espera un total de 12 partes para construir el objeto Persona.

    Args:
        linea (str): Una cadena de texto que representa los datos de una persona.

    Returns:
        Persona or None: Un objeto Persona si la linea es valida, None en caso contrario.
    """
    partes = linea.strip().split(";") # Divide la linea en partes usando ';'
    if len(partes) != 12: # Si el numero de partes no es 12, la linea es invalida
        return None

    es_admin_bool = (partes[11] == "1") # Convierte el string "1" o "0" a booleano True/False

    # Retorna una nueva instancia de Persona con los datos extraidos y convertidos
    return Persona(
        rut=partes[0],
        nombre=partes[1],
        apellido=partes[2],
        email=partes[3],
        telefono=partes[4],
        fecha_nacimiento=partes[5],
        direccion=partes[6],
        monto_pagado=int(partes[7]), # Convierte a entero
        monto_adeudado=int(partes[8]), # Convierte a entero
        username=partes[9],
        password=partes[10],
        es_admin=es_admin_bool # Asigna el valor booleano
    )


def cargar_personas():
    """
    Carga todas las personas registradas desde el archivo de texto.

    Verifica la existencia del archivo y lo crea si es necesario.
    Lee cada linea, la convierte en un objeto Persona y los almacena en una lista.

    Returns:
        list: Una lista de objetos Persona.
    """
    verificar_archivo_personas() # Asegura que el archivo de personas exista
    personas = [] # Inicializa la lista de personas
    archivo = open(ARCHIVO_PERSONAS, "r", encoding="utf-8") # Abre el archivo en modo lectura con UTF-8
    for linea in archivo: # Itera sobre cada linea del archivo
        persona = persona_desde_linea(linea) # Intenta crear un objeto Persona
        if persona is not None: # Si el objeto se creo correctamente
            personas.append(persona) # Añade la persona a la lista
    archivo.close() # Cierra el archivo
    return personas # Retorna la lista de personas cargadas


def guardar_personas(personas):
    """
    Guarda la lista de personas en el archivo de texto.

    Sobrescribe el contenido actual del archivo con la informacion
    actualizada de las personas, transformando cada objeto Persona
    a su formato de linea de texto.

    Args:
        personas (list): Una lista de objetos Persona a guardar.
    """
    archivo = open(ARCHIVO_PERSONAS, "w", encoding="utf-8") # Abre el archivo en modo escritura (sobrescribe) con UTF-8
    for persona in personas: # Itera sobre cada persona en la lista
        archivo.write(persona.a_linea_txt() + "\n") # Escribe la representacion en linea de la persona
    archivo.close() # Cierra el archivo


def buscar_persona_por_rut(rut):
    """
    Busca una persona en la lista de personas por su RUT.

    Carga todas las personas y busca la que coincida con el RUT proporcionado.

    Args:
        rut (str): El RUT de la persona a buscar.

    Returns:
        Persona or None: El objeto Persona si se encuentra, None en caso contrario.
    """
    personas = cargar_personas() # Carga todas las personas
    for persona in personas: # Itera sobre cada persona
        if persona.rut == rut: # Compara el RUT
            return persona # Retorna la persona si hay coincidencia
    return None # Retorna None si no se encuentra


def buscar_persona_por_username(username):
    """
    Busca una persona en la lista de personas por su nombre de usuario.

    Carga todas las personas y busca la que coincida con el username proporcionado.

    Args:
        username (str): El nombre de usuario de la persona a buscar.

    Returns:
        Persona or None: El objeto Persona si se encuentra, None en caso contrario.
    """
    personas = cargar_personas() # Carga todas las personas
    for persona in personas: # Itera sobre cada persona
        if persona.username == username: # Compara el nombre de usuario
            return persona # Retorna la persona si hay coincidencia
    return None # Retorna None si no se encuentra


def mostrar_personas():
    """
    Muestra la informacion de todas las personas registradas.

    Carga todas las personas y las imprime en la consola.
    """
    personas = cargar_personas() # Carga todas las personas
    if len(personas) == 0: # Si no hay personas
        print("No hay personas registradas.")
    else:
        for persona in personas: # Itera e imprime la informacion de cada persona
            print("--------------------")
            persona.mostrar_info()


def agregar_o_actualizar_persona(libro_prestamo=None, rut_ingresado=None):
    """
    Permite agregar una nueva persona o actualizar los datos de una existente.

    Solicita el RUT para identificar a la persona. Si existe, permite actualizar
    sus datos y, opcionalmente, sumarle el costo de un libro prestado a su deuda.
    Si no existe, solicita los datos para crear una nueva persona.

    Args:
        libro_prestamo (Libro, optional): Objeto Libro si se esta realizando un prestamo.
                                          Usado para añadir su costo a la deuda.
        rut_ingresado (str, optional): El RUT de la persona si ya se conoce (ej. desde un login).

    Returns:
        Persona: El objeto Persona que fue agregado o actualizado.
    """
    rut = ""
    if rut_ingresado is not None: # Si el RUT ya viene dado (ej. desde un prestamo directo)
        rut = rut_ingresado
    else: # Si no, lo pide al usuario
        rut = pedir_rut("Ingrese el RUT de la persona: ")

    personas = cargar_personas() # Carga todas las personas
    persona_existente = None # Variable para almacenar la persona si se encuentra

    for p in personas: # Busca a la persona por RUT
        if p.rut == rut:
            persona_existente = p
            break

    if persona_existente is not None: # Si la persona ya existe
        print("Persona ya registrada. Estos son sus datos:")
        persona_existente.mostrar_info() # Muestra la informacion actual

        if libro_prestamo is not None: # Si se esta prestando un libro, actualiza la deuda
            persona_existente.monto_adeudado += libro_prestamo.costo
            print("Se ha anadido $" + str(
                libro_prestamo.costo) + " a la deuda de la persona por el libro '" + libro_prestamo.titulo + "'.")

        respuesta = input("Desea actualizar otros datos de la persona? (s/n): ").lower() # Pregunta por actualizacion de datos
        if respuesta == "s": # Si el usuario desea actualizar
            print("Ingrese los nuevos datos. Deje vacio cualquier campo que no desea cambiar.")

            # Pide nuevos valores para cada campo, mostrando el valor actual entre corchetes
            nuevo_nombre = input("Nombre [" + persona_existente.nombre + "]: ").strip()
            nuevo_apellido = input("Apellido [" + persona_existente.apellido + "]: ").strip()
            nuevo_email = input("Email [" + persona_existente.email + "]: ").strip()
            nuevo_telefono = input("Telefono [" + persona_existente.telefono + "]: ").strip()
            nueva_fecha_nacimiento = input("Fecha de nacimiento [" + persona_existente.fecha_nacimiento + "]: ").strip()
            nueva_direccion = input("Direccion [" + persona_existente.direccion + "]: ").strip()

            # Actualiza el atributo solo si el nuevo valor no esta vacio
            if nuevo_nombre != "":
                persona_existente.nombre = nuevo_nombre
            if nuevo_apellido != "":
                persona_existente.apellido = nuevo_apellido
            if nuevo_email != "":
                persona_existente.email = nuevo_email
            if nuevo_telefono != "":
                persona_existente.telefono = nuevo_telefono
            if nueva_fecha_nacimiento != "":
                persona_existente.fecha_nacimiento = nueva_fecha_nacimiento
            if nueva_direccion != "":
                persona_existente.direccion = nueva_direccion

            print("\n--- Datos de Usuario (login) ---")
            respuesta_username = input("Desea cambiar el Username/Contrasena de login? (s/n): ").lower()
            if respuesta_username == "s": # Si desea cambiar credenciales de login
                nuevo_username = pedir_texto("Nuevo Username [" + persona_existente.username + "]: ")
                persona_existente.username = nuevo_username
                persona_existente.password = pedir_texto("Nueva Contrasena para login: ")

            print("\n--- Rol Administrativo ---")
            if persona_existente.es_admin: # Si ya es admin
                print("Esta persona ya es un administrador.")
                respuesta_admin = input("Desea revocarle el rol de administrador? (s/n): ").lower()
                if respuesta_admin == "s": # Si desea revocar el rol
                    persona_existente.es_admin = False
                    print("Rol administrativo revocado.")
            else: # Si no es admin
                print("Esta persona no es un administrador.")
                respuesta_admin = input("Desea asignarle el rol de administrador? (s/n): ").lower()
                if respuesta_admin == "s": # Si desea asignar el rol
                    persona_existente.es_admin = True
                    print("Rol administrativo asignado.")

    else: # Si la persona no existe, se registra una nueva
        print("Registrando nueva persona sin credenciales de login iniciales.")
        # Pide todos los datos para la nueva persona
        nombre = pedir_texto("Nombre: ")
        apellido = pedir_texto("Apellido: ")
        email = pedir_texto("Email: ")
        telefono = pedir_texto("Telefono: ")
        fecha_nacimiento = pedir_texto("Fecha de nacimiento: ")
        direccion = pedir_texto("Direccion: ")

        monto_pagado_inicial = 0 # Inicia con monto pagado en 0
        monto_adeudado_inicial = 0 # Inicia con monto adeudado en 0
        if libro_prestamo is not None: # Si se esta prestando un libro, se añade a la deuda inicial
            monto_adeudado_inicial = libro_prestamo.costo
            print("El costo del libro '" + libro_prestamo.titulo + "' es $" + str(
                libro_prestamo.costo) + ", anadido a la deuda.")

        username_nuevo = "" # Nombre de usuario inicial vacio
        password_nuevo = "" # Contrasena inicial vacia
        es_admin_nuevo = False # Por defecto, no es admin

        # Crea la nueva instancia de Persona
        persona_existente = Persona(rut, nombre, apellido, email, telefono, fecha_nacimiento, direccion,
                                    monto_pagado_inicial, monto_adeudado_inicial,
                                    username_nuevo, password_nuevo, es_admin_nuevo)
        personas.append(persona_existente) # Añade la nueva persona a la lista

    guardar_personas(personas) # Guarda la lista actualizada de personas
    print("Persona registrada o actualizada correctamente.") # Mensaje de confirmacion
    return persona_existente # Retorna la persona (nueva o actualizada)


def registrar_pago():
    """
    Permite a una persona registrar un pago para reducir su deuda y registra la transaccion.

    Solicita el RUT y el monto a pagar. Actualiza la deuda y el monto pagado
    de la persona, y registra la transaccion en el historial de pagos.
    """
    rut = pedir_rut("Ingrese el RUT de la persona que realiza el pago: ") # Pide el RUT de la persona que paga
    personas = cargar_personas() # Carga todas las personas
    persona_encontrada = None # Variable para la persona encontrada

    for p in personas: # Busca a la persona por RUT
        if p.rut == rut:
            persona_encontrada = p
            break

    if persona_encontrada is None: # Si la persona no es encontrada
        print("Persona no encontrada.")
        return # Termina la funcion

    print("Monto adeudado actual de " + persona_encontrada.nombre + " " + persona_encontrada.apellido + ": $" + str(
        persona_encontrada.monto_adeudado)) # Muestra la deuda actual
    if persona_encontrada.monto_adeudado == 0: # Si no tiene deuda
        print("Esta persona no tiene deudas pendientes.")
        return # Termina la funcion

    monto_a_pagar = pedir_entero("Ingrese el monto a pagar: ") # Pide el monto a pagar
    if monto_a_pagar <= 0: # Valida que el monto sea positivo
        print("El monto a pagar debe ser positivo.")
        return # Termina la funcion

    if monto_a_pagar > persona_encontrada.monto_adeudado: # Si el monto a pagar es mayor que la deuda
        print("El monto a pagar es mayor que la deuda. Se pagara la deuda completa.")
        monto_a_pagar = persona_encontrada.monto_adeudado # Se ajusta el monto al total de la deuda

    persona_encontrada.monto_adeudado -= monto_a_pagar # Reduce la deuda
    persona_encontrada.monto_pagado += monto_a_pagar # Aumenta el monto pagado acumulado

    guardar_personas(personas) # Guarda la lista actualizada de personas

    verificar_archivo_historial_pagos() # Asegura que el archivo de historial exista
    # Crea la linea para el historial de pagos: RUT;Fecha;MontoPagado
    linea_historial = persona_encontrada.rut + ";" + str(date.today()) + ";" + str(monto_a_pagar)
    archivo_historial = open(ARCHIVO_HISTORIAL_PAGOS, "a", encoding="utf-8") # Abre el archivo en modo append
    archivo_historial.write(linea_historial + "\n") # Escribe la linea en el historial
    archivo_historial.close() # Cierra el archivo

    print("Pago registrado correctamente. Deuda restante: $" + str(persona_encontrada.monto_adeudado)) # Mensaje de exito