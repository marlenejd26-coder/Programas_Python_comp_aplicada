# p120-contar-caracteres.py
# Objetivo: Mostrar un diccionario resultante con el conteo de caracteres.

print('\033[H\033[J')
print("Mostrar un diccionario resultante con el conteo de caracteres")

cadena = input("\nIngrese una cadena: ")
frecuencia = {}

# Iterar sobre cada carácter
for caracter in cadena:
    if caracter in frecuencia:
        frecuencia[caracter] += 1 
    else:
        frecuencia[caracter] = 1 

print("\nResultado:")
print(frecuencia)