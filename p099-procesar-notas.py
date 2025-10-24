# p099-procesar-notas.py
# Objetivo: Leer un numero indeterminado de notas en un rango entre 0 y 100

print('\033[H\033[J')
print('Leer un numero indeterminado de notas en un rango entre 0 y 100\n')

calificaciones = []

while True:
    try:
        cal = float(input("Calificación > "))
        if cal == 0: break
        if 0 <= cal <= 100:
            calificaciones.append(cal)
        else:
            print("Calificación no valida")
    except:
        print("Error: Entrada no válida.")

if not calificaciones:
    print("No se capturaron calificaciones.")
else:
    suma = sum(calificaciones)
    promedio = suma / len(calificaciones)
    menores_promedio = []
    for cal in calificaciones:
        if cal < promedio: 
            menores_promedio.append(cal)

print("\n--- Resultados ---")
print(f"\nTotal de notas introducidad {len(calificaciones)}")
print(f"Lista de notas {calificaciones}")
print(f"Suma de notas: {suma}")
print(f"Promdio de notas: {promedio}")
print(f"Nota máxima: {max(calificaciones)}")
print(f"Nota mínima: {min(calificaciones)}")
print(f"Notas menores al promedio: {len(menores_promedio)}")
print(f"Lista de notas menores al promedio: {menores_promedio}")