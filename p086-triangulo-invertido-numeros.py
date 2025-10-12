# p086-triangulo-invertido-numeros.py
# Objetivo: Mostrar un triángulo numérico invertido con la altura introducida.

print('\033[H\033[J')
print("Mostrar un triángulo numérico invertido con la altura introducida")

n = int(input("Dame un numero "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()