# p104-lista-impares.py

# Objetivo: Imprimir los números impares y su suma ascendente desde 1 hasta un número n

print("Imprimiendo los números impares y su suma ascendente desde 1 hasta un número n")

n = int(input("Hasta cual numero desdea imprimir? "))
c = 1
m = 1
suma = 0

while c <= n:
    if m % 2 != 0:
        m += 1
    print(f" {c}", end="") #para que no se salte la línea
    suma += c
    c += m
    
print(f"\n La suma total de los números impares es {suma}")

