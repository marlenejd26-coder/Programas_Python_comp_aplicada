# p155-estadisticas-basicas.py
# Objetivo: 

import math

def leer_lista():
    lista = []
    cantidad = int(input("¿Cuántos números deseas ingresar? "))
    for i in range(cantidad):
        num = int(input(f"Dame números (separados por enter): {i+1}: "))
        lista.append(num)
    return lista

def numero_mayor(lista):
    return max(lista)
def numero_menor(lista):
    return min(lista)
def media(lista):
    return sum(lista) / len(lista)
def varianza_poblacional(lista):
    m = media(lista)
    suma_cuadrados = sum((x - m) ** 2 for x in lista)
    return suma_cuadrados / len(lista) 
def desviacion_estandar_poblacional(lista):
    return math.sqrt(varianza_poblacional(lista))


def main():
    print("Lista de números:")
    datos = leer_lista()

    print("\nEstadísticas: ")
    print("Lista de números:", datos)
    print("La media:", media(datos))
    print("Mayor de los datos::", numero_mayor(datos))
    print("Menor de los datos:", numero_menor(datos))
    print("Varianza:", varianza_poblacional(datos))
    print("Desviación estándar:", desviacion_estandar_poblacional(datos))

main()