# Inventario de productos por sección del supermercado
supermercado = [
    [["Manzana", 50, 0.5], ["Banana", 30, 0.2]],  # Sección Frutas
    [["Leche", 20, 1.2], ["Yogur", 10, 0.8]],     # Sección Lácteos
    [["Pan", 15, 1.0], ["Galletas", 25, 2.5]]     # Sección Panadería
]

# de bananas
# print(supermercado[0][1][1])  # 30

# # precio yogur
# print(supermercado[1][1][2])  # 0.8

# # Supongamos que se vendieron 5 unidades de pan, por lo que el stock debe disminuir.
# supermercado[2][0][1] -= 5  # Reduce el stock de Pan
# print(supermercado[2][0])  # ['Pan', 10, 1.0]


# Recorriendo las secciones y productos usando for con range
# for i in range(len(supermercado)):  # Itera sobre el índice de las secciones
#     print("Sección " + str(i + 1) + ":")
#     for j in range(len(supermercado[i])):  # Itera sobre los productos en cada sección
#         producto = supermercado[i][j]
#         print(
#             "Producto: " + producto[0] + 
#             ", Stock: " + str(producto[1]) + 
#             ", Precio: $" + str(producto[2])
#         )

# Sección 1:
# Producto: Manzana, Stock: 50, Precio: $0.5
# Producto: Banana, Stock: 30, Precio: $0.2
# Sección 2:
# Producto: Leche, Stock: 20, Precio: $1.2
supermercado = [
    [
        ["Manzana", 50, 0.5], 
        ["Banana", 30, 0.2]
    ],  # Sección Frutas
    [
        ["Leche", 20, 1.2], 
        ["Yogur", 10, 0.8]
    ],     # Sección Lácteos
    [
        ["Pan", 15, 1.0], 
        ["Galletas", 25, 2.5]
    ]     # Sección Panadería
]
# Quiero primero mostrar los productos disponibles y luego solicitarle 
# al usuario que ingrese el nombre de un producto y que se imprima toda la 
# información del producto
supermercado = [
    [
        ["Manzana", 50, 0.5], 
        ["Banana", 30, 0.2]
    ],  # Sección Frutas
    [
        ["Leche", 20, 1.2], 
        ["Yogur", 10, 0.8]
    ],     # Sección Lácteos
    [
        ["Pan", 15, 1.0], 
        ["Galletas", 25, 2.5]
    ]     # Sección Panadería
]

nueva_lista = []

for i in range(len(supermercado)): 
    print("Sección " + str(i + 1) + ":")
    for j in range(len(supermercado[i])):  
        producto = supermercado[i][j]
        if producto[2]>= 1:
            nueva_lista.append(producto)
        print(
            "Producto: " + producto[0] + 
            ", Stock: " + str(producto[1]) + 
            ", Precio: $" + str(producto[2])
        )

print("Productos que valen al menos 1")
for prod in nueva_lista:
    print(prod)