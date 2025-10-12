# p084-cuadro-hueco-caracter.py
# Objetivo: Imprimir un cuadrado del caracter deseado

print('\033[H\033[J')
print("Imprime un cuadrado de n renglones y del caracter deseado")

n = int (input("¿De qué tamaño será el lado del cuadrado? "))
c = str (input ("Qué carácter quieres usar? "))

for i in range (n):
    if i == 0 or i == n - 1:
        print(c * n)
    else:
        print(c + ' ' * (n - 2) + c)
    
    print()
