# p028-retira-cuenta.py
# Objetivo:simula el retiro de dinero de una cuenta de ahorros revisa el saldo

saldo_actual = 15000.00
print ("Simulacro de retiro")

print (f"tu saldo inicial es de {saldo_actual}")

cantidad_retiro = float(input("Cantidad a retirar : $ "))

if cantidad_retiro > 0:
	print ("procediendo con el retiro...")
	if cantidad_retiro <= saldo_actual:
		saldo_actual -= cantidad_retiro
		print("\nRetiro Exitoso")
		print(f"Tu nuevo saldo es: {saldo_actual}")
	else:
		print("\n Fondos Insuficientes para completar la transaccion")
else:
	print("\nLa cantidad a retirar debe ser un numero positivo")

print ("\nProceso terminado")