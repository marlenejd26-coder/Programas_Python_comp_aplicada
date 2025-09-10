# p008-entrada-con-espacio.py
# Objetivo: Leer tres numeros enteros separados con un espacio

print("Entrada de varios valores separados por un espacio")

print("Dame tres numeros separados por espacio ")
n1, n2, n3 = input().split() #Leo una linea y la separa en base al espacio (split)
#si coloco algun caracter en el parentesis de split se pueden separar con ese caracter

n1, n2, n3 = int(n1), int(n2), int(n3)
print ("Los valores introducidos son: ")
print (n1, n2, n3)
