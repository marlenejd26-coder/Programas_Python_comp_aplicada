# p066-primer-parcial.py
# Objetivo: Administrar la venta de boletos en un cine local 

print ("\033[2J\033[H")
print("\n------------------------------------------------------------")
print("Objetivo: Administrar la venta de boletos en un cine local ")
print("Nombre del Alumno: Marlene Juarez Delgado")
print("Matrícula: Asp. 108496 ")
print("Materia: Computacion aplicada ")
print("Examen: Primer Parcial ")
print("------------------------------------------------------------")

# COSTO DE BOLETOS
print ("\033[2J\033[H")
print("\n---COSTO DE BOLETOS---")
print ("Estudiante: $50")
print ("Adulto: $90")
print ("Tercera Edad: $60")
print ("Académico: $70")

print("\n\nInicio de la simulacion de ventas: ")

# --- Inicialización de Contadores y Acumuladores ---
# Aquí se declaran todas las variables que necesitarás para guardar los datos
hombres = mujeres = H = M =0
Tipo= E = est = A = ad = T = te= C = ac = 0
comprador_menor=0
promedio=suma=edad=cuenta=0
cantidad_Estudiante = cantidad_Adulto = cantidad_Tercera_Edad = cantidad_Academico = 0
total_Estudiante = total_Adulto = total_Tercera_Edad = total_Academico = 0


while True:
    edad = int(input("Ingresa tu edad: "))
    cuenta+=1
    suma += edad

    if edad >= 13:
        sexo = input("Ingresa tu sexo (H/M): ").upper()
        tipo = input("Tipo de comprador (E)studiante, (A)dulto, (T)erceraEdad, (C)Aadémico): ").upper()
        print(f"¡Bienvenido(a)! Venta registrada: Edad {edad}, Sexo {sexo}, Tipo {tipo}")

        if sexo == 'H':
            hombres += 1
        if sexo == 'M':
            mujeres += 1

        if tipo == 'E':
            est += 1

        elif tipo=='A':
            ad += 1
            
        elif tipo=='T':
            te += 1

        elif tipo=='C':
            ac += 1
            
        if input ("Otra Venta (S/N) ? ").upper() != "S": break
    else: 
        comprador_menor =+ 1
        print(f"ACCESO DENEGADO: El comprador es menor de 13 años.")
    

#Calculos
cuenta += 1
suma += edad
promedio = suma/cuenta

total_Estudiante = est*50
total_Adulto = ad*90
total_Tercera_Edad = te*60
total_Academico = ac*70

total_asistentes = est + ad + te + ac
total_recaudado = total_Estudiante + total_Adulto + total_Tercera_Edad + total_Academico


print("\n*** REPORTE FINAL DE LA FUNCIÓN ***")
      
print("\n --- Estadísticas del público --- ")
print(f" Total de Estudiantes: {est}")
print(f" Total de Adultos: {ad}")
print(f" Total de Tercera Edad: {te}")
print(f" Total de Académicos: {ac}")
print("--------------------------------------------------")
print(f" Total de Hombres: {hombres}")
print(f" Total de Mujeres: {mujeres}")
print("--------------------------------------------------")
print(f" Total de asistentes: {total_asistentes}")
print(f" Promedio de edad de asistentes:{promedio} años")
print(f" Personas rechazadas por edad {comprador_menor}")

print("\n --- Reporte de ingresos --- ")
print(f" Ingresos por Estudiantes: {total_Estudiante}")
print(f" Ingresos por Adultos: {total_Adulto}")
print(f" Ingresos por Tercera Edad: {total_Tercera_Edad}")
print(f" Ingresos por Academicos: {total_Academico}")
print("--------------------------------------------------")
print(f"TOTAL RECAUDADO: {total_recaudado}")

mensaje_rentabilidad=""
if total_recaudado >= 3500:
    mensaje_rentabilidad = "La función generó BUENAS ganancias"
elif total_recaudado >= 1500:
    mensaje_rentabilidad="La función generó ganancias MODERADAS"
else:
    mensaje_rentabilidad="La función generó BAJAS ganancias."

print("\n --- Rentabilidad --- ")
print (f"{mensaje_rentabilidad}")


# """
# Preguntas: Explica con tus palabras

# 1. Imagina que el cine decide implementar una promoción: los martes, todos los boletos de Adulto tendrán un 20% de descuento. 
# ¿Qué cambios tendrías que hacer en tu código para agregar esta funcionalidad? 
# Menciona qué nueva pregunta le harías al usuario y en qué parte del código agregarías la nueva lógica.

# [Le preguntaría al usuario "día de la función", agregaría la variable "descuento" y dentro un if==martes haría el calculo de descuento*0.80 ]

# 2. Supongamos que, al probar tu programa, el "Total Recaudado en General" siempre te da un resultado incorrecto, 
# aunque los ingresos por cada tipo de comprador parecen correctos. 
# Describe, paso a paso, qué harías para encontrar el error. 
# ¿En qué líneas específicas de tu código pondrías atención para verificar los valores y solucionar el problema?

# [Primero revisaría que no existan errores de puntuación o símbolos, después revisaría que las 
# las variables que asigné sean correctas para cada "tipo" de cliente, y finalmente revisaría 
# las lineas que contienen los contadores del tipo de comprado e ingresos, y la suma del costo e ingresos totales]
# """
