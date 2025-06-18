import matplotlib.pyplot as graf 


class Datos_empresa_arrendadora: 
    """
    Clase que permite almacenar datos de una empresa.
    """
    def __init__(self, rut, nombre, telefono, email, direccion):
        """
        Inicializa Datos_empresa_arrendadora.
        Parametros:
        rut (str)
        nombre (str)
        telefono (str)
        email (str)
        direccion (str)
        """
        self.rut = rut
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.direccion = direccion
        
class Datos_personas_arrendatarias:
    """
    Clase que permite almacenar datos de una persona arrendataria.
    """
    def __init__(self, rut, primer_nombre, segundo_nombre, apellido_paterno, apellido_materno, telefono, email, fecha_nacimiento, ingreso_mensual, monto_a_pagar,empresa_arrendada):
        """
        Inicializa Datos_personas_arrendatarias.
        Parametros:
        rut (str)
        primer_nombre (str)
        segundo_nombre (str)
        apellido_paterno (str)
        apellido_materno (str)
        telefono (str)
        email (str)
        fecha_nacimiento (str)
        ingreso_mensual (str)
        monto_a_pagar (int)
        empresa_arrendada(str)
        """
        self.rut = rut
        self.primer_nombre = primer_nombre
        self.segundo_nombre = segundo_nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.telefono = telefono
        self.email = email
        self.fecha_nacimiento = fecha_nacimiento
        self.ingreso_mensual = ingreso_mensual
        self.monto_a_pagar = monto_a_pagar
        self.empresa_arrendada = empresa_arrendada

class Visualizar_datos_empresas_arrendadoras:
    """
    Clase que permite visualizar los datos de una empresa arrendadora.
    """
    def __init__(self,lista_datos_empresa):
        """
        Inicializa con una lista de objetos Datos_empresa_arrendadora.
        Parámetros:
        lista_datos_empresa (lista): Lista de empresas arrendadoras.
        """
        self.lista_datos_empresa = lista_datos_empresa
    def organizar_lista(self):
        """
        Organiza los objetos de la lista y lo guarda en self.datos.
        """
        self.datos = ""
        contador = 1
        for empresa in self.lista_datos_empresa:
            self.datos += "Empresa:" + str(contador) + ", Rut:" + empresa.rut + ", Nombre:"+ empresa.nombre + ", telefono:"+ empresa.telefono + ", Email:" + empresa.email + ", Direccion:" + empresa.direccion + "\n"
            contador += 1
    def __str__(self):
        """
        Retorna:
        str: self.datos
        """
        return self.datos
    
class Visualizar_datos_personas_arrendatarias:
    """
    Clase que permite visualizar los datos de una persona arrendataria.
    """
    def __init__(self, lista_datos_personas):
        """
        Inicializa con una lista de objetos Datos_personas_arrendatarias.
        Parámetros:
        lista_datos_personas (lista): Lista de personas arrendatarias
        """
        self.lista_datos_personas = lista_datos_personas    
    def organizar_lista(self):
        """
        Organiza los objetos de la lista y lo guarda en self.datos
        """
        self.datos = ""
        for personas in self.lista_datos_personas:
            self.datos += "Rut:" + personas.rut + ", Primer nombre:"+ personas.primer_nombre + ", Segundo nombre:"+ personas.segundo_nombre+", Apellido paterno:" +personas.apellido_paterno+", Apellido materno:"+personas.apellido_materno+", Telefono:"+personas.telefono+", Email:"+personas.email+", Fecha de nacimiento:"+personas.fecha_nacimiento+", Ingreso mensual:"+personas.ingreso_mensual+", Monto a pagar (UF):"+str(personas.monto_a_pagar)+", Empresa arrendada:"+personas.empresa_arrendada+"\n"
    def __str__(self):
        """
        Retorna:
        str: self.datos
        """
        return self.datos
    
def grafico_monto_pagar_persona(lista_datos_personas):
    """
    Genera un grafico de barras horizontales con montos a pagar por arrendatario.
    Parametros:
    lista_datos_personas(lista): lista con datos de las personas
    """
    if lista_datos_personas == []:
        print("No ha ingresado valores de personas arrendatarias.")
        print("Primero ingrese datos para luego poder visualizar el grafico.")
        return
    nombres = []
    montos = []
    for i in lista_datos_personas: 
        nombre = i.primer_nombre 
        monto = i.monto_a_pagar
        nombres.append(nombre)
        montos.append(monto)
    graf.figure(figsize=(8,6)) 
    graf.barh(nombres,montos)
    graf.title("Monto a pagar por persona arrendataria")
    graf.xlabel("Monto (UF)")
    graf.ylabel("Nombre")
    graf.show()

lista_datos_empresa = []
lista_datos_personas = []
while True:
    print("Sistema de gestion de arriendos.")
    print("1. Ingresar datos de las empresas arrendadoras.")
    print("2. Ingresar datos de las personas arrendatarias.")
    print("3. Gestion de arriendos. ")
    print("4. Visualizar datos de las personas arrendatarias. ")
    print("5. Visualizar gráfico del monto a pagar de las personas arrendatarias. ")
    print("6. Salir del programa. ")

    opcion = input("Ingrese una opcion (1-6): ") 
    if opcion < "1" or opcion > "6":
        print("No ingreso bien su opcion. Ingrese nuevamente.")
        continue 
    opcion = int(opcion) 

    if opcion == 1: 
        print("Ingresar datos de las empresas arrendadoras.")
        while True:
            rut = input("Ingrese rut (con puntos y con - )(ejemplo: xx.xxx.xxx.-x): ")
            if rut == "":
                print("No puede estar vacio.")
                continue
            else:
                break
        while True:
            nombre = input("Ingrese nombre: ")
            if nombre == "":
                print("No puede estar vacio.")
                continue
            else:
                break
        while True:
            telefono = input("Ingrese telefono: ")
            if telefono == "":
                print("No puede estar vacio.")
                continue
            else:
                break
        while True:
            email = input("Ingrese email: ")
            if email == "":
                print("No puede estar vacio.")
                continue
            else:
                break
        while True:
            direccion = (input("Ingrese direccion: "))
            if direccion == "":
                print("No puede estar vacio.")
                continue
            else:
                break

        d_empresa = Datos_empresa_arrendadora(rut, nombre, telefono, email, direccion)
        lista_datos_empresa.append(d_empresa)
        print("Datos ingresados correctamente.")
    
    elif opcion == 2:
        print(" Ingresar datos de las personas arrendatarias.")
        while True:
            rut = input("Ingrese rut (con punto y con -)(ejemplo: xx.xxx.xxx.-x): ")
            if rut == "":
                print("No puede estar vacio.")
                continue
            else:
                break
        while True:
            primer_nombre = input("Ingrese primer nombre: ")
            if primer_nombre == "":
                print("No puede estar vacio.")
                continue
            else:
                break
        while True:
            segundo_nombre = input("Ingrese segundo nombre: ")
            if segundo_nombre == "":
                print("No puede estar vacio.")
                continue
            else:
                break
        while True:
            apellido_paterno = input("Ingrese apellido paterno: ")
            if apellido_paterno == "":
                print("No puede estar vacio.")
                continue
            else:
                break
        while True:
            apellido_materno = input("Ingrese apellido materno: ")
            if apellido_materno == "":
                print("No puede estar vacio.")
                continue
            else:
                break
        while True:
            telefono = input("Ingrese telefono: ")
            if telefono == "":
                print("No puede estar vacio.")
                continue
            else:
                break
        while True:
            email = input("Ingrese email: ")
            if email == "":
                print("No puede estar vacio.")
                continue
            else:
                break
        while True:
            fecha_nacimiento = input("Ingrese fecha de nacimiento(dia/mes/año): ")
            if fecha_nacimiento == "":
                print("No puede estar vacio.")
                continue
            else:
                break
        while True:
            
            ingreso_mensual = input("Ingrese ingreso mensual: ")
            if ingreso_mensual == "":
                print("No puede estar vacio.")
                continue
            else:
                break
        while True:
            print("El monto a pagar debe estar entre 20UF a 25UF.")
            monto_a_pagar = input("Ingrese monto a pagar(en UF(1UF = 39.207 pesos)) : ")
            if monto_a_pagar == "":
                print("El monto que ingreso esta vacio.")
                print("Ingrese nuevamente.")
                continue
            monto_a_pagar = int(monto_a_pagar)
            if monto_a_pagar >= 20 and monto_a_pagar <= 25: 
                break
            else:
                print("El monto a pagar debe estar entre 20UF a 25UF.")
                print("Ingrese nuevamente.")
                continue
        
        empresa_arrendada = "No has seleccionado empresa arrendadora."
        d_personas= Datos_personas_arrendatarias(rut, primer_nombre, segundo_nombre, apellido_paterno, apellido_materno, telefono, email, fecha_nacimiento, ingreso_mensual, monto_a_pagar,empresa_arrendada)
        lista_datos_personas.append(d_personas)
        print("Datos ingresados correctamente.")

    elif opcion == 3:
        print("Gestion de arriendos. ")
        if lista_datos_empresa == []:
            print("No se puede realizar la gestion de arriendos.")
            print("Primero debe ingresar datos en la opcion 1.")
            continue
        datos_e_a = Visualizar_datos_empresas_arrendadoras(lista_datos_empresa)
        datos_e_a.organizar_lista()
        print(datos_e_a)

        while True:
            ingresa = input("Ingresa tu rut (con punto y con -) (ejemplo: xx.xxx.xxx.-x):")
            nombre = ""
            for persona in lista_datos_personas:
                if ingresa == persona.rut:
                    nombre = persona.primer_nombre
                    break
            if nombre == "":
                print("No se encontró una persona con ese RUT. Ingrese de la misma manera que lo ingreso en la opcion 2.")
                continue
            else:
                break
        
        print("Hola",nombre, "estas son las empresas disponibles.")
        contador = 1 
        for empresa in lista_datos_empresa:
            print(str(contador)+". "+empresa.nombre)
            contador += 1
        cantidad_empresa = len(lista_datos_empresa)

        while True:
            opcion_empresa = input("Elige el numero de empresa con la que quieres arrendar:")
            if opcion_empresa == "":
                print("No arrendo con ninguna empresa.")
                break
            opcion_empresa = int(opcion_empresa)
            if opcion_empresa < 1 or opcion_empresa > cantidad_empresa:
                print("Numero de empresa ingresado incorrecto.")
                continue
            
            empresa_seleccionada = lista_datos_empresa[opcion_empresa-1]
            for persona in lista_datos_personas:
                if persona.rut == ingresa:
                    persona.empresa_arrendada = empresa_seleccionada.nombre
                    break
            break

    elif opcion == 4:
        print(" Visualizar datos de las personas arrendatarias. ")
        if lista_datos_personas == []:
            print("No se puede visualizar ningun dato ya que no ha ingresado los datos.")
            print("Seleccione la opcion 2 para ingresar los datos.")
            continue
        datos_p_a = Visualizar_datos_personas_arrendatarias(lista_datos_personas)
        datos_p_a.organizar_lista()
        print(datos_p_a)

    elif opcion == 5:
        print(" Visualizar gráfico del monto a pagar de las personas arrendatarias. ")
        grafico_monto_pagar_persona(lista_datos_personas)

    elif opcion == 6:
        print("Finalizando el programa......")
        break
print("Programa finalizado.")
