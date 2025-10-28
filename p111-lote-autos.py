# p111-lote-autos.py
# Objetivo: Crear una lista de diccionarios 

autos = [
{ 'marca':'Ford', 'modelo':'Mustang', 'año': 1964 },
{ 'marca':'VW', 'modelo':'Jetta', 'año': 2015 }
]
autos.append({ 'marca':'Honda', 'modelo':'CVR', 'año': 2024 })
# append se usa para agregar a una lista 
print('\033[H\033[J')
print('Listado de Autos')

print(f'\nAutos : {autos} - {len(autos)}')

print('\nCada auto dentro de los autos:') # Para imprimir cada elemento por separado
for auto in autos:
    print(auto)

print('\nDatos de los autos en forma de Tabla:')
print('-'*50)
for k in autos[0].keys(): #Para cada llave se toma un elemento
    print(f'{k}\t', end='') # Para tenerlo en forma de tabla (encabezado)
print() # Para dejar el espacio
print('-'*50)

#Ciclo para iterar en cada elemento
for auto in autos:
    for v in auto.values(): #Para cada valor 
        print(f'{v}\t', end='') #Poner de forma horizontal
    print()

print('\nDatos en forma de Registro')
print('-'*50)
suma_años = 0
for auto in autos:
    suma_años = suma_años + auto["año"] #Para sumar lo años
    for k,v in auto.items():
        print(f'{k:<12} : {v:>12}')
    print('')
print('-'*50)

print("Suma años: ", suma_años)
