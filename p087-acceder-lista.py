# p087-acceder-lista.py
# Objetivo: Acceder a elementos de una lista

nums = [10, 20, 30, 40, 60, 70, 10, 20, 99]

print('\033[H\033[J')
print('Acceder a los elementos de una lista\n')

print('\nLongitud y contenido de las mediciones :')
print(f'Cuantas mediciones son : {len(nums)}')
print(f'Todas las mediciones : {nums} ')

print('\nPor indice positivo : ')
print(f'Primera y última : {nums[0]}, {nums[8]}')

print('\nPor indice negativo : ')
print(f'Primera y última : {nums[-9]}, {nums[-1]}')

print('\nPor rango : ')
print(f'De la 2 ala 6 (6 no incluida): {nums[2:6]}')

print('\nPor saltos :')
print(f'Las primeras 3 desde el principio : {nums[:3]}')
print(f'Las últimas 3 desde el 6 hasta el final : {nums[6:]}')