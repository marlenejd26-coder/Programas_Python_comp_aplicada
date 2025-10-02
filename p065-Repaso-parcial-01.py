# p065-Repaso-parcial-01.py
# Objetivo: gestion eficiente de control de ventas de una papelería

print("\033[H\033[J")
print ("Programa de repaso parcial 01")
print ("Gestion eficiente de control de ventas de una papelería")

ventas = cantidad = subtotal = 0
cantidad_c = cantidad_o = cantidad_d = cantidad_p = 0
total_c = total_o = total_d = total_p = 0

while True:
    ventas += 1
    print (f"\nVenta {ventas}")

    tipo = input ("Tipo de Copia (C)arta $3, (O)ficio $4, (D)oble 0f $6, (P)lano $12 ? ").upper()

    if tipo not in "CODP":
        err=input (">>>>> Error tipo de copia no valido intente de nuevo, <Enter>")
        ventas -= 1
        continue #Por si no esta en la letra valida de copias

    cantidad = int(input("Cantidad ? "))
    descuento = 1
    if cantidad > 50:
        descuento = 0.90
        print ("** Descuento del 10% aplicado por volumen de venta **")

    if tipo == 'C':
        cantidad_c += cantidad
        subtotal = (cantidad * 3) * descuento
        total_c += subtotal
    elif tipo=='O':
        cantidad_o += cantidad
        subtotal = (cantidad*4)*descuento
        total_o += subtotal
    elif tipo=='D':
        cantidad_d += cantidad
        subtotal = (cantidad*6)*descuento
        total_d += subtotal
    elif tipo=='P':
        cantidad_p += cantidad
        subtotal = (cantidad*12)*descuento
        total_p += subtotal

    if input ("Otra Venta (S/N) ? ").upper() != "S": break
total_copias = cantidad_c + cantidad_o + cantidad_d + cantidad_p
total_ventas = total_c + total_o + total_d + total_p

print("\n=================================")
print("Papelería la Malena, SA. de CV.")
print("Sistema de ventas de copias")
print("===================================")
print("\n=================================")
print(" Resumen diario de ventas")
print("===================================")
print(f" Ventas realizadas: {ventas}")
print("===================================")
print(f" Carta \t\t: {cantidad_c:2d} - $ {total_c:8.2f}")
print(f" Oficio\t\t: {cantidad_o:2d} - $ {total_o:8.2f}")
print(f" Doble oficio\t: {cantidad_d:2d} - $ {total_d:8.2f}")
print(f" Plano \t\t: {cantidad_p:2d} - $ {total_p:8.3f}")
print("===================================")
print(f" Total Ventas \t: {total_copias:2d} - $ {total_ventas:8.2f}")

mensaje_venta=""
if total_ventas > 150:
    mensaje_venta = "Venta Superada"
elif total_ventas >= 50:
    mensaje_venta="Venta frecuente"
else:
    mensaje_venta="Venta moderada"

print (f"Esta es una venta: {mensaje_venta}")
print ("\n Fin de las ventas por este día")