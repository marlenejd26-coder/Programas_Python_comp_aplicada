# p059-pares-descendente.py
# Objetivo: Imprimir los números pares y su suma descendente desde 100 hasta un número n

print ("Imprimiendo los números pares y su suma descendente desde 100 hasta un número n")

n = int(input("Introduce un numero limite (menor a 100) "))
c = 100
suma = 0

while c >= n:
    if c % 2 == 0:
        print(f" {c}", end="") #para que no se salte la línea
        suma += c
    c -= 1
print(f"\n La suma total de los números impares es {suma}")