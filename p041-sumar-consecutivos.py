# p041-sumar-consecutivos.py
# Objetivo: Suma números hasta que el total sea >= 100.

print ("Rifa entre amigos para recaudar 100. cuantos boletos necesito ?")

c = 0
suma = 0

# El ciclo está programado para correr hasta 200, pero el 'break' lo detendrá antes.
while c < 200:
    c += 1
    suma += c
    meta = 5000
    print(f" (+{c})", end="")

# Verificamos si hemos alcanzado o superado la meta.
    if suma >= meta:
        print("\n ¡Meta alcanzada!")
        print (f"boletos {suma} ")
        # La palabra 'break' termina el ciclo de inmediato.
        break

print ("\n Proceso terminado..." + str(suma))
