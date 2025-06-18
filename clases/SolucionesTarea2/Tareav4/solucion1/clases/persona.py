class Persona:
    """
    CLASE DE PERSONA.

    Representa una persona en el sistema, que puede ser un cliente
    o un usuario con rol administrativo. Contiene informacion personal,
    de contacto, financiera y de acceso.
    """
    def __init__(self, rut, nombre, apellido, email, telefono, fecha_nacimiento, direccion, monto_pagado,
                 monto_adeudado, username="", password="", es_admin=False):  # ELIMINADO admin_passcode
        """
            Inicializa una nueva instancia de la clase Persona.

            Args:
                rut (str): El RUT de la persona (identificador unico).
                nombre (str): El nombre de la persona.
                apellido (str): El apellido de la persona.
                email (str): La direccion de correo electronico de la persona.
                telefono (str): El numero de telefono de la persona.
                fecha_nacimiento (str): La fecha de nacimiento de la persona en formato de cadena.
                direccion (str): La direccion fisica de la persona.
                monto_pagado (float): El monto total pagado acumulado por la persona.
                monto_adeudado (float): El monto total que la persona debe actualmente.
                username (str): Nombre de usuario para el inicio de sesion (opcional).
                password (str): Contrasena para el inicio de sesion (sin hash, opcional).
                es_admin (bool): Indica si la persona tiene rol administrativo (True) o no (False).
        """
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.monto_pagado = monto_pagado
        self.monto_adeudado = monto_adeudado
        self.username = username
        self.password = password
        self.es_admin = es_admin  # Se mantiene, pero sin passcode asociado

    def mostrar_info(self):
        """
            Muestra en la consola toda la informacion detallada de la persona.
        """
        print("RUT: " + self.rut)
        print("Nombre: " + self.nombre + " " + self.apellido)
        print("Email: " + self.email)
        print("Telefono: " + self.telefono)
        print("Fecha de nacimiento: " + self.fecha_nacimiento)
        print("Direccion: " + self.direccion)
        print("Monto pagado acumulado: $" + str(self.monto_pagado))
        print("Monto adeudado: $" + str(self.monto_adeudado))
        print("Usuario: " + self.username)
        print("Es Admin: " + ("Si" if self.es_admin else "No")) # Muestra "Si" o "No" segun el valor booleano

    def a_linea_txt(self):
        """
            Convierte los atributos de la persona en una cadena de texto.

            Esta cadena esta formateada para ser guardada en un archivo,
            usando el punto y coma (;) como separador entre cada atributo.
            Los valores booleanos se convierten a "1" o "0".

            Returns:
                str: Una cadena de texto con la informacion de la persona.
        """
        return self.rut + ";" + \
            self.nombre + ";" + \
            self.apellido + ";" + \
            self.email + ";" + \
            self.telefono + ";" + \
            self.fecha_nacimiento + ";" + \
            self.direccion + ";" + \
            str(self.monto_pagado) + ";" + \
            str(self.monto_adeudado) + ";" + \
            self.username + ";" + \
            self.password + ";" + \
            ("1" if self.es_admin else "0") # Convierte True a "1" y False a "0"

    def actualizar_dato(self, campo, nuevo_valor):
        """
            Actualiza un atributo especifico de la persona con un nuevo valor.

            Permite modificar la informacion de la persona de forma individual
            segun el campo especificado.

            Args:
                campo (str): El nombre del atributo a actualizar (ej. "nombre", "email", "monto_adeudado").
                nuevo_valor (any): El nuevo valor que se asignara al atributo.
        """
        if campo == "nombre":
            self.nombre = nuevo_valor
        elif campo == "apellido":
            self.apellido = nuevo_valor
        elif campo == "email":
            self.email = nuevo_valor
        elif campo == "telefono":
            self.telefono = nuevo_valor
        elif campo == "fecha_nacimiento":
            self.fecha_nacimiento = nuevo_valor
        elif campo == "direccion":
            self.direccion = nuevo_valor
        elif campo == "monto_pagado":
            self.monto_pagado = nuevo_valor
        elif campo == "monto_adeudado":
            self.monto_adeudado = nuevo_valor
        elif campo == "username":
            self.username = nuevo_valor
        elif campo == "password":
            self.password = nuevo_valor
        elif campo == "es_admin":  # Se mantiene
            self.es_admin = nuevo_valor
        # ELIMINADO elif campo == "admin_passcode": # Este campo ya no existe en la clase