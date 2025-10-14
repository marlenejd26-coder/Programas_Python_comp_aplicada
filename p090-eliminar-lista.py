# p090-eliminar-lista.py
# Objetivo: Mostrar las diferentes formas de eliminar elementos de una lista

print('\033[H\033[J')
print("Eliminar elementos de una lista")

nums = [1,3,5,7,9,11,99,15,88,19,100]

print(f"Datos originales con anomalias: {nums} - {len(nums)}")

print(f"Eliminar el valor 99: ")
nums.remove(99)
print(f"Resultado: {nums} - {len(nums)}")

print(f"Eliminar el elemento en la posición 8")
num_removido = nums.pop(8)
print(f"Resultado: {nums} - {len(nums)} - Se removio: {num_removido}")

print(f'Eliminar el último elemento:')
ultimo_num = nums.pop()
print(f'Resultado: Removido({ultimo_num}): {nums}\n')

print(f'Eliminar todos los elementos de la lista:')
nums.clear()
print(f'Resultado: {nums}\n')