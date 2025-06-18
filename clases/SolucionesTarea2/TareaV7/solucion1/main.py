       
from Estudiantes import Estudiante
from empresa import Empresario
from empresa_creacion import Empresa
from graficouf import graficoUF

print("\nBienvenidos al menu de contrato")

lista_empresas = []
lista_estudiantes = []
estudiante_encontrado = None

while True:
    print("-------------------------------------------------------------------------------")
    print("1.- Ingresar datos de las empresas que contratan")
    print("2.- Ingresar datos de los/las estudiantes contratado(a)s")
    print("3.- Vinculacion de contrato")
    print("4.- Desvinculacion de contrato ")
    print("5.- Visualizar datos de las empresas que contratan")
    print("6.- Visualizar datos de los/las estudiantes contratado(a)s")
    print("7.- Visualizar gráfico del salario líquido de los/las estudiantes contratados")
    print("8.- Salir del programa")
    print("-------------------------------------------------------------------------------")

    opcion=input("Selecciona una opcion (1/8): ")
   
    while True:
        if opcion == "1":
            print("----------Menu de contrato--------")
            print("1.- agregar empresa")
            print("2.- mostrar datos de la/las empresas")
            print("3.- editar una empresa")
            print("4.- volver al menu principal")
            print("----------------------------------\n")

            eleccion=input("seleccione 1/4: ")
       
       
            if eleccion == "1":
                rutt = input("RUT de la empresa: ")
                nombre = input("Nombre de la empresa: ")
                telefono = input("Teléfono de contacto: ")
                emaill = input("Email de contacto: ")
                direccion = input("Dirección: ")
                empresa = Empresa(rutt, nombre, telefono, emaill, direccion)
                lista_empresas.append(empresa)
                print("Empresa creada exitosamente...\n")
                     
            elif eleccion == "2":
              for empresa in lista_empresas:
                  empresa.mostrar_datosdeempresa()

            elif eleccion == "3":
                if len(lista_empresas) == 0:
                    print("no hay empresas seleccionadas porfavor reanude el progreso..")
                    break
                else:
                    print("\nEmpresas Disponibles:")
                    contador = 1
                    for empresa in lista_empresas:
                        print(str(contador) + empresa.nombre + " RUT: " + empresa.rutt)      
                        contador += 1
                    
                    while True:
                        seleccion_editar = input("Seleccione el numero de las empresas para editar, (0 para salir del procedimiento): ")
                        
                        if seleccion_editar == "0":
                            break
                        
                        elif seleccion_editar.isdigit():
                            seleccion_editar = int(seleccion_editar)
                            
                            if seleccion_editar > 0 and seleccion_editar <= len(lista_empresas):
                                editar_empresa =lista_empresas[seleccion_editar - 1]
                                print("\nEditando la empresa: " + editar_empresa.nombre)
                                
                                while True:
                                    print("\n¿Qué datos desea modificar?")
                                    print("-----------------------------")
                                    print("1. Nombre")
                                    print("2. RUT")
                                    print("3. Teléfono")
                                    print("4. Email")
                                    print("5. Dirección")
                                    print("6. Volver al menu")
                                    print("-----------------------------")
                                    
                                    editar_opcion = input("Seleccione una opcion (1/6): ")
                                    
                                    if editar_opcion == "1":
                                        nombre_nuevo = input("Ingrese el nuevo nombre de empresa: ")
                                        editar_empresa.nombre = nombre_nuevo
                                        print("Nombre actualizado\n")
                                            
                                    elif editar_opcion == "2":
                                        rut_nuevo = input("Ingrese el nuevo RUT de empresa: ")
                                        while rut_nuevo.isdigit() == False:
                                            print("Error, no puedes poner letras en el RUT solo numero de 9 digitos")
                                            rut_nuevo = input("Ingrese de nuevo el nuevo RUT de la empresa: ")        
                                        editar_empresa.rutt = rut_nuevo
                                        print("RUT actualizado\n")
                                    
                                    elif editar_opcion == "3":
                                        telefono_nuevo = input("Ingrese el nuevo numero telefonico de la empresa: ")
                                        while telefono_nuevo.isdigit() == False:
                                            print("Error, no puedes poner letras en el numero telefonico, solo numero de 9 digitos")
                                            telefono_nuevo = input("Ingrese de nuevo el nuevo numero telefonico de la empresa: ")
                                        editar_empresa.telefono = telefono_nuevo
                                        print("Telefono actualizado\n")
                                        
                                    elif editar_opcion == "4":
                                        email_nuevo = input("Ingrese el nuevo Email de la empresa: ")
                                        editar_empresa.emaill = email_nuevo
                                        print("Email actualizado\n")
                                        
                                    elif editar_opcion == "5":
                                        direccion_nueva = input("Ingrese la nueva direccion de la empresa: ")
                                        editar_empresa.direccion = direccion_nueva
                                        print("Direccion de la empresa actualizada\n")
                                        
                                    elif editar_opcion == "6":
                                        print("Saliendo del proceso de editar...")
                                        break

            elif eleccion == "4":
                print("\nvolviendo al menu principal\n")
                break
                   
        elif opcion=="2":
            print("\n----Menu de contrato de estudiantes----")
            print("1.- agregar a estudiante")
            print("2.- mostrar datos de estudiante")
            print("3.- editar a estudiante")
            print("4.- volver al menu principal")
            print("-----------------------------------------\n")
            
            eleccion=input("seleccione 1/4: ")

            if eleccion == "1":
                primer_nombre=input("ingresa tu primer nombre: ")
                segundo_nombre=input("ingresa tu segundo nombre: ")

                apellidop=input("ingresa tu apellido Paterno: ")
                apellidom=input("ingresa tu apellido Materno: ")

                rut=input("ingresa tu RUT: ")
                while rut.isdigit() == False:
                    rut = input("ERROR, debes ingresar tu RUT de 8 o 9 digitos")

                numeroT = input("ingresa tu numero de telefono: ")

                while numeroT.isdigit() == False:
                    numeroT = input("ERROR, debe ingresar tu numero de telefono de 9 digitos: ")

                email=input("ingresa tu email: ")

                fda=input("ingresa tu Fecha de Nacimiento(DD.MM.AA): ")

                salarioL=input("ingresa tu Salario Liquido en UF (10/15): ")
                while salarioL.isdigit() == False:
                    salarioL=input("ERROR, debes ingresar tu Salario Liquido en UF entre (10/15) UF: ")
                while salarioL < "10" or salarioL > "15":
                    salarioL=input("ERROR, debes ingresar tu Salario Liquido en el rango de 10 a 15 UF : ")

                carrera=input("ingresa tu Carrera que estudias: ")

                universidad=input("ingresa tu Universidad en el que estudias: ")

                semestreactual=input("ingresa tu semestre actual del (1 al 7): ")

                while semestreactual not in "1" and semestreactual not in "2" and semestreactual not in "3" and semestreactual not in "4" and semestreactual not in "5" and semestreactual not in "6" and semestreactual not in "7":
                        print("error, debes responder con la condicion del (1 al 7): ")
                        semestreactual=input("ingresa tu semestre actual del (1 al 7): ")

                estudiante = Estudiante(primer_nombre,segundo_nombre,apellidop, apellidom, rut, numeroT, email, fda, salarioL, carrera, universidad, semestreactual)
                lista_estudiantes.append(estudiante)

            elif eleccion == "2":
                for estudiante in lista_estudiantes:
                    estudiante.mostrar_informacion()
         
            elif eleccion == "3":
                if len(lista_estudiantes) == 0:
                    print("No hay estudiantes registrados, porfavor reanude el progreso..")
                    break
                else:
                    print("\nEstudiantes disponibles")
                    contador = 1
                    for estudiantes in lista_estudiantes:
                        print(str(contador) + ". " + estudiante.primer_nombre + " " + estudiante.apellidop + " " + estudiante.apellidom + " RUT: " + estudiante.rut)
                        contador +=1
                        
                    while True:
                        seleccion_editar = input("Seleccione el numero de los estudiantes para editar, (0 para salir del procedimiento): ")
                        
                        if seleccion_editar == "0":
                            break
                        
                        elif seleccion_editar.isdigit():
                            seleccion_editar = int(seleccion_editar)
                            
                            if seleccion_editar > 0 and seleccion_editar <= len(lista_estudiantes):
                                editar_estudiante =lista_estudiantes[seleccion_editar - 1]
                                print("\nEditando el estudiante " + editar_estudiante.nombre)
                                
                                while True:
                                    print("\n¿Qué dato desea modificar?")
                                    print("-----------------------------")
                                    print("1. Nombres")
                                    print("2. Apellidos")
                                    print("3. RUT")
                                    print("4. Teléfono")
                                    print("5. Email")
                                    print("6. Fecha de nacimiento")
                                    print("7. Salario líquido")
                                    print("8. Carrera")
                                    print("9. Universidad")
                                    print("10. Semestre")
                                    print("11. Volver")
                                    print("-----------------------------")
                                    
                                    editar_opcion = input("Seleccione una opcion (1/6): ")
                                    
                                    if editar_opcion == "1":
                                        primer_nombre_nuevo = input("Ingrese el nuevo Primer nombre de empresa: ")
                                        segundo_nombre_nuevo = input("Ingrese el nuevo Segundo nombre de empresa: ")
                                        editar_estudiante.primer_nombre = primer_nombre_nuevo
                                        editar_estudiante.segundo_nombre = segundo_nombre_nuevo
                                        print("Los Nombres han sido actualizados\n")
                                        
                                    elif editar_opcion == "2":
                                        primer_apellido_nuevo =input("Ingrese su nuevo Apellido Paterno: ")
                                        segundo_apellido_nuevo =input("Ingrese su nuevo Apellido Materno: ")    
                                        editar_estudiante.apellidop = primer_apellido_nuevo
                                        editar_estudiante.apellidom = segundo_apellido_nuevo
                                        print("Los apellidos han sidos cambiados exitosamente....\n")
                                        
                                    elif editar_opcion == "3":
                                        rut_nuevo = input("Ingrese el nuevo RUT del Estudiante: ")
                                        while rut_nuevo.isdigit() == False:
                                            print("Error, no puedes poner letras en el RUT, solo numero de 9 digitos")
                                            rut_nuevo = input("Ingrese de nuevo el nuevo RUT del estudiante: ")        
                                        editar_estudiante.rut = rut_nuevo
                                        print("RUT actualizado\n")
                                    
                                    elif editar_opcion == "4":
                                        telefono_nuevo = input("Ingrese el nuevo numero telefonico del estudiante: ")
                                        while telefono_nuevo.isdigit() == False:
                                            print("Error, no puedes poner letras en el numero telefonico, solo numero de 9 digitos")
                                            telefono_nuevo = input("Ingrese de nuevo el nuevo numero telefonico de la empresa: ")
                                        editar_empresa.telefono = telefono_nuevo
                                        print("Telefono actualizado\n")
                                        
                                    elif editar_opcion == "5":
                                        email_nuevo = input("Ingrese el nuevo Email del estudiante: ")
                                        editar_empresa.emaill = email_nuevo
                                        print("El Email del Estudiante se ha actualizado\n")
                                        
                                    elif editar_opcion == "6":
                                        fda_nueva = input("Ingrese la nueva Fecha de nacimiento del Estudiante (dd/mm/aa): ")
                                        editar_estudiante.fda = fda_nueva
                                        print("la Fecha de nacimiento se ha actualizado\n")
                                         
                                    elif editar_opcion == "7":
                                        salarioUF_nuevo= input("ingresa el nuevo Salario Liquido del estudiante en UF (10/15): ")
                                        while salarioUF_nuevo.isdigit() == False:
                                            print("ERROR, debes ingresar tu Salario Liquido en UF entre (10/15) UF: ")
                                            salarioUF_nuevo= input("ingresa tu nuevo Salario Liquido en UF (10/15): ")
                                        while salarioUF_nuevo < "10" or salarioUF_nuevo > "15":
                                            print("ERROR, debes ingresar tu Salario Liquido en el rango de 10 a 15 UF : ")
                                            salarioUF_nuevo= input("ingresa tu nuevo Salario Liquido en UF (10/15): ")
                                        editar_estudiante.salarioL = salarioUF_nuevo
                                        print("El salario liquido del estudiante fue actualizadoo\n")
                                        
                                    elif editar_opcion == "8":
                                        carrera_nueva = input("Ingrese la nueva carrera del estudiante: ")
                                        editar_estudiante.carrera = carrera_nueva
                                        print("Carrera nueva actualizada\n")
                                
                                    elif editar_opcion == "9":
                                        universidad_nueva = input("Ingrese la nueva universidad del estudiante: ")
                                        editar_estudiante.universidad = universidad_nueva
                                        print("Universidad nueva actualizada")
                                        
                                    elif editar_opcion == "10":
                                        semestre_nuevo = input("Ingrese el nuevo semestre del estudiante del (1 al 7): ")
                                        while semestre_nuevo not in "1" and semestre_nuevo not in "2" and semestre_nuevo not in "3" and semestre_nuevo not in "4" and semestre_nuevo not in "5" and semestre_nuevo not in "6" and semestre_nuevo not in "7":
                                            print("error, debes responder con la condicion del (1 al 7): ")
                                            semestre_nuevo=input("Ingrese el nuevo semestre del estudiante del (1 al 7): ")
                                        editar_estudiante.semestreactual = semestre_nuevo
                                        print("Semestre actualizado\n")
                                        
                                    elif editar_opcion == "11":
                                        print("Saliendo del proceso de editar...")
                                        break
                        
            elif eleccion == "4":
                print("volviendo al menu principal\n")
                break
           
        elif opcion=="3":    
            print("")
            rut_estudiante = input("Ingrese el RUT del estudiante: ")
            for estudiante in lista_estudiantes:
                if estudiante.rut == rut_estudiante:
                    estudiante_encontrado = estudiante
                    break
            if estudiante_encontrado == None:
                print("El o los estudiantes no estan registrados, porfavor ir a la opcion 2\n")
                break
            else:
                if estudiante_encontrado.empresa:
                    print("El estudiante ya esta contratado por una empresa " + estudiante_encontrado.empresa.nombre)
                    break
                else:
                    print("Empresas disponibles")
                    contador = 1
                    for empresa in lista_empresas:
                        print(str(contador) + ". " + empresa.nombre + (" Rut: " + empresa.rutt))
                        contador += 1
                        
                    while True:
                        eleccion_empresa = input("\nSeleccione una empresa: ")
                        if eleccion_empresa.isdigit() == False:
                            print("Error, solo puede poner numeros")
                        else:
                            eleccion_empresa = int(eleccion_empresa)
                            if eleccion_empresa >= 1 and eleccion_empresa <= len(lista_empresas):
                                empresa_seleccionada = lista_empresas[eleccion_empresa - 1]
                                break
                    estudiante_encontrado.generar_contrato(empresa_seleccionada)   
                    print("Contrato generado exitosamente de " + estudiante_encontrado.primer_nombre + " vinculado a la empresa " + empresa_seleccionada.nombre)
                    break 

        elif opcion=="4":
            print("Desvinculacion de contrato")
            rut_estudiante = input("Ingrese el RUT del estudiante para la desvinculacion")
            for estudiante in lista_estudiantes:
                if estudiante.rut == rut_estudiante:
                    estudiante_encontrado = estudiante
                    break
            if estudiante_encontrado is None:
                print("El estudiante o los estudiantes no estan registrados, porfavor ir a opcion 2")
            else:
                if not estudiante_encontrado.empresa:
                    print("El estudiante no tiene contrato activo")
                else:
                    empresa_asociada = estudiante_encontrado.empresa
                    for estudiante_empresa in empresa_asociada.estudiantes:
                        if estudiante_empresa.rut == rut_estudiante:
                            empresa_asociada.estudiantes.remove(estudiante_empresa)
                            break
                    estudiante_encontrado.empresa = ""
                    print("Desvinculacion hecho correctamentee")
                    print("El estudiante " + estudiante_encontrado.primer_nombre + " ya no esta trabajando en la empresa " + empresa_asociada.nombre)
                    break
                break
            break
               
        elif opcion=="5":    
            print("\nDatos de las empresas contratantes\n")
            
            if len(lista_empresas) ==0:
                print("no hay empresas registradas, porfavor ir a la opcion (1) para agregar\n")
                break
            else:
                contador = 1
                for empresa in lista_empresas:
                    print("\nEmpresa N " + str(contador))
                    empresa.mostrar_datosdeempresa()
                    print("-------------------------------------------")
                    contador += 1
                input("\nAprete la tecla Enter para continuar")
                break
                
        elif opcion=="6":    
            print("\nDatos de los estudiantes contratados")
            
            if len(lista_estudiantes) == 0:
                print("No hay estudiantes registrados, Porfavor usar al opcion (2) para avanzar")
                break
            else:
                contador = 1
                for estudiantes in lista_estudiantes:
                    print("\nEstudiante N " + str(contador))
                    estudiante.mostrar_informacion()
                        
                    if estudiante.empresa:
                        print("Empresa contratante: " + estudiante.empresa.nombre)
                    else:
                        print("Empresa contratante: Ningun contrato activo")
                    
                    print("-------------------------------------------")
                    contador += 1
                input("\nAprete la tecla Enter para continuar")
                break

        elif opcion=="7":    
            if len(lista_estudiantes) == 0:
                print("No hay estudiantes registrados, Porfavor usar al opcion (2) para avanzar")
                break
            else:
                import matplotlib.pyplot as plt
                Grafico = graficoUF(lista_estudiantes)
                Grafico.sacar_datos()
                Grafico.generarUF()   
            break
       
        elif opcion=="8":    
            print("Saliendo del programa")
            break