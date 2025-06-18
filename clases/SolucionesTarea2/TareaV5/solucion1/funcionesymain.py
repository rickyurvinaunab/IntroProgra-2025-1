import matplotlib.pyplot as plt

class Medicamento:
    def __init__(self, nombre, componente, laboratorio, marca, tipo, precio):
        self.nombre = nombre
        self.componente = componente
        self.laboratorio = laboratorio
        self.marca = marca
        self.tipo = tipo
        self.precio = precio

    def __str__(self):
        return "Nombre: " + self.nombre + ", Componente: " + self.componente + ", Laboratorio: " + self.laboratorio + ", Marca: " + self.marca + ", Tipo: " + self.tipo + ", Precio: $" + str(self.precio)

class Farmacia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.medicamentos = []

    def agregar_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)

    def __str__(self):
        return "Farmacia: " + self.nombre

class Persona:
    def __init__(self, rut, nombre, segundo_nombre, apellido_paterno, apellido_materno):
        self.rut = rut
        self.nombre = nombre
        self.segundo_nombre = segundo_nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.medicamentos_comprados = []  

    def agregar_compra(self, medicamento, farmacia):
        self.medicamentos_comprados.append((medicamento, farmacia))

    def monto_total(self):
        total = 0
        for posicion in self.medicamentos_comprados:
            medicamento = posicion[0] 
            total = total + medicamento.precio
            return total

    def __str__(self):
        return "RUT: " + self.rut + ", Nombre: " + self.nombre + " " + self.segundo_nombre + " " + self.apellido_paterno + " " + self.apellido_materno + ", Monto a pagar: $" + str(self.monto_total())

def menu():
    print("Gestión de Medicamentos")
    print("1. Ingresar farmaca")
    print("2. Ingresar datos de los medicamentos a una farmacia")
    print("3. Ingresar datos de las personas que compran y registrar compra")
    print("4. Visualizar datos de los medicamentos por farmacia")
    print("5. Visualizar datos de las personas que compran")
    print("6. Visualizar medicamentos comprados por persona")
    print("7. Visualizar gráfico del monto a pagar por las personas que compraron medicamentos")
    print("8. Salir del programa")
    return input("Seleccione una opción: ")

def seleccionar_farmacia(farmacias):
    if not farmacias:
        print("No hay farmacias registradas.")
        return
    print("Seleccione una farmacia:")
    while True:
        print("Seleccione una farmacia:")
        for f in range(len(farmacias)):
            print(str(f+1) + ". " + farmacias[f].nombre)
        opcion = input("Escriba un número: ")

        if int(opcion) >= 1 and int(opcion) <= len(farmacias):
            return farmacias[int(opcion) - 1]
        else:
            print("Opción inválida. Intente de nuevo.")

def crear_farmacia(farmacias):
    print("ingresar farmacia")
    nombre = input("Nombre de la farmacia: ")
    farmacias.append(Farmacia(nombre))
    print("Farmacia agregada.")

def ingresar_medicamento():
    print("Ingreso de Medicamento")
    nombre = input("Nombre: ")
    componente = input("Componente principal: ")
    laboratorio = input("Laboratorio: ")
    marca = input("Marca: ")
    tipo = input("Tipo (capsula, suspensión, inyección): ")
    while True:
        precio = input("Precio: ")
        precio = float(precio)
        if precio < 0:
            print("Precio inválido. Debe ser un número positivo.")
        else:
            break
    return Medicamento(nombre, componente, laboratorio, marca, tipo, precio)

def ingresar_persona():
    print("Ingreso de Persona")
    rut = input("RUT: ")
    nombre = input("Primer nombre: ")
    segundo_nombre = input("Segundo nombre: ")
    apellido_paterno = input("Apellido paterno: ")
    apellido_materno = input("Apellido materno: ")
    return Persona(rut, nombre, segundo_nombre, apellido_paterno, apellido_materno)

def registrar_compra(persona, farmacias):
    if not farmacias:
        print("No hay farmacias registradas.")
        return
    print("Seleccione la farmacia de donde desea comprar:")
    farmacia = seleccionar_farmacia(farmacias)
    if len(farmacia.medicamentos) == 0:
        print("No hay medicamentos en esta farmacia.")
        return
    print("Medicamentos disponibles:")
    for far in range(len(farmacia.medicamentos)):
        print(str(far+1) + ". " + str(farmacia.medicamentos[far]))
    medcomprados = []
    while True:
        nummedicamento = input("Ingrese el número del medicamento a comprar (o ENTER para terminar): ")
        if nummedicamento == "":
            break
        numedi = int(nummedicamento)
        if 1 <= numedi <= len(farmacia.medicamentos):
            medcomprados.append(farmacia.medicamentos[numedi - 1])
        else:
            print("Número inválido.")
    for med in medcomprados:
        persona.agregar_compra(med, farmacia)
    if medcomprados:
        print("Compra registrada.")
    else:
        print("No se seleccionaron medicamentos.")

def visualizar_medicamentosfarmacias(farmacias):
    print("Medicamentos por farmacia")
    if not farmacias:
        print("No hay farmacias registradas.")
        return
    for farmacia in farmacias:
        print(farmacia.nombre + ":")
        if not farmacia.medicamentos:
            print("No hay medicamentos registrados.")
        for med in range(len(farmacia.medicamentos)):
            print("  " + str(med+1) + ". " + str(farmacia.medicamentos[med]))

def visualizar_personas(personas):
    print("Lista de personas que compran")
    if not personas:
        print("No hay personas registradas.")
    for per in range(len(personas)):
        print(str(per+1) + ". " + str(personas[per]))

def visualizar_medicamentosporpersona(personas):
    print("Medicamentos comprados por persona")
    if not personas:
        print("No hay personas registradas.")
        return
    for per in range(len(personas)):
        persona = personas[per]
        print(str(per+1) + ". " + persona.nombre + " " + persona.apellido_paterno + " " + persona.apellido_materno + " (RUT: " + persona.rut + ")")
        if not persona.medicamentos_comprados:
            print("No ha comprado medicamentos.")
        else:
            medd = 0
            while medd < len(persona.medicamentos_comprados):
                print(persona.medicamentos_comprados[medd][0].nombre + " ($" + str(persona.medicamentos_comprados[medd][0].precio) + ") en " + persona.medicamentos_comprados[medd][1].nombre)
                medd = medd + 1

def graficar_montos(personas):
    print("Gráfico de montos a pagar")
    if not personas:
        print("No hay datos para graficar.")
        return
    nombres = []
    montos = []
    for p in personas:
        nombres.append(p.nombre + " " + p.apellido_paterno)
        montos.append(p.monto_total())
    plt.figure(figsize=(10, 5))
    plt.bar(nombres, montos, color='slateblue')
    plt.xlabel('Personas')
    plt.ylabel('Monto a pagar ($)')
    plt.title('Monto a pagar por personas que compraron medicamentos')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def main():
    farmacias = []
    personas = []
    while True:
        opcion = menu()
        if opcion == "1":
            crear_farmacia(farmacias)
        elif opcion == "2":
            if not farmacias:
                print("Primero debe crear una farmacia.")
            else:
                farmacia = seleccionar_farmacia(farmacias)
                if farmacia:
                    medicamento = ingresar_medicamento()
                    farmacia.agregar_medicamento(medicamento)
                    print("Medicamento agregado a la farmacia.")
        elif opcion == "3":
            persona = ingresar_persona()
            registrar_compra(persona, farmacias)
            personas.append(persona)
        elif opcion == "4":
            visualizar_medicamentosfarmacias(farmacias)
        elif opcion == "5":
            visualizar_personas(personas)
        elif opcion == "6":
            visualizar_medicamentosporpersona(personas)
        elif opcion == "7":
            graficar_montos(personas)
        elif opcion == "8":
            print("Saliendo")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
main() 

