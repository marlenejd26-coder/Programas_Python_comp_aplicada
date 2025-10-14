# p092-lista-de-gastos.py
# Objetivo: Permite llevar el control de una lista de gasto

print('\033[H\033[J')

gastos = [450.50, 120.00, 85.90, 230.00, 55.75]
limite_gasto = 100.00

while True:
    print("\n---Menú de Gestión de Gastos---")
    print("1. Ver todos los gastos")
    print("2. Agregar un nuevo gasto")
    print("3. Modificar un gasto existente")
    print("4. Eliminar un gasto (por reempolso o error)")
    print("5. Ver resumen y total de gastos")
    print("6. Salir")
    opcion = int (input("Elige una opcion (1-6): "))

    if opcion == 1: #Ver los gastos
        print("\n --- Tus Gastos Registrados---")
        print(gastos)
    elif opcion == 2: #Agregar gastos
        try:
            nuevo_gasto = float(input("Ingresa el monto del nuevo gasto: "))
            gastos.append(nuevo_gasto)
            print(f"✅ Gasto de ${nuevo_gasto:.2f} agrgado correctamente.")
        except ValueError:
            print("❌ Error: Por favor, ingresa un número válido.")

    elif opcion == 3: #Modificar gasto
        try:
            pos=int(input("Ingresa la posición en la lista del gasto que quieres modificar: "))
            valor_anterior = gastos[pos]
            print(f"Gasto a modificar gastos [{pos}] ${valor_anterior:.2f} ")
            nuevo_valor = float(input("Ingresa el nuevo monto del gasto: "))
            gastos[pos] = nuevo_valor
            print (f"✅ Gasto modificado de ${valor_anterior:.2f} a ${nuevo_valor:.2f}. ")
        except IndexError:
            print ("❌ Error: la posición esoecificada no se encuentra en la lista. ")
        except ValueError:
            print("❌ Error: por favor, ingresa número válidos. ")
    elif opcion==4:
        try:
            gasto_a_eliminar=float(input("ingresa el monto del gasto que quieres eliminar: "))
            if gasto_a_eliminar in gastos:
                gastos.remove(gasto_a_eliminar)
                print(f"✅ Gasto de ${gasto_a_eliminar:.2f} eliminado correctamente. ")
            else:
                print("❌Error: El gasto especificado no se encuentra en la lista.")
        except ValueError:
            print("❌ Error: por favor, ingresa un número válido.")
    elif opcion==5:
        if not gastos:
            print("\n No hay gastos para mostrar. ")
        else:
            total_gastado = 0
            print("\n ---Resumen del Mes--- ")
            for gasto in gastos:
                total_gastado += gasto
                if gasto>limite_gasto:
                    print(f"Gasto considerable detectado> ${gasto:.2f}")
            print(f"\n El gasto total del mes es: ${total_gastado:.2f}")
    elif opcion==6:
        print("\nGracias por usar el gestor de gastos. !Hasta pronto! ✌️"); break
    else:
        print("❌ Opción no válida. Por favor, elige un número del 1 al 6.")

        