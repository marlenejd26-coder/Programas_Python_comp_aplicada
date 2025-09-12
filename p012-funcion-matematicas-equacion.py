# p012-funciones-matematicas-equacion.py
# Evaluar la función f(x, y) = 3x2 + √(x2 + y2) + e^(ln(x))
# Usando operador de exponenciación (**) y función pow() de math

import math as mt # Importar la biblioteca math para funciones matemáticas con un alias

# Definir los valores de x , y para la evaluación
x = 2
y = 2

# Evaluar la función usando el operador de exponenciación (**)
fx_y_star = 3 * x**2 + mt.sqrt(x**2 + y**2) + mt.exp(mt.log(x))

# Evaluar la misma función usando la función pow()
fx_y_pow = 3 * mt.pow(x, 2) + mt.sqrt(mt.pow(x, 2) + mt.pow(y, 2)) + mt.exp(mt.log(x))

# Mostrar ambos resultados para demostrar que son idénticos
print(f"Resultado con el operador ** : {fx_y_star}")
print(f"Resultado con la función pow() : {fx_y_pow}")
