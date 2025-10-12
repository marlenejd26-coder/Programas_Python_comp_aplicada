# p082-compara-rendimiento-inversion.py
# Objetivo: Comparar el crecimiento de dos fondos de inversión a lo largo de varios años

while True:
    print('\033[H\033[J')
    print("Comparar el crecimiento de dos fondos de inversión a lo largo de varios años")

    n1 = int(input("ingresa monto inicial para fondo de inversion A "))
    tasa1 = float(input("ingresa la tasa de interes anual : "))
    tasat1= tasa1/100+1

    n2 = int(input("ingresa monto inicial para fondo de inversion B "))
    tasa2 = float(input("ingresa la tasa de interes anual : "))
    tasat2= tasa2/100+1
   
    anios = int(input("años a proyectar: "))

    print ("\n --- Fondo de inversión A --- ")
    print (f"Monto inicial {n1}")
    print (f"Tasa de interés anual \(%): {tasa1}")
    
    print ("\n --- Fondo de inversión B --- ")
    print (f"Monto inicial {n2}")
    print (f"Tasa de interés anual \(%): {tasa2}")
    
    print (f"Años a proyectar {anios}")
    print ("\n --- Comparación de Rendimientos Anuales --- ")
    print ("Año  |  Fondo A     |  Fondo B  ")

    for i in range (1, anios+1):
        n1 *= (tasat1)
        n2 *= (tasat2)
        print(f"{i}  |{n1:,.2f}     |{n2:,.2f}")

    break
      
if n1>n2:
    print(f"Resultado final: El Fondo A {n1:,.2f} superó al Fondo B {n2:,.2f}.")
else:
    print (f"Resultado final: El Fondo B {n2:,.2f} superó al Fondo A {n1:,.2f}.")
