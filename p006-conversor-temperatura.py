# p006-conversor-temperatura.py
# Objetivo: Convertir grados celcius a farenheit

print ("Conversor de temperatura (Celcius-Farenheit) \n")

celcius = float(input("Ingresa la temperatura en Celcius: "))
farenheit = (celcius * 9/5) + 32

print(f"{celcius} grados celcius quivale a {farenheit: .2f} farenheit")
