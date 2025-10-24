# p100-listas-multiplica.py
# Objetivo: Crear una tercera lista multiplicando los elementos de dos listas.

print('\033[H\033[J')
print('Crear una tercera lista multiplicando los elementos de dos listas.')

ListaA = [2, 4, 6, 8, 10]
ListaB = [5, 1, 3, 7, 9]
multiplicacion = []

for i in range(5):
    multiplicacion.append (ListaA[i] * ListaB[i])

print("\n--- Resultados ---")
print(f"Lista A: {ListaA}")
print(f"Lista B: {ListaB}")
print(f"Lista C (A * B): {multiplicacion}")