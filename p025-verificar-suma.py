# 025-verificar-suma.py
# Objetivo: Verificar si la suma de dos números es igual a un tercero

print ("-"*60)
print ("Verificar si la suma de dos números es igual a un tercero ")
print ("-"*60)

print ("\n Dame 3 numeros enteros : ")
n1 = int(input("numero 1 ?"))
n2 = int(input("numero 2 ?"))
n3 = int(input("numero 3 ?"))

#Proceso
suma = n1 + n2

if suma == n3 :
	print(f"\n !correcto! {n1}+{n2} ES IGUAL {n3} ")
else:
	print(f"\n No coinciden {n1}+{n2} NO ES IGUAL A {n3} !")


print ("-"*60)
print ("\n Fin del programa")