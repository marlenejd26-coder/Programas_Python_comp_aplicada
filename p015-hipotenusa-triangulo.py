# p015-hipotenusa-triangulo.py
# Objetivo: calcular la longitud de la hipotenusa de un triángulo rectángulo.

import math

print("Calculando la longitud de la hipotenusa de un triángulo rectángulo")

longlado1 = float(input("Ingresa la longitud del cateto 1: ")) 
longlado2 = float(input("Ingresa la longitud del cateto 2: ")) 

hipotenusa = math.sqrt( longlado1*longlado1 + longlado2*longlado2 )

print(f"El triangulo con cateto1 de longitud {longlado1} y cateto2 de longitud {longlado2} tiene una hipotenusa de {hipotenusa :.2f}")
