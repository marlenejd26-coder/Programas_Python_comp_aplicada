# p102-listas-aleatorios-suma.py
# Objetivo: Crear una tercera lista a partir de las listas A y B

import random #Para generar números aleatorios
print('\033[H\033[J')
print('Crear una tercera lista a partir de las listas A y B:\n')

MAX = 10
lista_a = []
lista_b = []
lista_c = []

for i in range(MAX): 
    lista_a.append(random.randint(1, 100)) # Llena la lista del sensor A
    lista_b.append(random.randint(1, 100)) # Llena la lista del sensor B

for i in range(MAX):
    lista_a.append(random.randint(1, 100)) # Llena la lista del sensor A
    lista_b.append(random.randint(1, 100)) # Llena la lista del sensor B
    if lista_a[i] % 2 != 0 and lista_b[i] % 2 != 0:
        lista_c.append(lista_a[i] + lista_b[i])
    else:
        lista_c.append(0)

print("\n--- Resultados (Suma solo si A[i] y B[i] son ambos impares) ---")
print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")
print(f"Lista C: {lista_c}")
