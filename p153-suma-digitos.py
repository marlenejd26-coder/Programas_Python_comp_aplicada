# p153-suma-digitos.py
# Objetivo: Procesa una lista de números

def leer_lista():
    lista = []
    cantidad = int(input("¿Cuántos números deseas ingresar? "))
    for i in range(cantidad):
        num = int(input(f"Dame los números (separados por enter):{i+1}: "))
        lista.append(num)
    return lista

def suma_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma

def procesar_lista(lista):
    nueva_lista = []
    for n in lista:
        nueva_lista.append(suma_digitos(n))
    return nueva_lista

def main():
    lista_original = leer_lista()
    lista_sumas = procesar_lista(lista_original)

    print("\nLa lista de números original", lista_original)
    print("La lista con las suma de dígitos de los números:", lista_sumas)


# Ejecutar programa
main()