# p080-combina-colores.py
# Objetivo: Genera combinaciones de dos colores a partir de una lista

print("--- Generador de Combinaciones de Colores ---\n")

# Pedir al usuario que ingrese los colores y crear una lista
colores = input("Ingresa los colores separados por comas: ").strip().split(',')
print(f"\nColores base: {colores}")
print("--- Combinaciones Posibles ---")
# Bucle exterior: toma el primer color
for color1 in colores:
    # Bucle interior: toma el segundo color
    for color2 in colores:
    # Condición para evitar combinar un color consigo mismo
        if color1 != color2:

            print(f"- {color1} y {color2}")