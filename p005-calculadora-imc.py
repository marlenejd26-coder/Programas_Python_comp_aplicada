# p005-calculadora-imc.py
# Objetivo: Calcular el IMC

print ("Calculando el indice de masa corporal (IMC) \n")

#Entrada
peso_kg = float(input("Ingresa tu peso en kilogramos: "))
altura_m = float(input("Ingresa tu altura en metros: "))

#Proceso
imc = peso_kg / (altura_m ** 2) #** eleva a la potencia del numero
#los nombres de variables mayusculas suelen usarse para constantes

#Salida - otra forma de realizar la operacion
print ("El peso es {0: .2f}kg y la altura es {1: 2f}m, y resulta en un IMC de {2: .2f} ".format(peso_kg, altura_m, imc)) 
# en esta funcion cada dato es un numero, el primer dato es 0 y el segundo 1
