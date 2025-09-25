# p037-conteo-ascendente-v2.py
# Objetivo: Imprime los números de 1 a n en incrementos de m, usando un ciclo while

print ("\033[2J\033[H")
print("iniciando secuencia ascendente...")

n = int(input("Hasta donde ? "))
m = int(input("De cuanto en cuanto ? "))
c = 1
while c <= n:
    print(f" {c}", end="")
    c += m
print("\n ¡Secuencia completada!")