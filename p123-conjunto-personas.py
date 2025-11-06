# p123-conjunto-personas.py
# Objetivo: Gestion de datos de dos listas de nombres

listaA = {'Juan', 'Maria', 'Pedro', 'Jose', 'Rocio'}
listaB = {'Pedro', 'Juan', 'Pablo', 'Mateo', 'Esther'}

print('\033[H\033[J')
print('--- conjunto personas --- \n')
print(f"listaA: {listaA}\nlistaB: {listaB}")

#Calcula y muestra los resultados de las siguientes operaciones:
print("\n--- Unión ( | ) ---")
print(f"Unión (A | B) : {listaA.union(listaB)}")

print("\n--- Intersección ( & ) ---")
print(f"Intersección (A & B) {listaA.intersection(listaB)}")

print("\n--- Diferencia ( - ) ---")
print(f"Diferencia (A - B): {listaA.difference(listaB)}")


print("\n--- Diferencia Simétrica ( ^ ) ---")
print(f"Diferencia Simétrica (A ^ B):{listaA.symmetric_difference(listaB)}")

#Verifica y muestra el resultado (Verdadero/Falso) de las siguientes afirmaciones:
print("\n--- Subconjuntos ---")
print(f"¿Es Pablo, Mateo un subconjunto de B?:{"Pablo" in listaB},{"Mateo" in listaB}")

print("\n--- Superconjuntos ( >= ) ---")
print(f"¿Es A un superconjunto de Reynaldo, Angelica? : {"Reynaldo" in listaA},{"Angelica" in listaA}")

print("\n--- Pertenencia ( in / not in ) ---")
print(f"¿Está Pedro en el conjunto A? : {'Pedro' in listaA}")
print(f"¿No está Lilia en el conjunto B? : {'Lilia' in listaB}")



