# p003-area-triangulo.py
# Objetivo: calcula el area de un triangulo

print("calculando el area de un triangulo: \n")

#Entrada
print("Dame la base y la altura separados por Enter")
base, altura = int( input()), int( input()) #lee dos valores

#Proceso
area = base*altura/2 #No es necesario poner parentesis porque en la logica de programacion se lee de izquierda a derecha

#Salida
print("El triangulo de base: ", base)
print("El triangulo de base: ", altura)
print("Tiene un area de: ", area)

print (f"El triangulo de base {base} y altura {altura} tiene un area de {area: ,.2f}")

print ("El triangulo de base " +str(base) + " y altura " +str(altura) + " tiene un area de " +str(area))

#las anteriores son tres formas distintas de mostrar el resultado


