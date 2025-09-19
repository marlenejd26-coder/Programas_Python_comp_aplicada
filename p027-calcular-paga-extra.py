# p027-calcular-paga-extra.py
# Objetivo: Calcula la paga de un trabajador, considerando las horas extras (se pagan al doble)

print("\033[2J\033[H")
print("Calculando la paga extra de un trabajador")

print ("introduce los datos del trabajador")
nombre = input ("Nombre ?")
horas= int(input("Horas trabajadas ? "))
paga_hora= float(input("Paga por hora ?"))

#Proceso
paga_normal = 0
horas_normales = 40
paga_extra = 0
total = 0

if horas <= horas_normales:
      paga_normal = horas*paga_hora
      total=paga_normal
else:
	paga_normal = horas*paga_hora
	horas_extra = horas - horas_normales
	paga_extra = horas_extra * (paga_hora*2)
	total = horas_normales *paga_hora+ paga_extra

print("\nCalculo completo")
print(f"{nombre} trabajo {horas} horas, a una paga de {paga_hora} pesos por hora")
print(f"Paga normal  : ${paga_normal:}")
print(f"Paga extra  : $ {paga_extra:}")
print(f"Total  : $ {total}")
