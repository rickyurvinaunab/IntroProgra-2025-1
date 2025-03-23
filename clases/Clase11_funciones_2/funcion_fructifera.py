def saludo (lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(saludo('en'),'Ricardo')
print(saludo('es'),'Ingrid')
print(saludo('fr'),'Liliana')
