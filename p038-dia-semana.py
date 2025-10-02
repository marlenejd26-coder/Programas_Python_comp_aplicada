# p038-dia-semana.py
# Objetivo: Mostrar el día de la semana correspondiente al número ingresado

print("-"*60)
print("Mostrando el día de la semana correspondiente al numero ingresado")
print("-"*60)

#Entrada de datos
numero = int(input("ingresa un numero del 1 al 7: "))

if numero <= 7 :
    if numero == 1:
        print ("El numero ingresado corresponde al día domingo")
    if numero == 2:
        print ("El numero ingresado corresponde al día lunes")
    if numero == 3:
        print ("El numero ingresado corresponde al día martes")
    if numero == 4:
        print ("El numero ingresado corresponde al día miercoles")
    if numero == 5:
        print ("El numero ingresado corresponde al día jueves")
    if numero == 6:
        print ("El numero ingresado corresponde al día viernes")
    if numero == 7:
        print ("El numero ingresado corresponde al día sabado")
else:
    print("Día inválido")

print ("Fin del programa")