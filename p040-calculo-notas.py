# p040-calculo-notas.py
# Objetivo: Calcular el promedio de 5 calificaciones y mostrar un mensaje de acuerdo a la calificación 

print("-"*60)
print("Calculando el promedio de 5 calificaciones y mostrar un mensaje")
print("-"*60)

#Entrada de datos
print("Ingresa las calificaciones")
c1 = float(input("calificación 1 ?"))
c2 = float(input("calificación 2 ?"))
c3 = float(input("calificación 3 ?"))
c4 = float(input("calificación 4 ?"))
c5 = float(input("calificación 5 ?"))

#Proceso
promedio = (c1+c2+c3+c4+c5)/5

if promedio < 6:
    print(f"Tu promedio es {promedio} Quedas reprobado")
else:
    if promedio < 7:
        print(f"Tu promedio es {promedio} Pasas de panzaso")
    else:
        if promedio < 8:
            print(f"Tu promedio es {promedio} Muy bien, puedes mejorar")
        else:
            if promedio == 8 < 9:
                print(f"Tu promedio es {promedio} Excelente, sigue así")
            else:
                if promedio == 9:
                    print(f"Tu promedio es {promedio} Perfecto, tu esfuerzo valió la pena")
                if promedio == 10:
                    print(f"Tu promedio es {promedio} Perfecto, tu esfuerzo valió la pena")

print ("Fin del programa")