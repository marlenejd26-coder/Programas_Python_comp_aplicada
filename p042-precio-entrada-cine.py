# p042-precio-entrada-cine.py
# Objetivo: Mostrar precio correspondiente segun la edad para entrada a cine

print("Mostrando precio correspondiente segun la edad para entrada a cine")

edad=int(input("ingresa tu edad: "))

if edad <= 5:
    print("Tu entrada es gratis")

if edad > 5 and edad <= 12:
    print("El precio de tu entrada es de $5 ")

if edad > 12 and edad <= 64:
    print("El precio de tu entrada es de $10 ")

if edad > 65:
    print("El precio de tu entrada es de $7 ")

print ("Fin del programa")