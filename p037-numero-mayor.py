# p037-numero-mayor.py
# Objetivo: Identificar el número mayor

print("-"*60)
print("Identificando cual es el numero mayor")
print("-"*60)

# Entrada de datos
print("dame tres numero enteros")
n1 = int(input("numero 1 ?"))
n2 = int(input("numero 2 ?"))
n3 = int(input("numero 3 ?"))

#Proceso
if n1 > n2:
    if n1 > n3:
        print(f"{n1} es el numero mayor")

if n2 > n1:
    if n2 > n3:
        print(f"{n2} es el numero mayor")

if n3 > n1:
    if n3 > n2:
        print(f"{n3} es el numero mayor")

print("Proceso terminado")