# p043-calculadora-anio-bisiesto.py
# Objetivo: Determinar si el año ingresado es bisiesto.

print("Determinando si el año ingresado es bisiesto")

anio= int(input("Ingresa el año: "))

if anio % 4 == 0 and anio % 100 != 0:
        print(f"El año {anio} es bisiesto. (Porque es divisible por 4 pero no por 100).")
elif anio % 400 == 0:
    print(f"El año {anio} es bisiesto. (Porque es divisible por 400).")
else:
    print(f"El año {anio} no es bisiesto. (Porque no es divisible por 4).")