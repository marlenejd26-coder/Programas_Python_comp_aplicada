# p039-numeros-romanos.py
# Objetivo: Mostrar el equilvalente en numeros romanos del numero ingresado

print("-"*60)
print("Mostrando el equivalente en numero romando del numero ingresado")
print("-"*60)

#Entrada de datos
numero = int(input("ingresa un numero del 1 al 10: "))

if numero <= 10 :
    if numero >= 1:
        if numero == 1:
            print ("I")
        if numero == 2:
            print ("II")
        if numero == 3:
            print ("III")
        if numero == 4:
            print ("IV")
        if numero == 5:
            print ("V")
        if numero == 6:
            print ("VI")
        if numero == 7:
            print ("VII")
        if numero == 8:
            print ("VIII")
        if numero == 9:
            print ("IX")
        if numero == 10:
            print ("X")
    else:
        print("numero inválido")
else:
        print("numero inválido")


print ("Fin del programa")