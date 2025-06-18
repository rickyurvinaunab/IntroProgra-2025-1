from clases import Empresa
from clases import Estudiante
from clases import Datos

def menu():
    """
    creo una funcion que al llamarma imprimira el menu del sistema
    """
    print("============================================================")
    print("               menu de gestion de practicas                ")
    print("============================================================")
    print("|DATOS|")
    
    print("1-Ingresar datos de las empresas que contratan")
    print("2-Ingresar datos de los/las estudiantes")
    print("|VISUALIZACION DE DATOS|")
 
    print("3-Visualiar datos de las empresas que contratan")
    print("4-Visualiar datos de los/las estudiantes que postulan")
    print("|CONTRATOS|")
    
    
    print("5-proceso de contratos")
    print("|RESULTADOS DE LAS POSTULACIONES|")
  
    print("6-Visualizar datos de los/las estudiantes contratado(a)s")
    print("7-Visualizar datos de los/las estudiantes no contratado(a)s")
    print("|GRAFICOS|")
   
    print("8-Visualizar grafico del salario liquido de los/las contratado(a)s")
    print("9-visualizar grafico personalizado de las empresas")
    print(" ")
    
    print("10-Salir del programa")
    print("===========================")
    
    
def crear_datos_empresa():
    """
    creo una funcion que al llamarma me pedira los atributos que se agregaran a la clase Empresa, tambien agrego ese objeto a la base de datos para asi guardar todas las empresas registradas en una lista
    """
    rut_empresa=input("Ingrese el rut de la empresa:")
    nombre_empresa=input("Ingrese el nombre de la empresa:")
    phono_empresa=input("Ingrese el phono de la empresa:")
    email_empresa=input("Ingrese el email de la empresa:")
    direccion_empresa=input("Ingrese la direccion de la empresa")
    
   
    
    empresa_asignada=Empresa(rut_empresa,nombre_empresa,phono_empresa,email_empresa,direccion_empresa)
    datos.agregar_datos_empresa(empresa_asignada)
  
    print("Datos de la empresa guardados exitosamente......")
    
    
def crear_datos_estudiante():
    """
    creo una funcion que al llamarma me pedira los atributos que se agregaran a la clase Estudiante y tambien se valida mediante un while que el semestre que ingrese sea mayor aa 1 y menor a 15 semestres para poder hacer mas realista
    la postulacion, esto se hace en un while,porque no se cuantas veces se equivoque el usuario, para finalizar agregando el obejto a la datos
    """
    rut_estudiante=input("ingrese el rut del estudiante:")
    primer_nombre=input("ingrese el primer nombre del estudiante:")
    segundo_nombre=input("ingrese el segundo nombre del estudiante:")
    apellido_paterno=input("ingrese el apellido paterno del estudiante:")
    apellido_materno=input("ingrese el apellido materno del estudiante:")
    phono_estudiante=input("ingrese el phono del estudiante:")                                                                                                                                            
    email_estudiante=input("ingrese el email del estudiante:")                                                                                                   
    fecha_nacimiento=input("ingrese la fecha de nacimiento del estudiante en formato(dd/mm/aa):")
    carrera=input("ingrese la carrera del estudiante:")
    universidad=input("ingrese la universidad  del estudiante:")
    semestre_actual=int(input("ingrese el semestre actual del estudiante:"))
    while True:
        if semestre_actual<1:
            print("-----no existe un semestre menor a 1------ingrese un numero de semestre valido------")
            semestre_actual=int(input("ingrese el semestre actual del estudiante:"))
            
        elif semestre_actual>15:
            print("-----ingrese un semestre menor a 15----por lo general usted ya tiene titulo pasado esos semestres-----")
            semestre_actual=int(input("ingrese el semestre actual del estudiante:")) 
        else:
            break
            
    estudiante_postulante=Estudiante(rut_estudiante,primer_nombre,segundo_nombre,apellido_paterno,apellido_materno,phono_estudiante,email_estudiante,fecha_nacimiento,carrera,universidad,semestre_actual)
    datos.agregar_datos_estudiante(estudiante_postulante)
    print("Datos del estudiante guardados exitosamente.......")
    

def escoger_contrato():
    """
    se crea la funcion para que el estudiante pueda escoger su contratp ingresando  su sut correspondiente, se valida que el rut ingresado exista primero definiendo con None estudiante, ya que esto me sirve
    poque con un for yo accedo a los objetos que tiene datos._estudiante y  como es un objeto estudiante puedo acceder a su rut y al momento que el rut ingresado sea igual al rut del estuidante se cambia 
    el None por el objeto estudiante, no por su rut si no por el estudiante en si y los dos ciclos terminan, pero si me ingresa un incorrecto  y estudiante sigue siendo None, se le dice que el rut no fue encontrado 
    y se le vuelve a pedir hasta que lo escriba bien, luego yo como fuarde el obejto estudiante accedo a su semestre y si es mayor a 5  si puede ser contratado y le pido que ingrese una empresa de las que hay y lo 
    valido con la misma logica anterior, para asi hacer el contrato, agregarlo a estuidantes contratados y sacarlo de datos estudiantes,porque el ya esta contratado
    
    """
    
    rut=input("|ingrese el rut del estudiante:")
    estudiante=None
    empresa=None
    while True:
        
        for dato in datos.datos_estudiante:
            
            if rut==dato.rut_estudiante:
                
               estudiante=dato
               break
        if estudiante is None:
            
            print("|ESTUDIANTE  NO ENCONTRADO|INGRESE UN RUT CORRECTO")
            rut=input("|ingrese el rut del estudiante:")
            
        else:
            break
        
    if estudiante.semestre_actual>5:
            
        print( "ESTUDIANTE:" + estudiante.primer_nombre +" " +estudiante.segundo_nombre  +" "  + estudiante.apellido_paterno +" " +estudiante.apellido_materno)
        print("empresas disponibles para postular")
        indice=0
        for dato in datos.datos_empresa:
                
            indice+=1
            print( str(indice)+ "|" + dato.nombre_empresa)
            
        escoger=input("ingrese el nombre de la empresa que mas le interesaria ser contratado:")
        while True:
            
            for dato in datos.datos_empresa:
                
                if escoger==dato.nombre_empresa:
                    empresa=dato
                    break
                
            if empresa is None:
                
                print("|EMPRESA  NO ENCONTRADA|INGRESE UN NOMBRE CORRECTO")
                escoger=input("ingrese el nombre de la empresa que mas le interesaria ser contratado:")
                    
            else:
                break
        datos.datos_contratados.append(estudiante)
        datos.datos_estudiante.remove(estudiante)
                    
                
    
        for dato in datos.datos_empresa:
            
            if escoger==dato.nombre_empresa:
                empresa=dato
                break
            
        estudiante.realizar_contrato(empresa)
        x= "|" + "RUT:" + estudiante.rut_estudiante + "|" + "NOMBRE:" + estudiante.primer_nombre + " " + estudiante.segundo_nombre  + " "  + estudiante.apellido_paterno + " " + estudiante.apellido_materno + "|" + "EMPRESA:" + empresa.nombre_empresa

    

    elif  estudiante.semestre_actual<5:
        x=estudiante.primer_nombre + " " + estudiante.segundo_nombre + " " + estudiante.apellido_paterno + " " + estudiante.apellido_materno + "|" + "RUT:" + estudiante.rut_estudiante
        y="SEMESTRE ACTUAL:" + "" + str(estudiante.semestre_actual )
        print("Lo sentimos" + x)
        print("|Usted no puede ser contrado(a) porque su semestre actual no es superior al quinto|")
        print(y)
        datos.datos_no_contratados.append(estudiante)
        datos.datos_estudiante.remove(estudiante)
        
        

def escoger_empresa():
    """
    creo una funcion para que el usuario pueda ver el grafico de una empresa y le pido que ingrese la empresa que quiera ver el grafico y para eso sigo la misma logica que se uso para crear el contrato
    y defino primero empresa con none, para luego de ser encontrada valido si la empresa tiene estudiantes accediendo a su lista de estudiantes y si es menor o igual a 0 se le dice 
    mediante un print, porque no fue posible graficar,pero si es mayor a 0 se llama al metodo de graficar emresa
    
    """
    
    
    opcion=input("ingrese el nombre de la empresa para ver el grafico del salario liquido de sus trabajadores")
    empresa=None
    while True:
        for dato in datos.datos_empresa:
            if opcion==dato.nombre_empresa:
                empresa=dato
                
                
        if empresa is None:
            print("|EMPRESA  NO ENCONTRADA|INGRESE UN NOMBRE CORRECTO")
            opcion=input("ingrese el nombre de la empresa para ver el grafico del salario liquido de sus trabajadores")
            
        else:
            break
            
            

    if len(empresa.estudiantes)<=0:
            print("|esta empresa no tiene estudiantes contratados|no se puede graficar|")
            
    elif len(empresa.estudiantes)>0:
        empresa.graficar_empresa()
        
        
datos=Datos()
while True:
    menu()
    opcion=input("ingrese una opcion(1-10)")
    
    if opcion<"1" or opcion>"10":
        print("")
        


    if opcion=="1":
       
        print("OPCION 1 EN EJECUCION...")
        crear_datos_empresa()
        
    elif opcion=="2":
        if len(datos.datos_empresa)<=0:
            print("======================================================================================")
            print("Debe ingresar los datos de las empresas primero para que un estudiante pueda postular ")
            print("======================================================================================")
            
            
            
        else:
            print("OPCION 2 EN EJECUCION")
            
            crear_datos_estudiante()
        
    elif opcion=="3":
        if len(datos.datos_empresa)<=0:
            print("=======================================================")
            print("Debe ingresar las empresas primero para ver sus datos ")
            print("=======================================================")
            
        
        else:
            print("OPCION 3 EN EJECUCION...")
            print("----EMPRESAS------")  
            datos.ver_datos_empresas() 
            
    elif opcion=="4":
        
        if len(datos.datos_estudiantes_registrados)<=0:
            print("=====================================")
            print("NINGUN ESTUDIANTE HA SIDO REGISTRADO")
            print("=====================================")
            
            
            
        else:
            print("OPCION 3 EN EJECUCION...")
            print("----ESTUDIANTES------")  
            datos.ver_datos_estudiante() 
            
    elif opcion=="5":
        if len(datos.datos_estudiante)<=0:
            print("======================================================================================")
            print("Debe ingresar los datos de los estudiantes primero para que puedan escoger un contrato ")
            print("======================================================================================")
            
        else:
            print("|PROCESO DE CONTRATOS|ESTUDIANTES|")
            print("...................................")
            indice=0
            for dato in datos.datos_estudiante:
                indice+=1
                print(str(indice) + "|" + "RUT:" + dato.rut_estudiante + "|" + "NOMBRE:" + dato.primer_nombre)
            escoger_contrato()
       
        
        
    elif opcion=="6":
        
        if len(datos.datos_estudiantes_registrados)<=0:
            print("======================================================================================")
            print("Debe ingresar los datos de los estudiantes primero para ver quienes fueron contratados ")
            print("======================================================================================")
            
            
        elif len(datos.datos_contratados)>=1:
            print("OPCION 4 EN EJECUCION...")
            print("CONTRATADOS")
            for dato in datos.datos_empresa:
                dato.ver_contratados()
        
            
        elif len(datos.datos_contratados)<=0 and len(datos.datos_no_contratados)>0:
            print("=================================")
            print("NINGUN ESTUDIANTE FUE CONTRATADO")
            print("=================================")
            
        
            
        else:
            print("========================================")
            print("|Aun no realiza el proceso de contratos|")
            print("========================================")
            
            
        
    elif opcion=="7":
        
        if len(datos.datos_estudiantes_registrados)<=0:
            print("==========================================================================================")
            print("Debe ingresar los datos de los estudiantes primero para ver quienes no fueron contratados ")
            print("==========================================================================================")
            
            
            
        elif len(datos.datos_no_contratados)>=1:
            print("OPCION 5 EN EJECUCION...")
            print(" NO CONTRATADOS")
            print("----------------------------------------------------------------------------------------------")
            datos.ver_estudiantes_no_contratados()
            print("----------------------------------------------------------------------------------------------")
            
        elif len(datos.datos_contratados)>0 and len(datos.datos_no_contratados)<=0:
            print("==========================================")
            print("TODOS LOS ESTUDIANTES FUERON CONTRATADOS")
            print("==========================================")
            
            
   
        else:
            print("==========================================")
            print("|Aun no realiza el proceso de contratos|")
            print("==========================================")
            
        
            
            
        
    elif opcion=="8":
        if len(datos.datos_estudiante)<=0 and len(datos.datos_estudiantes_registrados)<=0:
            print("=======================================================================================")
            print("Debe ingresar los datos de los estudiantes primero para ver  el grafico de su salario")
            print("=======================================================================================")
            
        
        elif len(datos.datos_contratados)>=1:    
            print("OPCION 6 EN EJECUCION...")
            print(" Crenado grafico")
            datos.grafico_total()
            
    
            
        else:
            print("=====================================================================")
            print("|Ningun estuidante fue contratado|no es posible realizar el grafico|")
            print("=====================================================================")
            
            
    elif opcion=="9":
        if len(datos.datos_empresa)<=0:
            print("==================================================================")
            print("|SIN DATOS DE EMPRESAS|INGRECE LA OPCION 1 PARA PODER AGREGARLOS|")
            print("==================================================================")
            
        elif len(datos.datos_empresa)>0:
            indice=0
            for dato in datos.datos_empresa:
                indice+=1
                print(str(indice) + "|" + dato.nombre_empresa)
    
            escoger_empresa()
                 
    elif opcion=="10":
        
        print("Saliendo del programa.....")
        break              
