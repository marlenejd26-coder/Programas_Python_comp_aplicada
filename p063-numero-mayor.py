# p063-numero-mayor.py
# Objetivo: Leer na serie de numeros introducidos y determinar cual es el mayor

print("Leyendo numeros introducidos para obtener el mayor")

mayor = 0
num = 0

while True:
    num=int(input("Introduce un numero (0 para terminar): "))
    if num == 0:
        print ("El proceso a terminado")
        print(f"El número mayor fue: {mayor}")
        if input ("Deseas continuar (S/N): ").upper() != "S": break
        break
        
    if num > mayor:
        mayor=num



