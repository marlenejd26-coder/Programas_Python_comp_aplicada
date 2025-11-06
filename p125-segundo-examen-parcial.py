# p125-segundo-examen-parcial.py
# Objetivo: Procesar el inventario de productos de una tienda de electrónicos

print('\033[H\033[J')
print("--- TecnoTienda - Sistema de Inventario ---")

#Se utiliza def para definir una función
def capturar_productos():
    productos = []

#Se solicita al usuario que capture los datos dentro de un un ciclo while, si se introduce un * se termina la captura de datos.   
    print("Captura de datos de los productos (* para terminar):")
    while True:
        nombre = input("Nombre: ")
        if nombre == "*":
            break
        
        try:
            precio = float(input("Precio: "))
        except ValueError:
            print("❌ Error: Debes ingresar un número válido para el precio.")
            continue
        
        categoria = input("Categoría: ")
        proveedor = input("Proveedor: ")
        
        try:
            stock = int(input("Stock: "))
        except ValueError:
            print("❌ Error: Debes ingresar un número entero")
            continue

     #Almacena los datos en la variable llamada "producto"   
        producto = {
            "nombre": nombre,
            "precio": precio,
            "categoria": categoria,
            "proveedor": proveedor,
            "stock": stock
        }
        productos.append(producto)
    
    #Mensaje que indica que el producto fue agregado correctamente
        print("✅ Producto agregado.\n")
    return productos

#Muestra la lista de diccionarios
def mostrar_datos(productos):
    print("\n=== DATOS (LISTA DE DICCIONARIOS): ===")
    for p in productos:
        print(p)

# Muestra los datos ordenados en una tabla
def mostrar_tabla(productos):
    print("\n=== TABLA DE DATOS: ===")
    print(f"{'Nombre':<20} | {'Precio':<10} | {'Categoría':<15} | {'Proveedor':<15} | {'Stock':<10} |")
    print("-" * 70)
    for p in productos:
        print(f"{p['nombre']:<20} | {p['precio']:<10.2f} | {p['categoria']:<15} | {p['proveedor']:<15} | {p['stock']:<10} |")

# Se muestra el resumen de los datos
def resumen_inventario(productos):
    print("\n=== RESUMEN ===")

#Cantidad total de productos    
    total_productos = len(productos)
    print(f"\nProductos totales: {total_productos}")
    
# Se usa .get para obtener los valores de categorias y proveedores y despues se mustran en forma de lista
    categorias = {}
    proveedores = {}
    total_stock = 0
    total_precios = 0
    
    for p in productos:
        cat = p["categoria"]
        categorias[cat] = categorias.get(cat, 0) + 1
        
        prov = p["proveedor"]
        proveedores[prov] = proveedores.get(prov, 0) + 1
        
        total_stock += p["stock"]
        total_precios += p["precio"]
    
    print("\nCategorías:")
    for c, n in categorias.items():
        print(f" - {c}: {n}")
    
    print("\nProveedores:")
    for pr, n in proveedores.items():
        print(f" - {pr}: {n}")
    
#Se calcula el promedio de stock y los precios
    promedio_stock = total_stock / total_productos if total_productos > 0 else 0
    promedio_precios = total_precios / total_productos if total_productos > 0 else 0
    
    print(f"\nStock-> Suma: {total_stock}, Promedio: {promedio_stock:.2f}")
    print(f"Precio-> Suma: {total_precios:.2f}, Promedio: {promedio_precios:.2f}")
    
# Producto más caro y más barato
    producto_mas_caro = max(productos, key=lambda x: x["precio"])
    producto_mas_barato = min(productos, key=lambda x: x["precio"])
    
    print(f"\n{producto_mas_caro['nombre']} de (${producto_mas_caro['precio']:.2f}) es el producto más caro")
    print(f"{producto_mas_barato['nombre']} de (${producto_mas_barato['precio']:.2f}) es el producto más caro")


# PROGRAMA PRINCIPAL
#Define la función principal, se ejecuta para iniciar el flujo del programa
def main():
    productos = capturar_productos()
    mostrar_datos(productos)
    mostrar_tabla(productos)
    resumen_inventario(productos)

#Se asegura de que el programa solo se ejecute cuando corresponde
if __name__ == "__main__":
    main()
