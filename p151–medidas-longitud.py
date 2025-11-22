# p151–medidas-longitud.py
# Objetivo: Conversor de unidades de longitud.

# Pulgadas a centimetros
def pulgadas_a_centimetros(pulgadas):
    return pulgadas * 2.54

# Metros a pies
def metros_a_pies(metros):
    return metros * 3.281

def main():
    while True:
        print("\n*** Conversor de unidades ***")
        print("1. Pulgadas a centímetros")
        print("2. Metros a pies")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            pulgadas = float(input("Ingresa la cantidad en pulgadas: "))
            resultado = pulgadas_a_centimetros(pulgadas)
            print(f"{pulgadas} pulgadas = {resultado:.2f} cm")

        elif opcion == "2":
            metros = float(input("Ingresa la cantidad en metros: "))
            resultado = metros_a_pies(metros)
            print(f"{metros} metros = {resultado:.2f} pies")

        elif opcion == "3":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta otra vez.")

main()