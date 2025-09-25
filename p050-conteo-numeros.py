# p042-conteo-numeros.py
# Lee números hasta ingresar 999, luego, muestra un resumen estadístico

print ("\033[2J\033[H")
print ("Estadísticas con números que el usuario proporciona")

cuenta = 0
suma = 0
cp = cn = cz = 0
cuenta_negativos = 0
cuenta_ceros = 0
while True:
    num = int(input("Introduce un número entero ?"))
    if num == 999:
        print("Detectando sentinela 999, me voy...")
        break
        
    cuenta+=1
    suma += num


print(" Analizador de Números (escribe 999 para finalizar) ")
while True:
    num = int(input('Introduce un número entero: '))
    if num == 999: # Condición de salida
        print("Detectado código de salida (999)")
        break # Rompe el ciclo infinito.

# Proceso
cuenta += 1
suma += num
if num > 0:
     cp += 1
elif num < 0:
    cn += 1
else:
    cz+= 1

print("\n========== RESUMEN FINAL ==========")
print(f" Números introducidos: {cuenta}")
print(f" La suma es: {suma}")
print(f" Positivos: {cp}")
print(f" Negativos: {cn}")
print(f" Ceros: {cz}")
print("===================================")