# p017-convertir-temperatura.py
# Objetivo: convertir temperatura de Celsius a Fahrenheit

print("Conversor de Temperatura (Celsius a Fahrenheit):\n")

celsius = float(input("Ingresa la temperatura en Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f}°F")

