# p016-tercer-angulo.py
# Objetivo: encontrar el ángulo faltante de un triángulo 

print("Encontrando el angulo faltante de un triangulo")

angulo1 = float(input("Ingresa la medida del angulo1 en grados: ")) 
angulo2 = float(input("Ingresa la medida del angulo2 en grados: ")) 


angulo3 = 180 - (angulo1 + angulo2)

print(f"El triangulo con medida de angulo1 de {angulo1} grados y angulo2 de {angulo2} grados tiene una angulo3 de {angulo3 :.2f} grados")
