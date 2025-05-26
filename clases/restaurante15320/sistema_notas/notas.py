
def ingresar_nota():
    nombre = input("Ingresa tu nommbre: ")
    s1 = float(input("Ingresa tu nota s1: "))
    s2 = float(input("Ingresa tu nota s2: "))
    c1 = float(input("Ingresa tu nota c1: "))
    c2 = float(input("Ingresa tu nota c2: "))
    c3 = float(input("Ingresa tu nota c3: "))
    t1 = float(input("Ingresa tu nota t1: "))
    t2 = float(input("Ingresa tu nota t2: "))
    mic = float(input("Ingresa tu nota del curso de MIC"))
    npe = 0.2*s1 + 0.2*s2 + 0.025*c1  +0.05*c2 + 0.025*c3 + 0.1*mic + 0.2*t1 + 0.2*t2
    ne = 0
    nf = 0
    if npe>=5:
        nf = npe
    else:
        ne = float(input("Ingresa la nota del examen"))
    nf = npe*0.7 + ne*0.3
    estado = ""
    if nf>=4:
        estado = "Aprobado"
    else:
        estado ="Reprobado"

    item = nombre + ","+str(s1)+","+str(s2)+","+str(c1)+ \
    ","+str(c2)+","+str(c3)+","+str(t1)+","+str(t2)+","+ \
    str(mic)+","+str(npe)+","+str(ne)+","+str(nf)+","+estado+"\n"

    archivo = open('notas.txt','a')
    archivo.write(item)
    archivo.close()
    print("Nota guardada exitosamente...")


def mostrar_cant_aprobados():

    archivo = open('notas.txt','r')
    contenido = archivo.readlines()
    aprobados = 0
    reprobados = 0
    for linea in contenido:
        datos = linea.strip().split(',')
        if datos[-1] == "Aprobado":
            aprobados += 1
        else:
            reprobados += 1
    
    print("Hay "+ str(aprobados)+ " aprobados y " + str(reprobados) + " reprobados")

    
opcion = ""


while opcion == "":
    print("Bienvenido")
    print("1. Ingresar notas")
    print("2. Mostrar resultados")
    print("3. Salir")

    opcion = input("ingresa la opcion (1-2): ")
    if opcion == "1":
        ingresar_nota()
    elif opcion == "2":
        mostrar_cant_aprobados()

    elif opcion == "3":
        break

    opcion = ""