def guardar_empresa(contenido):
    archivo = open("empresas.txt",'a')
    archivo.write(contenido)
    archivo.close()
    return "Archivo empresas actualizado correctamente..."

class Empresa:
    def __init__(self):
        self.vales = []
    def agregar_vale(self, vale):
        self.vales.append(vale)
        print("Vale agregado exitosamente a la empresa...")
    def imprimir_vales(self):
        for vale in self.vales:
            print(vale)
            print("-"*20)
    def imprimir_mayor_menor(self):
        mayor = ""
        cant_mayor = 0
        menor = ""
        cant_menor = 10000000000000
        for vale in self.vales:
            if vale.monto_total > cant_mayor:
                cant_mayor = vale.monto_total
                mayor = vale
            
            if vale.monto_total < cant_menor:
                cant_menor = vale.monto_total
                menor = vale
        
        print("Rut y Nombre de la empresa con mayor y menor monto total de vales")
        print(mayor)
        print()
        print(menor)
    def visualizar_nombre_monto(self):
        for vale in self.vales:
            print("Nombre:", vale.nombre)
            print("Monto total vales:", vale.monto_total)
            print("-"*10)

class Vale:
    def __init__(self, rut, nombre, tipo, email, direccion, monto_total):
        self.rut = rut
        self.nombre = nombre
        self.tipo = tipo
        self.email = email
        self.direccion = direccion
        self.monto_total = monto_total
    def __str__(self):
        texto = "Datos de la empresa que solicita impresion de vales\n" + \
        "Nombre:" + self.nombre + "\n" +\
        "Tipo:" + self.tipo + "\n" +\
        "Email:" + self.email + "\n" +\
        "Direccion:" + self.direccion + "\n" +\
        "Monto total vales:" + str(self.monto_total)
        return texto
empresa = Empresa()

while True:
    print("SISTEMA DE IMPRESION DE VALES DE ALIMENTACION")
    print("1. Ingresar datos de las empresas que solicitaron impresion de vales")
    print("2. Visualizar datos de las empresas que solicitar impresion de vales")
    print("3. Visualizar RUT y nombre de la empresa con mayor y menor monto total de vales")
    print("4. Visualizar Nombre de empresas y monto total de vales de cada una")
    print("5. Salir del programa")
    opcion = input("Ingrese una opcion (1-5)")
    if opcion == "1":
        rut = input("Ingresa rut: ")
        nombre = input("Ingresa nombre: ")
        tipo = input("Ingresa tipo (natural o juridica): ")
        opciones_validas = ["natural", "juridica"]
        if tipo not in opciones_validas:
            print("Tipo no valido ingrese natural o juridica")
            continue
        email = input("Ingresa email: ")
        direccion = input("Ingresa direccion: ")
        monto_total = float(input("Ingresa monto total: "))
        vale = Vale(rut, nombre, tipo, email, direccion, monto_total)
        empresa.agregar_vale(vale)
        texto = rut +";"+nombre+ ";"+tipo+ ";"+email+";"+direccion+";"+str(monto_total)+"\n"
        print(guardar_empresa(texto))
    elif opcion == "2":
        empresa.imprimir_vales()
    elif opcion == "3":
        empresa.imprimir_mayor_menor()
    elif opcion == "4":
        empresa.visualizar_nombre_monto()
    elif opcion == "5":
        print("Saliendo...")
        break