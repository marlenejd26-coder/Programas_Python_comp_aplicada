# p101-mes-día-nombre.py
# Objetivo: Imprimir el nombre del mes y la cantidad de días del mes correspondiente

print('\033[H\033[J')
print("Imprimir el nombre del mes y la cantidad de días del mes correspondiente")

mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Obtubre", "Noviembre", "Diciembre"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
num = int(input("Introduzca un número de mes (1-12): "))

if  1 <= num <= 12:
    for i in range(12):
        if i == num - 1:
            print(f'Mes: {mes[i]}')
            print(f'Días: {dias[i]}')
else:
    print("Mes inválido")
    


