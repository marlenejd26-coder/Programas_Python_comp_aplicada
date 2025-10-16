# p096-registro-estudiantes.py
# # Registro y análisis de asistentes a un evento

print('\033[H\033[J')
print('Sistema de Registro para Evento\n')

print("Introduce los nombres y edades de los asistentes (* para terminar)\n")

# Listas paralelas para almacenar los datos
nombres = []
edades = []

# Ciclo para la captura de datos
while True:
    nombre = input("Nombre del asistente: ")
    if nombre == "*": break # Termina el ciclo si el nombre es *
    try: 
        edad = int(input(f"Edad : "))
        nombres.append(nombre) # Agrega el nombre a la lista
        edades.append(edad) # Agrega la edad en la misma posición
    except ValueError:
        print("Valor erroneo")

# --- Generación de Reportes ---
if not nombres:
    print("\nNo hay datos para procesar.")
else:
# 1. Reporte de asistentes mayores de edad
    print("\n--- Asistentes Mayores de Edad ---")
    encontrados = False
    for i in range(len(nombres)):
        if edades[i] >= 18:
            print(f"Nombre: {nombres[i]}, Edad: {edades[i]}")
            encontrados = True
    if not encontrados:
        print("No hay mayores de edad.")

# 2. Reporte del asistente con mayor edad
edad_maxima = max(edades)
pos_max = edades.index(edad_maxima) # Encuentra la primera ocurrencia de la edad máxima
nombre_max = nombres[pos_max]

print("\nEl reconocimiento a la persona de Mayor Edad es para ")
print(f"Nombre: {nombre_max} con edad {edad_maxima} años.")