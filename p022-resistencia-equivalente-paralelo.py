# p022-resistencia-equivalente-paralelo.py
# Objetivo: calcular la resistencia total o equivalente de un circuito con cuatro resistencias en paralelo.

import math
print ("calculando la resistencia total o equivalente de un circuito con cuatro resistencias en paralelo.")

# Definir los valores de las 4 resistencias
print("Escribe los valores de las cuatro resistencias, separados por un espacio: ")
R1, R2, R3, R4 = input().split()
R1, R2, R3, R4 = float(R1), float(R2), float(R3), float(R4)

# Calculando resistencia total
resistencia_total = 1/((1/R1) + (1/R2) + (1/R3) + (1/R4))

print(f"La resistencia total es : {resistencia_total:.2f}")