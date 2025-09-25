# p040-multiplos-continue.py
# Ojetivo: Imprime solo los múltiplos de 10 hasta 200.

print(" Buscando múltiplos de 10 entre 1 y 200...")

c = 0

while c < 200:
    c += 1
    if c % 10 != 0:
        continue # "Ignora todo lo que sigue y salta a la siguiente iteración".
    #Solo se ejecuta si el número es múltiplo de 10 
    print(f" {c}", end=" ")

print("\n Búsqueda terminada.")