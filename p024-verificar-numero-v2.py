# p024-verificar-numero-v2.py
# Objetivo:verifica si un número es positivo, negativo o cero

print("verificando si un numero es positivo, negativo o cero")

#Entrada
print("Dame un numero entero ?")
numero=int(input())

#Proceso o la toma de decision
if numero==0:
	print("el numero es CERO ")
else:
	if numero <0:
		print ("El numero es NEGATIVO ")
	else: print("el numero es POSITIVO ")