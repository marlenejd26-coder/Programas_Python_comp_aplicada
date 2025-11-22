# p154-calcula-factoriales.py
# Objetivo: Desarrollar un programa que calcule el factorial de cada número en una lista

def leer_lista():
    lista = []
    cantidad = int(input("¿Cuántos números deseas ingresar? "))
    for i in range(cantidad):
        num = int(input(f"Ingrese el número {i+1}: "))
        lista.append(num)
    return lista

def factorial(n):
    if n < 0:
        return None  
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def procesar_lista(lista):
    nueva_lista = []
    for numero in lista:
        nueva_lista.append(factorial(numero))
    return nueva_lista


def main():
    lista_original = leer_lista()
    lista_factoriales = procesar_lista(lista_original)
    print("\nLa lista de números originales:", lista_original)
    print("La lista con los factoriales:", lista_factoriales)

main()