from transmisiones.exito import decodificar_exito
from transmisiones.fallo import buscar_nombre


def main():
    while True:
        # Recibimos el mensaje del usuario
        mensaje = input("Ingresa el mensaje de transmisión: ")
        
        if mensaje == "FIN":
            print("La misión ha finalizado!!! :D")
            break
        
        # Decidimos si hay "fallo" en el mensaje
        if "fallo" in mensaje: # Busca fallo en el string, si lo encuentra devuelve True, sino False
            nombre_astronauta = buscar_nombre(mensaje)
            print("El astronauta", nombre_astronauta, "ha tenido un fallo y necesita asistencia!")
        else:
            nombre_astronauta = decodificar_exito(mensaje)
            print("El astronauta", nombre_astronauta, "ha completado la misión con éxito!")


main()

# Ingresa el mensaje de transmisión: ehfoIfnfalloggrriidd
# El astronauta Ingrid ha tenido un fallo y necesita asistencia!
# Ingresa el mensaje de transmisión: sSBalmuupeyln
# El astronauta Samuel ha completado la misión con éxito!
# Ingresa el mensaje de transmisión: FIN
# La misión ha finalizado!!! :D

# ajckMhehnttfallohhoonrs
# hLxiilriiaannaz
# dBreenijmazmoipn
# FIN
