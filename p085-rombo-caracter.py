# p085-rombo-caracter.py
# Objetivo: Imprime un rombo de caracteres

print('\033[H\033[J')
print("Imprimir un rombo de n altura con el caracter deseado")
while True:
    n = int(input("Dame un numero impar para la altura: "))
    c = input("Ingrese el carácter con el que desea dibujar el rombo: ")

    for i in range(n // 2 + 1):
        espacio = (n // 2) - i
        caracter = 2 * i + 1
        print(' ' * espacio + c * caracter)

    for i in range(n // 2 - 1, -1, -1):
        espacio = (n // 2) - i
        caracter = 2 * i + 1
        print(' ' * espacio + c * caracter)

    break