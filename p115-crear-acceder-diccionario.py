# p115-crear-acceder-diccionario.py
# Objetivo: Crear un diccionario llamado dias usando llaves numéricas para los días de la semana.

print('\033[H\033[J')
print("Crear un diccionario llamado dias usando llaves numéricas para los días de la semana.")


dias = {1: 'Lunes', 2: 'Martes', 3: 'Miércoles', 4: 'Jueves', 5: 'Viernes', 6: 'Sábado', 7: 'Domingo'}
print("\n\nDiccionario completo:")
print(dias)

print("\nAccesos específicos:")
print("Valor de la llave 1 (usando []):", dias[1])
print("Valor de la llave 7 (usando []):", dias[7])
print("Valor de la llave 5 (usando get()):", dias.get(5))
print("Valor de la llave 7 (usando get()):", dias.get(7))

print("\n\nDiccionario final:")
print(dias)
