# p152-suma-pares-impares.py
# Objetivo: Sumar números pares o impares dentro de un rango especificado.

def sumar_rango (inicio, fin, tipo):
    suma = 0
    for numero in range(inicio, fin + 1):
        if tipo == 'P' and numero % 2 == 0:
            suma += numero
        elif tipo == 'I' and numero % 2 != 0:
            suma += numero
    return suma

def main():
    while True:
        print("\n*** Suma en Rango ***")
        opcion = input("¿Qué deseas sumar? (P)ares o (I)mpares: ")

        if opcion in ("P", "I"):
            inicio = int(input("Introduce el número inicial: "))
            fin = int(input("Introduce el número final: "))

            if opcion == "P":
                resultado = sumar_rango(inicio, fin, 'P')
                print(f"La suma de los números pares entre {inicio} y {fin} es: {resultado}")
            else:
                resultado = sumar_rango(inicio, fin, 'I')
                print(f"La suma de los números impares entre {inicio} y {fin} es: {resultado}")

main()