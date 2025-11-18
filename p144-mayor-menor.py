# p144-mayor-menor.py
# Objetivo: 

from typing import List

def mayor(lista:List[float]) -> float:
    num_mayor = lista[0]
    for numero in lista:
        if numero > num_mayor:
            num_mayor = numero
    return

def menor(lista:List[float]) -> float:
    num_menor = list[0]
    for numero in lista:
        if numero < num_menor:
            num_menor = numero
    return

def captura_datos() -> List[float]:
    datos : List[float] = []
    print("Ingrese un numero (fin para terminar)")
    while True:
        entrada = input("Numero: ")
        if entrada.lower() == "fin" : break
        try:
            numero = float(entrada)
            datos.append(numero)
        except ValueError:
            print("Debe ser numero")
    return datos

def main() -> None:

    # numeros : List[float] = [20, 50, 80, 100, 10, 4, 25]
    numeros : List[float]= captura_datos()

    if numeros:
        
        num_menor = menor(numeros)
        num_mayor = mayor(numeros)

        print(f"Numeros ingresados: {numeros} - {len(numeros)}")
        print(f"El menor es: {num_menor}")
        print(f"El mayor es: {num_mayor}")

if __name__ == "__main__":
    main ()