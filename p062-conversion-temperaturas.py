# p062-conversion-temperaturas.py
# Objetivo: mostrar la conversión de grados Celcius a Fahrenheit para cada grado introducido

print ("Mostrar la conversión de grados Celcius a Fahrenheit para cada grado introducido")

t1 = float(input("Ingresa la temperatura inicial en °C: "))
t2 = float(input("Ingresa la temperatura final en °C: "))

while t1 <= t2:
    farenheit = (t1 * 9/5) + 32
    print(f"{t1}°C = {farenheit}°F")
    t1 += 1
