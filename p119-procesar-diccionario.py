# p119-procesar-diccionario.py
# Objetivo: Definir dos listas y procesar diccionario

print('\033[H\033[J')
print("Definir dos listas y procesar diccionario")

# Definir las listas
nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

# Combinar diccionario
nomina = dict(zip(nombres, sueldos))
print("Diccionario de nomina:")
print(nomina)

# Mostrar llaves
print("\n--- Iterando Llaves (keys) ---")
for nombre in nomina.keys():
    print(nombre)

# Mostrar valores
print("\n--- Iterando Llave y Valor (accediendo por llave) ---")
for sueldo in nomina.values():
    print(sueldo)

# 4. Mostrar llave y valor
print("\n--- Iterando Llave y Valor (items) ---")
for nombre, sueldo in nomina.items():
    print(f"{nombre}: {sueldo}")

# Suma y promedio
suma_sueldos = sum(nomina.values())
promedio_sueldos = suma_sueldos / len(nomina)
print("\n--- Cálculos ---")
print(f"Suma total de sueldos: {suma_sueldos:.2f}")
print(f"Promedio de sueldos: {promedio_sueldos:.2f}")