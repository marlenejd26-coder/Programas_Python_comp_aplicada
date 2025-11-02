# p118-eliminar-diccionario.py
#Objetivo: Crear un diccionario de municipios y eliminar elementos 

print('\033[H\033[J')
print("Crear un diccionario de municipios y eliminar elementos")

municipios = {'Apozol': 1863, 'Calera': 1868, 'Fresnillo': 1554, 'Guadalupe': 1821, 'Jalpa': 1824, 'Jerez': 1824, 'Loreto': 1931, 'Mazapil': 1824, 'Momax': 1857}

print("Diccionario inicial:")
print(municipios)

del municipios["Apozol"]
print("\nDespués de 'Del Apozol':")
print(municipios)

municipios.pop("Fresnillo")
print("\nDespués de 'pop(Fresnillo)':")
print(municipios)

municipios.popitem()
print("\nDespués de 'popitem()' (eliminando Momax)::")
print(municipios)

municipios.clear()
print("\nDespués de 'clear()':")
print(municipios)