# p019-calculo-tiempo.Py
# Objetivo: Tomar una cantidad de horas y mostrar su equivalente en días, minutos y segundos

print("Conversor de tiempo:\n")

#Entrada de datos
horas = int(input("Ingresa tiempo en horas: "))

#Cálculo de tiempo
dias = horas/24
minutos = horas*60
segundos = minutos*60

#Mostrar resultados
print(f"{horas:.2f}Horas equivale a {dias:.2f} días, {minutos:.2f} minutos y {segundos:.2f} segundos")