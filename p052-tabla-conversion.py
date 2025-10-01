# p052-tabla-conversion.py
# Objetivo: Muestra una tabla de conversion de Peso a Dollar

tc = 20.71
while True :
    print("\033[H\033[J")
    print("Tabla de Conversion Peso a Dollar")
    print(f"Tipo de Cambio: {tc} Pesos por Dollar")
    print("-"*15)

    while True:
        pi = float(input("Valor inicial: "))
        pf = float(input("Valor final : "))
        if (pi>0 and pf>0) and pi<pf:
            break
        print("Error en los valores, intente de nuevo")
    c = pi
    print("\nPesos\tDollar")
    print("-"*15)
    while c<=pf :
        print(f'{c}\t{c/tc:.2f}')
        c+=1
    print("-"*15)
    
    res=input('Deseas Continuar(S/N)? ').upper()
    if res=='N':
        break