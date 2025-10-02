# p036-numeros-consecutivos.py
# Objetivo: Determinar si los números son consecuitivos

print("-"*60)
print("Determinando si los números son consecutivos")
print("-"*60)

#Entrada
print("dame tres numero enteros")
n1 = int(input("numero 1 ?"))
n2 = int(input("numero 2 ?"))
n3 = int(input("numero 3 ?"))

#Proceso
if n3 > n2 > n1:
	print("Los numeros son consecutivos 😊")
else: 
	print ("Los numeros no son consecutivos ☹️")
	

print("Fin del programa")
