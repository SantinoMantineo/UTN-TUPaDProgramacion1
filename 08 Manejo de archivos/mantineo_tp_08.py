# punto 1

with open("productos.txt", "w") as archivo:
    archivo.write("naranja,1200,10\n")
    archivo.write("banana,1000,5\n")
    archivo.write("manzana,1500,8\n")
    
# punto 2
with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        producto = linea.strip().split(",")
        print(f'Producto: {producto[0]} | Precio: {producto[1]} | Cantidad: {producto[2]}')
# punto 3

with open("productos.txt", "a") as archivo:
    nuevo_producto = input("Ingresa el nuevo producto (formato: nombre, precio, cantidad): ")
    archivo.write(nuevo_producto + "\n")
    
# punto 4
productos = []
with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        nombre, precio, cantidad = linea.strip().split(",")
        productos.append({
            "nombre": nombre,
            "precio": int(precio),
            "cantidad": int(cantidad)
        })
    
    # punto 5
    nombre_a_buscar = input("Ingresa el nombre del producto que queres buscar: ").lower()
    encontrado = False
    for item in productos:
        if item["nombre"].lower() == nombre_a_buscar:
            print(f"\nProducto encontrado:")
            print(f"Nombre: {item['nombre']}")
            print(f"Precio: ${item['precio']}")
            print(f"Cantidad: {item['cantidad']}")
            encontrado = True
            break

    if not encontrado:
        print("No se encontró un producto con ese nombre.")

    # punto 6
    with open("productos.txt", "w") as archivo:
        for item in productos:
            linea = f"{item['nombre']},{item['precio']},{item['cantidad']}\n"
            archivo.write(linea)

    print("'productos.txt' actualizado correctamente.")