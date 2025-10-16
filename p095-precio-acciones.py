# p095-precio-acciones.py
# Análisis básico de protafolio de acciones
# Funciones max, index

print('\033[H\033[J')
print(" Encontrar las acciones mas altas y mas baja en una semana")

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado"]
precios = [150.25, 152.50, 149.75, 155.00, 153.20, 100.00]

# Encontrar el precio máximo y mínimo y en que día
precio_max = max(precios)
precio_min = min(precios)

# Encontrar la posición (el día) de esos precios
pos_max = precios.index(precio_max)
pos_min = precios.index(precio_min)

print(f"Precios de las acciones de la semana: {precios}")
print(f"Días: {dias}")
print(f"El precio más alto fue ${precio_max} el día {dias[pos_max]}.")
print(f"El precio más bajo fue ${precio_min} el día {dias[pos_min]}.")