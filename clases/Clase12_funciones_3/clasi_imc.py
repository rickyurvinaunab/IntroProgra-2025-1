def clasificar_imc(imc):

    if imc<18.5:
        return "Bajo peso"
    elif imc>=18.5 and imc < 24.9:
        return "Peso normal"
    elif imc>=25 and imc < 29.9:
        return "Sobrepeso"
    elif imc>=30:
        return "Obesidad"