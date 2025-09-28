# p018-volumen-cilindro.py
# Objetivo: Calcular el área y volumen de un cilindro  

import math
print('Calculando el area y volumen de un cilindro\n')

#Entrada de datos:
radio = float(input("Ingresa el radio: "))
altura = float(input("Ingresa la altura: "))

#Cálculo de área y volumen:

area = math.pi * radio * (radio + altura)
volumen = math.pi * math.pow(radio,2) * altura

#Mostrar resultados:
print(f"El cilindro de radio {radio:.2f} y altura {altura:.2f} tiene un area de {area:.2f} y un volumen {volumen:.2f}")