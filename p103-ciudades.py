# p103-ciudades.py
# Objetivo: Leer nombres de ciudades en una lista, continuando hasta que el usuario introduzca el carácter $

print('\033[H\033[J')
print('Leer nombres de ciudades en una lista, continuando hasta que el usuario introduzca el carácter $')

ciudades = []
while True:
    ciudad = input("Introduzca nombre de ciudad ($ para detener): ")
    if ciudad == "$":
        break
    ciudades.append(ciudad)

lista_ordenada = sorted(ciudades, reverse=True)
vocales = "aeiouAEIOU"
ciudades_consonantes = [c for c in ciudades if c and c[0] not in vocales]

print(f"\n--- Resultados --- ")
print(f"Total de ciudades introducidas: {len(ciudades)}")
print(f"Lista completa de ciudades: {ciudades}")
print(f"Lista ordenada descendente: {lista_ordenada}")
print(f"Cantidad de ciudades que inician con consonante: {len(ciudades_consonantes)}")
print(f"Ciudades que inician con consonante: {ciudades_consonantes}")
