

class graficoUF:
    """generara un gráfico de barras con los salarios líquidos de estudiantes contratados."""
     
    def __init__(self, lista_estudiantes):
        
        """
        se inicia el gráfico de barras con la lista de estudiantes.
        
        Argumento:
            lista_estudiantes (list): Lista de objetos Estudiante.
        """
        
        self.lista_estudiantes = lista_estudiantes
        self.salarios = []
        self.nombres_estudiantes = []
        self.estudiantes_con_contrato = False
        
    def sacar_datos(self):
        
        """Se filtrara los estudiantes con contrato y sin contrato y tambien sacara o extraera los salarios y los nombres de los estudiantes."""
        
        for estudiantes in self.lista_estudiantes:
            self.salarios.append(int(estudiantes.salarioL))
            self.nombres_estudiantes.append(f"{estudiantes.primer_nombre} {estudiantes.apellidop}")
            self.estudiante_con_contratos = True
                    
    def generarUF(self):
        import matplotlib as plt
        
        """Mostrara el gráfico de barras con los datos que se sacaron o extrayeron anteriormente."""
        
        if not self.estudiante_con_contratos:
            print("no hay estudiantes con un contrato")
            return
        fig = plt.figure()
        plt.bar(self.nombres_estudiantes, self.salarios, color='red')
            

        plt.title("Salario Líquido de Estudiantes Contratados (UF)", fontweight='bold')
        plt.xlabel("Estudiantes")
        plt.ylabel("Salario (UF)")
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--')

            
        contador = 0
        while contador < len(self.salarios):
            plt.text(contador, self.salarios[contador] + 0.2, f"{self.salarios[contador]} UF")
            contador += 1

        plt.tight_layout()
        plt.show()
        
        
        
        
        
        
        
        
        
                       
