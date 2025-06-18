def pedir_entero(mensaje):
    """
    Solicita al usuario un numero entero y valida la entrada.

    Continua pidiendo la entrada hasta que el usuario ingrese
    un valor que pueda ser convertido a un numero entero.

    Args:
        mensaje (str): El mensaje que se mostrara al usuario para pedir la entrada.

    Returns:
        int: El numero entero valido ingresado por el usuario.
    """
    while True:
        entrada = input(mensaje).strip()
        if entrada.isdigit():
            return int(entrada)
        print("Por favor, ingresa un numero entero valido.")

def pedir_texto(mensaje):
    """
    Solicita al usuario una cadena de texto y valida que no este vacia.

    Continua pidiendo la entrada hasta que el usuario ingrese
    un texto no vacio.

    Args:
        mensaje (str): El mensaje que se mostrara al usuario para pedir la entrada.

    Returns:
        str: La cadena de texto no vacia ingresada por el usuario.
    """
    while True:
        entrada = input(mensaje).strip()
        if entrada != "":
            return entrada
        print("Este campo no puede estar vacio.")

def normalizar_rut(rut_input):
    """
    Normaliza una cadena de RUT eliminando caracteres no alfanumericos y convirtiendo a minusculas.

    Se utiliza para limpiar el RUT antes de su validacion, permitiendo formatos flexibles.

    Args:
        rut_input (str): El RUT tal como lo ingreso el usuario.

    Returns:
        str: El RUT normalizado (solo numeros y 'k', en minusculas).
    """
    return ''.join(c.lower() for c in rut_input if c.isalnum())

def pedir_rut(mensaje):
    """
    Solicita al usuario un RUT y valida su formato basico.

    Normaliza el RUT ingresado y verifica que cumpla con una estructura basica:
    al menos 2 caracteres, con todos los digitos excepto el ultimo, y el ultimo
    caracter siendo un digito o 'k'.

    Args:
        mensaje (str): El mensaje que se mostrara al usuario para pedir el RUT.

    Returns:
        str: El RUT valido y normalizado ingresado por el usuario.
    """
    while True:
        entrada = input(mensaje).strip()
        rut_limpio = normalizar_rut(entrada)
        if len(rut_limpio) >= 2 and rut_limpio[:-1].isdigit() and rut_limpio[-1] in "0123456789k":
            return rut_limpio
        print("RUT no valido. Ejemplo: 244739652 o 24.473.965-K")
