# Escriba un programa para que un estudiante decida cómo ir desde su casa en Ñuñoa hasta la Universidad Andres Bello en Casona. Tiene tres opciones: ir en Metro, en bicicleta o en micro (bus).
# Condiciones:
# Si está lloviendo, el estudiante preferirá ir en Metro.
# Si no está lloviendo y hay congestión vehicular en la Avenida Grecia, preferirá ir en bicicleta para evitar el tráfico.
# Si no está lloviendo y no hay congestión vehicular, pero la calidad del aire es regular o mala, preferirá ir en Metro.
# Si ninguna de las condiciones anteriores se cumple, tomará la micro.
#
# Respuesta deseada “El estudiante decide ir en” , transporte


# Solicitar al usuario el estado del clima
clima = input("¿Está lloviendo? (si/no): ")
# Solicitar al usuario el estado del tráfico
trafico = input("¿Hay congestión vehicular en Avenida Grecia? (si/no): ")
# Solicitar al usuario la calidad del aire
aire = input("¿La calidad del aire es regular o mala? (regular/mala): ")

# Verificar si está lloviendo
if clima == "si":
    print("El estudiante decide ir en Metro.")
# Verificar si no está lloviendo y hay congestión vehicular
elif clima == "no" and trafico == "si":
    print("El estudiante decide ir en bicicleta.")
# Verificar si no está lloviendo, no hay congestión vehicular y la calidad del aire es regular o mala
elif clima == "no" and trafico == "no" and (aire == "regular" or aire == "mala"):
    print("El estudiante decide ir en Metro.")
# Si no se cumple ninguna condición
else:
    print("El estudiante decide ir en micro.")
