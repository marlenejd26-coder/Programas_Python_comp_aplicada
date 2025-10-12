# p082-compara-rendimiento-inversion.py
# Objetivo: Comparar el crecimiento de dos fondos de inversión a lo largo de varios años

while True:
    print('\033[H\033[J')
    print("Comparar el crecimiento de dos fondos de inversión a lo largo de varios años")

    n = int(input("ingresa monto inicial ? "))
    suma = 0
    numeros = ""

    for i in range (1, n+1):
        c = int(input(f"Tasa de interes anual {i} : "))
        suma += c
        numeros = numeros + str(c) + ""

    print (f"Imprime numeros en forma de cadena: {numeros}")
    print (f"La tasa de inerés anual es: {suma}")
    print (f"El promedio es: {suma/n}")

    if input("\n\nDeseas continuar (S/N)").upper()=="N": break
print ("\nProceso terminado")