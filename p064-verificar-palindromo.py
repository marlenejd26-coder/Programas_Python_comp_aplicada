# p064-verificar-palindromo.py
# Objetivo: Determinar si un numero es palindromo

print("Determinando si un numero es palindromo")

while True:
    num = input("Introduce un número para verificar si es palindromo: ")

    if num == num[::-1]:
        print(f"El número {num} es un palíndromo.\n")
    else:
        print(f"El número {num} no es un palíndromo.\n")

    if input ("Desea continuar (S/N) ? ").upper() != "S": break
