# p061-suma-200.py
# Objetivo: Leer números y sumarlos hasta que el total acumulado sea mayor o igual a 200.

print("Leyendo números y sumarlos hasta que el total acumulado sea mayor o igual a 200")

cuenta = 0
suma = 0

while True:
    num = int(input(f"Suma actual: {suma}. Introduce un número "))
    if suma >= 200:
        break

    cuenta+=1
    suma += num

# Proceso
cuenta += 1
num += suma

print("\n----------------------------------")
print("Meta de 200 alcanzada")
print(f" Suma final {suma}")
print(f" Total de numeros introducidos {cuenta}")
