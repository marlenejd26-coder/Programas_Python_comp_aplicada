# p060-promedio-suma.py
# Objetivo: Leer números introducidos por el usuario hasta que ingrese un 0.

print ("Leyendo números introducidos por el usuario hasta que ingrese un 0.")

cuenta = 0
suma = 0
promedio = 0

while True:
    num = int(input("Introduce numeros (0 para terminar) "))
    if num == 0:
        break

    cuenta+=1
    suma += num

# Proceso
cuenta += 1
suma += num
promedio = suma/cuenta

print("\n=================================")
print(f" Se introdujeron {cuenta} numeros")
print(f" La suma es: {suma}")
print(f" El promedio es: {promedio}")
print("===================================")