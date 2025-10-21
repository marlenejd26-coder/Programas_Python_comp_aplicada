# p099-procesar-notas.py
# Objetivo: Leer un numero indeterminado de notas en un rango entre 0 y 100
#Procesa calificaciones en un alumno, usando una lista

print('\033[H\033[J')
print('Procesar las calificaciones de un alumno\n')

calificaciones = []

while True:
    try:
        cal = float(input("Calificación > "))
        if cal == 99: break
        if 0 <= cal <= 10:
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
    mayores_promedio = []
    for cal in calificaciones:
        if cal > promedio: 
            mayores_promedio.append(cal)

print(f"\nSe capturaron {len(calificaciones)} calificaciones.")
print(f"Las calificaciones fueron: {calificaciones}")
print("\n--- Estadísticas del Curso ---")
print(f"Suma : {suma}")
print(f"Promdio : {promedio}")
print(f"Calificaciones mayores al promedio: {len(mayores_promedio)} y son {mayores_promedio}")
print(f"Calificación más alta: {max(calificaciones)}")
print(f"Calificación más baja: {min(calificaciones)}")