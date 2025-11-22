# p149–numero-menor.py
# Objetivo: Solicitar tres números al usuario y devolver el menor 

def numero_menor (n1: int, n2: int, n3: int) -> int:
    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    return menor

print('Dame tres numeros enteros separados por enter:')
a = int(input())
b = int(input())
c = int(input())
print(f'El número menor es: {numero_menor(a, b, c)}')

