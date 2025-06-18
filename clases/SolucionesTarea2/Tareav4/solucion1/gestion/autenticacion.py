from gestion.gestion_personas import cargar_personas, guardar_personas, buscar_persona_por_username, \
    buscar_persona_por_rut
from clases.persona import Persona
from utilidades import pedir_texto, pedir_entero, pedir_rut, normalizar_rut


def registrar_usuario():
    """
    Permite a un nuevo usuario registrarse en el sistema.
    Asigna un rol de usuario normal por defecto.
    """
    print("\n===== REGISTRO DE NUEVO USUARIO =====")

    rut_ingresado = pedir_rut("Ingrese su RUT: ")
    persona_existente_rut = buscar_persona_por_rut(rut_ingresado)

    if persona_existente_rut is not None: # Si ya existe una persona con ese RUT
        print("Ya existe una persona registrada con este RUT.")
        if persona_existente_rut.username == "": # Si la persona no tiene nombre de usuario para login
            print("La persona con este RUT no tiene un nombre de usuario asociado para login.")
            print("Desea crear un nombre de usuario y contrasena para esta persona existente? (s/n)")
            respuesta = input().lower()
            if respuesta == "s": # Si el usuario desea crear credenciales
                username_nuevo = pedir_texto("Ingrese un nombre de usuario: ")
                if buscar_persona_por_username(username_nuevo) is not None: # Verifica si el username ya esta en uso
                    print("Ese nombre de usuario ya esta en uso. Por favor, elija otro.")
                    return # Cancela el registro

                persona_existente_rut.username = username_nuevo # Asigna el nuevo username
                persona_existente_rut.password = pedir_texto("Ingrese una contrasena: ") # Asigna la nueva contrasena

                todas_las_personas = cargar_personas() # Carga todas las personas
                # Busca y actualiza la persona en la lista para guardar los cambios
                for i, p in enumerate(todas_las_personas):
                    if p.rut == persona_existente_rut.rut:
                        todas_las_personas[i] = persona_existente_rut
                        break
                guardar_personas(todas_las_personas) # Guarda la lista actualizada de personas
                print("Nombre de usuario y contrasena creados para la persona existente. Ahora puede iniciar sesion.")
            else:
                print("Registro cancelado.")
        else: # Si la persona ya tiene un nombre de usuario
            print("Esta persona ya tiene un nombre de usuario y contrasena. Por favor, inicie sesion.")
        return # Termina la funcion

    print("No se encontro una persona con este RUT. Se creara un nuevo registro.")
    nombre = pedir_texto("Ingrese su nombre: ")
    apellido = pedir_texto("Ingrese su apellido: ")
    email = pedir_texto("Ingrese su email: ")
    telefono = pedir_texto("Ingrese su telefono: ")
    fecha_nacimiento = pedir_texto("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")
    direccion = pedir_texto("Ingrese su direccion: ")

    username = pedir_texto("Ingrese un nombre de usuario para su login: ")
    if buscar_persona_por_username(username) is not None: # Verifica si el username ya esta en uso
        print("Ese nombre de usuario ya esta en uso. Por favor, elija otro.")
        return # Cancela el registro

    password = pedir_texto("Ingrese una contrasena: ")

    monto_pagado = 0 # Inicializa el monto pagado en 0
    monto_adeudado = 0 # Inicializa el monto adeudado en 0
    es_admin = False # Por defecto, el nuevo usuario no es admin


    # Crea una nueva instancia de Persona con los datos ingresados
    nueva_persona = Persona(rut_ingresado, nombre, apellido, email, telefono, fecha_nacimiento, direccion,
                            monto_pagado, monto_adeudado, username, password, es_admin)

    todas_las_personas_existentes = cargar_personas() # Carga la lista actual de personas
    todas_las_personas_existentes.append(nueva_persona) # Agrega la nueva persona a la lista
    guardar_personas(todas_las_personas_existentes) # Guarda la lista actualizada en el archivo
    print("Registro completado con exito. Ahora puede iniciar sesion.")


def login_usuario():
    """
    Permite a un usuario iniciar sesion en el sistema.
    Valida las credenciales (nombre de usuario y contrasena).
    Si el usuario es administrador, ofrece la opcion de iniciar sesion
    como administrador o como usuario normal.

    Returns:
        Persona or None: El objeto Persona si el login es exitoso,
                         None en caso de credenciales incorrectas o usuario no encontrado.
    """
    print("\n===== INICIO DE SESION =====")
    username = pedir_texto("Nombre de usuario: ") # Solicita el nombre de usuario
    password = pedir_texto("Contrasena: ") # Solicita la contrasena

    persona = buscar_persona_por_username(username) # Busca la persona por el nombre de usuario

    if persona is None: # Si el nombre de usuario no es encontrado
        print("Nombre de usuario no encontrado.")
        return None # Retorna None

    if persona.password != password: # Si la contrasena no coincide
        print("Contrasena incorrecta.")
        return None # Retorna None

    print("Inicio de sesion exitoso! Bienvenido, " + persona.nombre + ".")

    # ---LOGICA SIMPLIFICADA PARA ADMIN ---
    if persona.es_admin: # Si la persona tiene privilegios de administrador
        print("Ha iniciado sesion como un usuario con privilegios administrativos.")
        opcion_rol = pedir_texto("Desea ingresar como (A)dministrador o como (U)suario normal? (A/U): ").lower()

        if opcion_rol == "a": # Si elige 'a' para administrador
            print("Acceso como administrador concedido.")
            return persona  # Retornamos la persona original con es_admin=True
        elif opcion_rol == "u": # Si elige 'u' para usuario normal
            print("Accediendo como usuario normal por eleccion.")
            # Creamos una copia de la persona y modificamos es_admin en la copia para no afectar la original
            persona_para_sesion = Persona(
                persona.rut, persona.nombre, persona.apellido, persona.email, persona.telefono,
                persona.fecha_nacimiento, persona.direccion, persona.monto_pagado, persona.monto_adeudado,
                persona.username, persona.password, False  # es_admin False en la copia
            )
            return persona_para_sesion  # Retornamos la copia como usuario normal
        else: # Si la opcion no es valida, por defecto se accede como usuario normal
            print("Opcion no valida. Accediendo como usuario normal por defecto.")
            persona_para_sesion = Persona(
                persona.rut, persona.nombre, persona.apellido, persona.email, persona.telefono,
                persona.fecha_nacimiento, persona.direccion, persona.monto_pagado, persona.monto_adeudado,
                persona.username, persona.password, False  # es_admin False en la copia
            )
            return persona_para_sesion
    # --- FIN DE LA LOGICA SIMPLIFICADA PARA ADMIN ---

    return persona  # Si no es admin, simplemente retorna la persona tal cual