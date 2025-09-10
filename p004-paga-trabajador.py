# p004-paga-trabajador.py
# Objetivo: Calcula la paga de un trabajador

print ("calculando la paga de un trabajador \n")

#Entrada
nombre = input("Nombre: ")
horas = int (input("Horas: "))
paga = float (input("Paga x hora: "))

#Proceso
tasa = 0.03 #impuesto de hacienda
pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

#Salida
print ("Resumen de pagos")
print (f"El trabajador {nombre}, trabajo {horas} horas, con una paga de  {paga} pesos, con una tasa de {tasa: .2%}")
print(f"Paga Bruta {pagabruta: ,.2f}")
print(f"Impuesto {impuesto: ,.2f}")
print(f"paga Neta {paganeta: ,.2f}")
