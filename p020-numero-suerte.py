# p020-numero-suerte.py
# Mostrar y sumar dígitos individuales de año de nacimiento

print("Muestra y suma digitos individuales a partir de tu año de namcimiento")

print("Escribe tu fecha de nacimiento separando cada digito con un espacio: ")
n1, n2, n3, n4 = input().split()

n1, n2, n3, n4 = int(n1), int(n2), int(n3), int(n4)
print ("Los digitos individuales son: ")
print (n1, n2, n3, n4)

suma = n1 + n2 + n3 + n4
print(f" La suma de los digitos {n1}, {n2}, {n3} y {n4} da como resultado {suma}")
