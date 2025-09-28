# p021-distancia-entre-puntos.py
# Objetivo: Calcular la distancia entre dos puntos en un plano cartesiano

import math as mt 
print ("Calculando la distancia entre dos puntos en un plano cartesiano")

# Definir los valores x, y para punto A
print("Escribe los valores de x-y para el punto A, separados por un espacio: ")
x1, y1 = input().split()
x1, y1 = float(x1), float(y1)

print("Ahora escribe los valores de x-y para el punto B, separados por un espacio: ")
x2, y2 = input().split()
x2, y2 = float(x2), float(y2)

# Calculando distancia
distancia = mt.sqrt((x1 - x2)**2 + (y1 - y2)**2)

print(f"La distancia entre el punto A y el punto B es : {distancia:.2f}")
