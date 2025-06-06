class Cancion:

    def __init__(self, titulo, artista):
        self.tit = titulo
        self.art = artista

    def reproducir(self,minutos):
        return  "Reproduciendo "+ self.tit +" de "+self.art + str(minutos)
    
cancion1 = Cancion("DtMf","Bad Bunny")
cancion2 = Cancion("Satirologia","Kid bodo")
resultado = cancion1.reproducir(4)
print(resultado)
print(cancion1.reproducir(10))