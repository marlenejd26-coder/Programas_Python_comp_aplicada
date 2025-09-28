#p029-calculadora-descuento.py
#Objetivo: simula una calculadora de descuentos en base al monto de compra

compra=descuento=porcentaje=0 #En python se pueden declarar varias variables a la vez

print("\033[2J\033[H")
print ("Calculadora de descuentos")

compra=float(input("Ingresa el total de la compra: $ "))

if compra > 2000:
	porcentaje = 0.20
else:
	if compra > 1000:
		porcentaje = 0.10
	else:
		if compra > 500:
			porcentaje=0.05
		else:
			porcentaje=0

descuento=compra*porcentaje
total=compra - descuento

print ("Resumen Final")
print (f"Total de la compra.	:{compra}")
print (f"Porcentaje de descuento :{porcentaje:.2f}")
print (f"Descuento.		 :{descuento}")
print (f"Total a pagar		 :{total}")

print ("\nProceso Terminado")
