# p112-registro-estudiantes.py
# Objetivo: Crear una lista de diccionarios

grupo = [
    {'nombre':'Carlos','edad':45,'carrera':'sistemas','promedio':9} ,
    {'nombre':'Rocio','edad':35,'carrera':'sistemas','promedio':10}
]
print('\033[H\033[J')
print('Registro de Estudiantes\n')

print(f'\nGrupo {grupo} - {len(grupo)}')

print('\nCapturar estudiantes')
while True:
    print(f'Datos Estudiante:')
    datos = {} #Crear un diccionario vacío para introducir datos
    nombre = input('Nombre ? ')
    if nombre!='': break
    datos['nombre'] = nombre
    datos['edad'] = int(input('Edad? '))
    datos['carrera'] = input('Carrera ? ')
    datos['promedio'] = float(input('Promedio? '))
    grupo.append(datos)


print(f'\nGrupo de estudiantes completo:\n{'-'*60}\n{grupo} - {len(grupo)}')

print('\nDatos en forma de Tabla:')
print('-'*60)
for k in grupo[0].keys():
    print(f'{k:<13}', end='')
print('')
print('-'*60)
for alumno in grupo:
    for v in alumno.values():
        print(f'{v:<13}', end='')
    print('')
print('-'*60)


print('\nDatos en forma de Registro y Cálculo de Promedios:')
print('-'*60)
suma=0
for est in grupo:
    suma += est['promedio']
    for k,v in est.items():
        print(f'{k:<10} : {v}')
    print('')
print('-'*60)

print("Suma            : ", suma)
print("Promedio        : ", suma / {len(grupo)})