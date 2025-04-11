supermercado = [
    [["Manzana", 50, 0.5], ["Banana", 30, 0.2]],  # Sección Frutas
    [["Leche", 20, 1.2], ["Yogur", 10, 0.8]],     # Sección Lácteos
    [["Pan", 15, 1.0], ["Galletas", 25, 2.5]]     # Sección Panadería
]


print("Productos disponibles:")
for i in range(len(supermercado)):
    for j in range(len(supermercado[i])):
        print(supermercado[i][j][0])
print("----------------------")      
producto = input("Ingrese el nombre del producto: ")
for i in range(len(supermercado)):
    for j in range(len(supermercado[i])):
        if supermercado[i][j][0] == producto:
            print(
                "Producto: " + supermercado[i][j][0] + 
                ", Stock: " + str(supermercado[i][j][1]) + 
                ", Precio: $" + str(supermercado[i][j][2])
            )
            break
    else:
        continue
    break
# Ingrese el nombre del producto: Yogur
# Producto: Yogur, Stock: 10, Precio: $0.8