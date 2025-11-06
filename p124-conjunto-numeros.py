# p124-conjunto-numeros.py
# Objtivo: Gestion de datos de tres listas de números

l1 = {50, 60, 70, 80, 90, 100, 200}
l2 = {60, 90, 100, 300, 400, 500}
l3 = {10, 20, 60, 90, 70, 100, 600, 700}

print('\033[H\033[J')
print("--- conjunto numeros ---")
print(f"lista1: {l1}\nlista2: {l2}\nlista3: {l3}")

print("\n--- Unión ( | ) ---")
print(f"Unión (A | B) {l1.union(l2)}")
print(f"Unión (B | C) {l2 | l3}")

print("\n--- Diferencia ( - ) ---")
print(f"Diferencia (A - C) {l1.difference(l3)}")

print("\n--- Diferencia Simétrica ( ^ ) ---")
print(f"Diferencia Simétrica (B ^ C) {l2 ^ l3}")

print("\n--- Intersección ( & ) ---")
print(f"Intersección (B & C): {l2 & l3}")


print("\n--- Subconjuntos ( <= ) ---")
print(f"¿Es A subconjunto de B? : {l1.issubset(l2)}")
print(f"¿Es C subconjunto de A? : {l3 <= l1}")

print("\n--- Pertenencia ( in / not in ) ---")
print(f"¿Está el número 100 en A?: {100 in l1}")
print(f"¿Está el número 60 en A, B y C? {60 in l1,l2,l3}")
print(f"¿No está el número 900 en C? {900 in l3}")