# p147-aleatorios.py
# Objetivo: Genera dos listas con numeros aleatorios y los suma en una tercera

import random
from typing import List

def genera_aleatorios(n:int, min:int, max:int) -> List[int]:
    nums : List[int] = []
    for _ in range(n):
        num = random.randint(min, max)
        nums.append(num)
    return nums

def suma_listas(l1:List[int], l2:List[int]) -> List[int]: #Se puede omitir el tipo de variable
    suma : List[int] = []
    for i in range(len(l1)):
        s = l1[i] + l2[i]
        suma.append(s) #Se agregan a la tercera lista
    return suma

def main() -> None:
    MAX = 10

    lista1 : List[int] = genera_aleatorios(MAX, 1, 100)
    lista2 : List[int] = genera_aleatorios(MAX, 50, 70)
    lista3 : List[int] = suma_listas(lista1, lista2)

    print(f"Lista 1: {lista1} - {len(lista1)}")
    print(f"Lista 2: {lista2} - {len(lista2)}")
    print(f"Lista 3: {lista3} - {len(lista3)}")

if __name__ == "__main__":
    main ()

# Cuando hay mas de 5 lineas se recomienta usar main