# p097-procesar-datos-sensores.py
# Simular recolección de datos de dos sensores y procesar las lecturas
import random #Para generar números aleatorios

# --- 1. Generación de Datos Simulados ---
print('\033[H\033[J')
print("Simulando la recolección de datos de dos sensores")

MAX = 10
sensor_a = []
sensor_b = []
todo = []

for _ in range(MAX): # El guío se pone si no voy a usar i
    sensor_a.append(random.randint(1, 100)) # Llena la lista del sensor A
    sensor_b.append(random.randint(1, 100)) # Llena la lista del sensor B

print("\n--- Datos Originales de los Sensores ---")
print(f"Sensor A: {sensor_a}")
print(f"Sensor B: {sensor_b}")

#Otra forma de hacer cálculo
for i in range(MAX): 
    sensor_a[i] = sensor_a[i]**2
    sensor_b[i] = sensor_b[i]**2
    todo.append(sensor_a[i] + sensor_b[i])

# --- 2. Transformación y Combinación de Datos ---
# datos_combinados = []
# for i in range(10):
# Transforma (eleva al cuadrado) el dato de cada sensor
# sensor_a_datos[i] = sensor_a_datos[i] ** 2
# sensor_b_datos[i] = sensor_b_datos[i] ** 2
# Suma los datos ya transformados y los añade a la tercera lista
# suma_transformada = sensor_a_datos[i] + sensor_b_datos[i]
# datos_combinados.append(suma_transformada)

# --- 3. Muestra de Resultados ---
print("\n--- Reporte de lecturas de sensores ---")
print(f"Sensor A: {sensor_a}")
print(f"Sensor B: {sensor_b}")
print(f"Combinado: {todo}")