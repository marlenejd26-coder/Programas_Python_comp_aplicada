# p105-datos-estudiante.py
# Gestión de datos de estudiantes usando diccionarios

print('\033[H\033[J')
print('Gestión de datos de estudiantes')

estudiante = {
'nombre':'Marlene Juarez',
'edad':45,
'email':'marlenejd@gmail.com',
'carrera':'Electrónica'
}
print(f'\nEl diccionario original: \n\n{estudiante}')

estudiante['calificacion'] = 9.1
estudiante['email'] = 'marlenejd@gmail.com'
print(f'\nEl diccionario actualizado: \n\n{estudiante}')

print('\nLas llaves del diccionario: \n')
for k in estudiante.keys():
    print(k)

print('\nLos valores del diccionario: \n')
for v in estudiante.values():
    print(v)

print("\nListado de llaves y valores:\n")
for k, v in estudiante.items():
    print(f'{k:<10} : {v}')