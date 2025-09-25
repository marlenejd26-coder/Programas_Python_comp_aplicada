# p038-conteo-descendente.py
# Objetivo: Imprime los números de 100 a 1 usando un ciclo while

print ("\033[2J\033[H")
print (" Iniciando cuenta regresiva...")

c = 100

while c >= 1:
    print(f" {c}", end="")
    c -= 1

print("\n ¡Despegue!")