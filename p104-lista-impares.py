# p104-lista-impares.py
# Objetivo: Leer un entero n. Llenar una lista con los primeros n números impares.

print('\033[H\033[J')
print('Leer un entero n. Llenar una lista con los primeros n números impares.')

n = int(input("Introduzca la cantidad de números impares (n): "))
impares = [2 * i + 1 for i in range(n)]
print("\n--- Generación de Lista ---")
print(f"Lista de los primeros {n} números impares: {impares}")

# Suma y promedio
suma_total = sum(impares)
promedio = suma_total / n
print("\n--- Cálculos ---" )
print(f"Suma de los números: {suma_total}")
print(f"Promedio de los números: {promedio}")

#Numeros divisibles entre 3
div3 = [x for x in impares if x % 3 == 0]
suma_div3 = sum(div3)
print("\n--- Divisibles entre 3 ---")
print(f"Números divisibles entre 3: {div3}")
print(f"Suma de los números divisibles entre 3: {suma_div3}")

#Busqueda
print("\n--- Búsqueda ---")
buscar = int(input("\nIntroduzca elemento a buscar: "))
if buscar in impares:
    posicion = impares.index(buscar)
    print(f"El elemento {buscar} está en la lista en la posición (índice) {posicion}.")
else:
    print(f"El elemento {buscar} no está en la lista.")

