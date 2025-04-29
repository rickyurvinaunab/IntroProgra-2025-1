
menu = [
    '# 1 Nombre: sanduche Precio: 4500 Tipo de menu: 1 \n',
    '# 2 Nombre: pan Precio: 4500 Tipo de menu: 2 \n'
]


for plato in menu:
    plato_lista = plato.split()
    if plato_lista[9] == "1":
        print(plato)