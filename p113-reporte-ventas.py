# p113-reporte-ventas.py
# Objetivo: Crear un diccionario de diccionarios 

print('\033[H\033[J')
print('Reporte de Ventas por cliente\n')

n = int(input("Número de compras a registrar ? "))
compras = []

for i in range(1,n+1):
    print(f'\n------ Compra {i} ------')
    compra = {
    "cliente" : input("Cliente : "),
    "producto": input("Producto : "),
    "cantidad": int( input("Cantidad : ")),
    "precio" : float(input("Precio : "))
    }
    compras.append(compra)

print('\n--- Lista de Compras Registradas ---\n')

clientes = {} 
for compra in compras:
    cliente = compra["cliente"]
    if cliente not in clientes:
        clientes[cliente] = {"cantidad": 0, "subtotal": 0}

    clientes[cliente]["cantidad"] += compra["cantidad"]
    clientes[cliente]["subtotal"] += compra["cantidad"] * compra["precio"]

for cliente, datos in clientes.items():
    print("Cliente :", cliente)
    print("Cantidad:", datos["cantidad"])
    print("Subtotal:", datos["subtotal"])
    print()