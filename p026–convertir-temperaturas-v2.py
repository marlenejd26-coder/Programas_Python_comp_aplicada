# p026–convertir-temperaturas-v2.py
# Objetivo:convertir temperaturas de grados Celcius a Farenheit y viceversa 

#Secuencias de escape ANSI se usan para enviar instrucciones la siguiente indica borra la pantalla

print ("Convertir de grados Celcius a Grados Farenheit")

print("[C] elcius a Farenheit")
print("[F] arenheit a Celcius")
op = input ("Elige ?").upper ()

if op=="C":
	print ("Convirtiendo de Celcius a Farenheit")
	c = float(input ("Introduce los grados Celcius ?"))
	f = (c * 9 / 5) +32
	print (f"\n {c:.2f} grados Celcius, equivale a {c:.2f} grados Farenheit")
else:
	if op=="F":
		print("Convirtiendo de Farenheit a Celcius")
		c = float(input("Introduce los grados Farenheit ?"))
		f = (c - 32) * 5/9
		print (f"\n {f:.2f} grados Farenheit, equivale a {c:.2f} grados Centigrados")
	else:
		print ("OPCION INVALIDA!!")
		