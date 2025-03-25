import random
#15320
lista_estudiantes = [
    "ALEGRÍA GONZÁLEZ BENJAMÍN",
    "BARRIENTOS FONCEA MARTÍN",
    "BELTRAN PINTO ANTONELLA",
    "CAUAS FURNARO LUCAS",
    "CID ZAPATA AMARO",
    "DURÁN TOLEDO FERNANDO",
    "LECUMBERRI URIARTE SANTI",
    "PÉREZ BOCAZ LUKAS",
    "PINO RODRÍGUEZ ISIDORA",
    "ROSALES PÉREZ BENJAMÍN",
    "VÁSQUEZ MORALES NICOLÁS",
    "VELA TIRADO ELMER"
]
#11615
lista_estudiantes = [
    "ACEVEDO MUÑOZ FLORENCIA",
    "ALGUIBAY LOPEZ TOBIAS",
    "BALTIERRA ASCENCIO CRISTIAN",
    "CHAMORRO BASSO MARTÍN",
    "FUENTES CESPEDES PATRICIA",
    "FUICA SEPÚLVEDA NICOLÁS",
    "GAETE CURIQUEO PABLO",
    "GÓNGORA DURÁN JUAN",
    "JARA TUDELA JOAQUÍN",
    "JARA TUDELA VICENTE",
    "LARRONDO OLAVARRIA RAYEN",
    "LEON BENITEZ NICOLAS",
    "LIRA CARO SOFÍA",
    "MALDONADO HERRERA BENJAMIN",
    "MANSILLA SALDAÑA FERNANDO",
    "MEDINA LANDA AGUSTÍN",
    "NAVARRO SÁEZ BENJAMÍN",
    "ORELLANA SEGUIN RODRIGO",
    "PEDEMONTE URIBARRI VALENTINA",
    "PEREIRA RUPAYÁN BENEDICTO",
    "PONCE VILLEGAS JOSEFA",
    "PUENTES MOLINA ANGEL",
    "ROMERO MEZA BENJAMIN",
    "SÁNCHEZ MUÑOZ MARTÍN",
    "SILVA MEÑIQUE MARTÍN",
    "VÁSQUEZ ATOCHE HAMILTON"
]

numero_de_ganadores = 3

#random.sample permite obtener una muestra aleatoria de una lista
ganadores = random.sample(lista_estudiantes, numero_de_ganadores)

print("¡Felicidades a los ganadores del sorteo!")
for ganador in ganadores:
    print(ganador)
