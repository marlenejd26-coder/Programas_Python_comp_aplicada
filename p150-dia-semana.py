# p150-dia-semana.py
# Objetivo: Pedir al usuario un numero, entre 1 y 7 y mostrar el dia correspondiente

def dias_semana(dia: int) -> str:
    if dia in [1]:
        return "Lunes"
    elif dia in [2]:
        return "Martes"
    elif dia in [3]:
        return "Miercoles"
    elif dia in [4]:
        return "Jueves"
    elif dia in [5]:
        return "Viernes"
    elif dia in [6]:
        return "Sábado"
    elif dia in [7]:
        return "Domingo"
    else:
        return "Error: El número debe estar entre 1 y 7"

print('Introduce un número del 1 al 7:')
dia = int(input())
print(f'El día es: {dias_semana(dia)}')

