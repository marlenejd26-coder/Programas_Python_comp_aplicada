# p002-area-circulo
# Objetivo: calcula el area de un circulo - area = PI * r * r

import math #importamos el modulo math para constantes y funciones matematicas

print("Calculando el area de un circulo: \n")

#Entrada
print("Dame el radio: ")
radio = float( input() )

#Proceso
area = math.pi * math.pow(radio, 2)
print(f"el circulo de radio {radio: .2f} tiene un area de: {area: ,.2f}")

      
