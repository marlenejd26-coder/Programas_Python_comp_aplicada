# p114-area-figuras.py
# Objetivo: Crear un diccionario de diccionarios 

figuras = {
"Circulo": {"radio": 0, "formula": "math.pi * r ** 2"},
"Triangulo": {"base": 0, "altura": 0, "formula": "0.5 * b * a"},
"Rectangulo": {"largo": 0, "ancho": 0, "formula": "l * a"}
} #Se pide al usuario que sustituya las fórmulas por valores

print('\033[H\033[J')
print('Área de Figuras Geométricas\n')

print("Figuras disponibles:")
for k,v in figuras.items(): #Conformar menú
    print(f'{k:<10} - Fórmula: {v["formula"]}')

while True: #ciclo para elegir figura válida
    fig = input('\nElige Figura ? ').title()
    if fig in figuras: break
    print("❌")

#Calcular área específica de esa figura
area = 0

if fig == 'Circulo':
    r = float(input('Radio ? '))
    f = figuras[fig]["formula"].replace("r",str(r))
    area = eval(f)
    print(f"formula: {f}")

elif fig=='Triangulo':
    b = float(input('Base ? '))
    a = float(input('Altura ? '))
    f = figuras[fig]["formula"].replace("b",str(b)).replace("a", str(a))
    area = eval(f)
    print(f"formula: {f}")

elif fig=='Rectangulo':
    l = float(input('Largo ? '))
    a = float(input('Ancho ? '))
    f = figuras[fig]["formula"].replace("l",str(l)).replace("a", str(a))
    area = eval(f)
    print(f"formula: {f}")
    
print(f'\nEl Área del {fig} es : {area:.4f}')