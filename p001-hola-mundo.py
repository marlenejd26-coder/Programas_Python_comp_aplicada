# p001-hola-mundo
# Objetivo: lee datos y envia un saludo

print("leyendo datos y enviando un saludo: \n")

nombre = input("Dame tu nombre: ")
edad = int( input("Edad: "))
peso = float( input ("Dame tu peso: "))

print(f"{nombre} Bienvenid@ a python, tu edad es {edad}, tu peso es {peso} \n")

print( type(nombre) )
print( type(edad) )
print( type(peso) )

