# p072-suma-pares-impares.py
# Objetivo: Imprimir los números pares y números impares , su suma también en un rango determinado

while(True):
    print('\033[H\033[J')
    print('Imprimir la suma de pares e impares en un rango de 1 a n')
    n = int(input('Dame el valor final ? '))
    sp = si = 0
    cp = ci = ""
    for i in range(1, n +1):
        if i % 2 == 0: # es par
            cp = cp + " " + str(i)
            sp = sp + i
        else: # es impar
            ci = ci + " " + str(i)
            si = si + i

    print(f'\nLos pares : {cp} = {sp}')
    print(f'\nLos impares : {ci} = {si}')
    if input('\n\nDeseas continuar (S/N) ? ').upper()=='N': break
    
print('\nHemos llegado al final ....')