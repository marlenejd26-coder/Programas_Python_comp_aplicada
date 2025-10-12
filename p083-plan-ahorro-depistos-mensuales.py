# p083-plan-ahorro-depistos-mensuales.py
# Objetivo: Simular un plan de ahorro

while True:
    print('\033[H\033[J')
    print("Comparar el crecimiento de dos fondos de inversión a lo largo de varios años")

    n1 = int(input("ingresa monto inicial de ahoro "))
    dep = int(input("ingresa el deposito mensual "))
    tasa1 = float(input("ingresa la tasa de interes mensual : "))
    tasat1= tasa1/100
    meses = int(input("Ingresa numero de meses: "))

    print (f"Monto inicial de ahorro {n1}")
    print (f"Deposito mensual {dep}")
    print (f"Tasa de interés mensual \(%): {tasa1}")
    print (f"Numero de meses a simular {meses}")
    
    print ("\n --- Plan de ahorro detallado --- ")

    for i in range (1, meses+1):
        dept=dep*i
        nt1= n1+dept
        tasat = nt1*tasat1
        nt = nt1+tasat
        print(f"Mes {i}  |Saldo inicial {nt1:,.2f}  |Interes{tasat:,.2f}  |Saldo final {nt:,.2f}")

    break
      

print(f"Al final de {meses}, tendrás {n1} ")
