import random
import matplotlib.pyplot as plt
import numpy as np


class Empresa: 
    
    def __init__(self,rut_empresa,nombre_empresa,phono_empresa,email_empresa,direccion_empresa): 
        """
        inicializo  con init para poder crear los atributos del objeto, se define self para hacer la referencia al objetos que se creo
        
        """
        
        self.rut_empresa=rut_empresa
        self.nombre_empresa=nombre_empresa
        self.phono_empresa=phono_empresa                 
        self.email_empresa=email_empresa
        self.direccion_empresa=direccion_empresa
        self.estudiantes = []
        
        
    def graficar_empresa(self):
        """
         Se crea un metodo en el cual se define un eje x e y en listas que se llenan a partir de los estudiantes que tenga contrados donde el eje x es
         el rut del estudiante el cual obtengo recorriendo la lista de self.estuidantes[ ] que es una lista de objetos en la cual tiene sus estudiantes 
         contratdos y ahi accedo a sus rut y tambien a su salario en uf que sera el eje y, para finalmente crear el grafico
        """
        x=[]
        y=[]
    
        for  estudiante in self.estudiantes:
            x.append(estudiante.rut_estudiante)
        
        for salario in self.estudiantes:
            y.append(salario.salario_liquido)
            
        color_relleno="cyan"
        color_borde="darkgreen"
        grosor=0.5
        legenda="1UF=39000$"
        plt.bar(x,y,edgecolor=color_borde,color=color_relleno,width=grosor,label=legenda)
        plt.xticks( x,x,rotation=45)
        
        plt.title("grafico de sueldo liquido de estudiantes contratados por la empresa")
        plt.xlabel("Contratados")
        plt.ylabel("salario en UF")
        plt.legend()
        plt.show()
       
        
    
        
        
    def ver_contratados(self):
        """
        defino un metodo para poder ver los contratados de la empresa recorriend con un for la lista self.estudiantes[]
        """
        for i in self.estudiantes:
            print("|" + "RUT:" + i.rut_estudiante + "|" + "NOMBRE:" + i.primer_nombre + " " + i.segundo_nombre  + "|EMPRESA|" +  self.nombre_empresa + "|"+ "SUELDO LIQUIDO(UF):"+ str(i.salario_liquido))
        
    def __str__(self):
        """
        defino un str para luego retornar los atributos del obejto empresa, menos su lista de estudiantes contratados
        """
        return  "|" + "RUT:" + self.rut_empresa + "|" + "NOMBRE:" + self.nombre_empresa + "|" + "PHONO:" + self.phono_empresa + "|" + "EMAIL:" + self.phono_empresa + "|" + "EMAIL:" + self.email_empresa + "|" + "DIRECCION:" + self.direccion_empresa 
        
         
    
class Estudiante:
    
    def __init__(self,rut_estudiante,primer_nombre,segundo_nombre,apellido_paterno,apellido_materno,phono_estudiante,email_estudiante,fecha_nacimiento,carrera,universidad,semestre_actual): 
        """
        se crea una clase llamada Estudiante la cual inicializo con self para poder darle  los atributos que tendra el obejto Estudiante
        """
        
        self.rut_estudiante=rut_estudiante
        self.primer_nombre=primer_nombre
        self.segundo_nombre=segundo_nombre
        self.apellido_paterno=apellido_paterno
        self.apellido_materno=apellido_materno
        self.phono_estudiante=phono_estudiante                                                                                                                                               #
        self.email_estudiante=email_estudiante                                                                                                           
        self.fecha_nacimiento=fecha_nacimiento                                                                                                            
        self.carrera=carrera
        self.universidad=universidad
        self.semestre_actual=semestre_actual
        self.salario_liquido=0
        self.empresas = []
        
  
    
    def __str__(self):
        """
        defino un str para luego retornar los atributos que tengo en el obejto Estudiante
        """
        return "|" + "RUT:" + self.rut_estudiante + "|" + "NOMBRE:" + self.primer_nombre + " " + self.segundo_nombre  + " "  + self.apellido_paterno + " " + self.apellido_materno + "|" + "PHONO:" + self.phono_estudiante + "|" + "EMAIL:" + self.email_estudiante + "|" + " FECHA DE NACIMIENTO:" + self.fecha_nacimiento + "|" + "CARRERA:" + self.carrera + "|" + "UNIVERSIDAD:" + self.universidad + "|" + "SEMESTRE:" + str(self.semestre_actual)+ "|" + "SUELDO LIQUIDO:" + str(self.salario_liquido)
       
    def realizar_contrato(self, Empresa):
        """
        se c rea un metodo en el cual se recibe el objeto empresa para poder hacer el contrato del estudiante con la empresa , agregando el estudiante  a la empresa y la empresa al estudiante,
        tambien se le da un salario liquido entre 10 y 15 UF(todas las empresas pagan igual)
        """
        Empresa.estudiantes.append(self)
        x=random.randint(10,15)
        self.salario_liquido =x
        self.empresas.append(Empresa)
        
        print("Estuidante contratado!")
        
        
        
    
  
        
        
        
   
    
        
    
class Datos: 
    
    def __init__(self):
        
        """
        inicializo una clase Datos con self, la cual no resive ningun atributo ingresado por el usuario,pero si me servira como una base de datos para guardar todo los datos de las empresas y los estudiantes
        """
        self.datos_empresa=[]
        
        self.datos_estudiante=[]
        
        self.datos_estudiantes_registrados=[]
        
        self.datos_contratados=[]
    
        self.datos_no_contratados=[]
        
    def agregar_datos_empresa(self,Empresa):
        """
        creo un metodo que recibe la clase de Empresa, este  se agrega a la lista de datos_empresa la cual se transfomra en una lista de objetos 
        """
        self.datos_empresa.append(Empresa)
    
        
    def agregar_datos_estudiante(self,Estudiante):
        """
        creo un metodo que recibe la clase Estudiante para agregarla a la lista de datos de estudiante la cual se transfomra en una lista de objetos, tambien agrego al estudiante a otra lista 
        que no se tocara nunca ya, que tendra a todos los estudiantes registrados, en cambio la de datos_estudiante  va variando dependiendo de quien fuie contratado o no para agregarlos a una de las dos listas de contratos
        
        """
        
    
        self.datos_estudiante.append(Estudiante)
        self.datos_estudiantes_registrados.append(Estudiante)
   
       
            
    def ver_estudiantes_no_contratados(self):
        """
        se crea un metodo para poder ver los estudiantes no  contratados llamando con un for a  self.datos_no_contratados que tiene en su lista a los no contratados,tambien se  les dice el motivo por el cual no son contratados
        
        """
        for dato in self.datos_no_contratados:
            print(dato , "|", "MOTIVO= No supera el 5 semestre de universidad")
            
    
        
        
    def ver_datos_empresas(self):
        """
        se crea un metodo para acceder a todas las empresas registradas y mediante el for se accede al objeto empresa y  se imprime su __str__
        """
        indice=0
        for  dato_1 in self.datos_empresa:
            indice +=1
            print(str(indice) , dato_1)
            
   
   
   
        
        
        
        
    def ver_datos_estudiante(self):
        """
        se crea un metodo para acceder a todos los  estudiantes y mediante con el  for se accede a todos los estuiantes registrados un por uno para asi imprimir su __str__ 
        """
        for  dat in self.datos_estudiantes_registrados:
            print(dat)
    
    
    def grafico_total(self):
        """
        se crea un metodo para ver  un grafico de barras agrupado donde en el eje x se pondran los nombres de las empresas y en eje y  sus trabajadores donde se representara su sueldo en uf
        se empieza creando  dos listas, en una itero en un for donde tengo a todas las empresas y cada ves que se itera el for accedo a el nombre de la empresa y lo guardo en una lista de nombres_empresas[],
        dentro de ese for accedo al dato.estudiante donde tengo una lista del objeto estudiante y por cada ves que se itera  guardo el salario del estuiante en una lista de salarios la cual agrego a salarios por empresa
        ya que cada empresa tiene x estudiantes y esos se guardan sus salarios en una lista creando una lista de listas,porque el salario se limpia en cada for,pero se guarda en el salario_por_empresa, tambien valido con una cantidad maxima
        de estudiantes teniendo la longitud de empresa se cambia el valor 0 por la longitud dela empresa y luego con plt.get_camp("tab10") accedo a la paletas de colores de matplotlib y le agrego un color aleatorio a las empresas dependiendo de su longitud,
        para finalizar  con un for que entra en el rango de estudiantes y por cada valor me crea una lista para iterar otro for dentro que ingresa a la lista de salarios por empresa que tiene una lista de numeros por eso al momento de agregar el salario uso el i para 
        acceder a los valores de la lista y si la empresa no tiene valores le agrega 0, para finalisar creando el grafico y centrando el eje x para que no se vea descuadrado
        
        """
        nombres_empresas=[]
 
        salario_por_empresa=[]
        
        estudiantes_max=0
        for dato in self.datos_empresa:
            x=dato.nombre_empresa
            nombres_empresas.append(x)
            salarios_empresa=[]
            for estudiante in dato.estudiantes:
                salarios_empresa.append(estudiante.salario_liquido)
            salario_por_empresa.append(salarios_empresa)   

            if len(salarios_empresa)> estudiantes_max:
                estudiantes_max=len(salarios_empresa)       
                
                
        color_aleatorio=plt.get_cmap("tab10") 
        colores=[] 
        for i in range(len(nombres_empresas)):
            color=color_aleatorio(i%color_aleatorio.N)      
            colores.append(color)    
        x=np.arange(len(nombres_empresas))
        ancho=0.15
        plt.figure(figsize=(10, 6), layout="constrained")
        
        for i in range(estudiantes_max):
            valores_por_empresa=[]
            for salario in salario_por_empresa:
                if i < len(salario):
                    valores_por_empresa.append(salario[i])
                
                else:
                    valores_por_empresa.append(0)
                          
            plt.bar(x+i*ancho,valores_por_empresa,edgecolor="black",color=colores,width=ancho)
        plt.xticks( x+ ancho*(estudiantes_max-1)/2,nombres_empresas,rotation=45)
        plt.xlabel("Empresas")
        plt.ylabel("Salario en UF de estudiantes contratados")
        plt.title("Salario liquido de estudiantes por empresa")
        plt.legend()
        plt.show()