def ingresar_notas():
    nombre = input("Ingresa tu nombre: ")
    s1 = float(input("Ingresa s1"))
    s2 = float(input("Ingresa s2"))
    c1 = float(input("Ingresa c1"))
    c2 = float(input("Ingresa c2"))
    c3 = float(input("Ingresa c3"))
    t1 = float(input("Ingresa t1"))
    t2 = float(input("Ingresa t2"))
    mic = float(input("Ingresa mic"))
    npe = s1 *0.2 + s2*0.2 +c1*0.025+c2*0.05+c3*0.025+t1*0.2+t2*0.2+mic*0.1
    nf = 0
    ne = 0
    if npe < 5:
        ne = float(input("Ingresa examen"))
        nf = npe*0.7 + ne*0.3
    else:
        nf = npe
    
    if nf > 4:
        estado = "Aprobado"
    else:
        estado = "Reprobado"
    
    texto = nombre + ","+str(s1)+","+str(s2)+","+str(c1)+","+str(c2)+\
            ","+str(c3)+","+str(t1)+","+str(t2)+","+str(mic)+","+str(npe)+\
    ","+str(ne)+","+str(nf)+","+estado+"\n"

    archivo =  open("notas.txt","a")
    archivo.write(texto)
    archivo.close()
    print("Nota ingresa exitosamente!!!")


while True:
    print("Bienvenido")
    print("1. Ingresar notas")
    print("2. Salir")
    opcion = input("Ingresa la opcion (1-2)")

    if opcion == "1":
        ingresar_notas()
    else:
        print("Saliendo...")
        break