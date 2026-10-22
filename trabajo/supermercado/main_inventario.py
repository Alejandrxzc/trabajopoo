from producto import Producto, Inventario

inventario = Inventario()
cantidad_productos = int(input("Ingrese la cantidad de productos en inventario: "))

for _ in range(cantidad_productos):
    cod = input("Código del producto: ")
    nom = input("Nombre del producto: ")
    cant = int(input("Cantidad disponible: "))
    producto = Producto(cod, nom, cant)
    producto.verificar_stock()
    inventario.agregar_producto(producto)

print("\n--- Estado individual ---")
for p in inventario.productos:
    print(p.ver_info())
    
print("\n--- Reporte Final ---")
print(inventario.reporte_consolidado())
