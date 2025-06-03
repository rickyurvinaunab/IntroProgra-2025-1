class Cancion:

    def __init__(self, titulo, artista, cantidad_reproducciones = 0):
        self.tit = titulo
        self.art = artista
        self.cant_r = cantidad_reproducciones

    def __str__(self):
        return "La cancion es:" + self.tit +" y su artista es: "+ self.art + " se ha reproducido: "+ str(self.cant_r)
    
    def mas_reproducida(self, lista):
        cant_max = 0
        nombre_max = ""
        for cancion in lista:
            if cancion.cant_r > cant_max:
                cant_max = cancion.cant_r
                nombre_max = cancion.tit
        
        return nombre_max
     

artista = "Maluma"
cancion1 = Cancion("4 babys", artista)
cancion2 =  Cancion("Miami", artista, 12)
cancion3 =  Cancion("Dtmf", "bad bunny", 8)
lista = [cancion1, cancion2, cancion3]
nombre_c1 = cancion1.mas_reproducida(lista)
print(nombre_c1)