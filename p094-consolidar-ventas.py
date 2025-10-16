# p094-consolidar-ventas.py
# Consolidar las ventas de dos sucursales, las ventas las cptura el usuario

print('\033[H\033[J')
print('Consolidar las ventas de las dos sucursales\n')
ventas = int(input('¿Cuántas ventas por sucursal? '))

# Inicializar listas
ventas1 = []
ventas2 = []
todo = []

# Leer datos de la Sucursal 1 usando un ciclo
print('\n Dame las ventas de la primera sucursal 1:')
for i in range(ventas):
    venta = int(input(f'Venta del día {i+1} ? ')) 
    ventas1.append(venta)

# Leer datos de la Sucursal 2
print('\n Dame las ventas de la primera sucursal 1:')
for i in range(ventas):
    venta = int(input(f'Venta del día {i+1} ? ')) # Es para que no se muestre desde la posición 0
    ventas2.append(venta)

print('\nConsolidando las ventas:')
for i in range(ventas):
    sumadia = ventas1[i] + ventas2[i]
    todo.append(sumadia)

# Mostrar resultados
print('\n--- Reporte de Ventas ---')
print(f'Sucursal 1: {ventas1}')
print(f'Sucursal 2: {ventas2}')
print(f'Ventas Consolidadas: {todo}')