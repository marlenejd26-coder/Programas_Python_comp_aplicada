# p043-adivina-numero.py
# Objetivo: Simula un juego de azar donde el usuario adivina un número entre 1 y 50 

import random

print ("\033[2J\033[H")
print ("Bienvenido al juego de Adivina número")
print ("Yo te doy un número entre 1 y 50 y tu trata de adivinarlo")

numero_secreto = random.randint(1, 50) # Se elige un número entero aleatorio entre 1 y 50.
intento_usuario = 0
contador_intentos = 0
print(" ¡Bienvenido al juego 'Adivina el Número'! ")
print("He pensado en un número entre 1 y 50. ¿Podrás adivinarlo?")
print("------------------------------------------------------")
# Usamos 'while True' para que el juego continúe hasta que adivinemos el número y rompamos el ciclo con 'break'.

while True:
    intento_usuario = int(input("Tu número: "))
    contador_intentos += 1

    if intento_usuario < numero_secreto:
        print(" ¡Demasiado bajo! Intenta un número más alto.")
    elif intento_usuario > numero_secreto:
        print(" ¡Demasiado alto! Intenta un número más bajo.")
    else:
# Si no es ni más bajo ni más alto, ¡es el correcto!
        print(f"\n ¡Felicidades! ¡Adivinaste el número secreto era {numero_secreto}!")
        print(f"Lo lograste en {contador_intentos} intentos.")
        break

print ("\nHaya sido como haya sido ya terminamos")