def adoptar_mascotas(personas, mascotas):
    """Solicita al usuario su rut, si este usuario existe le mostrara por pantalla 
        todas las mascotas para adoptar
        luego el usuario elige el numero de esa mascota 
        y esa mascota se asignara a su lista.
        Args:
        Personas(list):Lista de las personas
        Mascotas(List):Lista de las mascotas
        """
    rut=input("ingresa tu rut para adoptar una mascota: ")
    persona_registrada=None
    for persona in personas:
        if persona.rut==rut:
            persona_registrada=persona
            break
    if persona_registrada is None:
        print("No se encuentra registrada una persona con ese rut...")
        print("Por favor, registrelo primero")
        return
    if len(mascotas)==0:
        print("No hay mascotas para adoptar")
        return
    print("Mascotas disponibles")
    i=0
    for i in range(len(mascotas)):
        print(str(i+1)+ "." + str(mascotas[i]))   
    op=int(input("Ingrese el numero de la mascota que desea adoptar: "))
    op=op-1
    if op>=0 and op < len(mascotas):
        mascota_elegida=mascotas[op]
        mascota_elegida.adoptante=persona_registrada
        persona_registrada.mascotas.append(mascota_elegida)
        print(persona_registrada.primer_nombre, "adopto a", mascota_elegida.nombre, ".")
    else:
        print("Selecciona una mascota dentro del rango")