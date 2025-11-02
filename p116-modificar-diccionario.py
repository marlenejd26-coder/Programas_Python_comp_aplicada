# p116-modificar-diccionario.py
# Objetivo: Crear un diccionario llamado paises y modificar los valores

print('\033[H\033[J')
print("Crear un diccionario llamado paises y modificar los valores")

paises = {'Argentina': 100, 'Brasil': 200, 'Colombia': 300, 'Chile': 400, 'Ecuador': 500, 'Bolivia': 600, 'Jamaica': 700}

print("Diccionario inicial:")
print(paises)

# Modifica valores con []
paises["Brasil"] = 250
paises["Chile"] = 450

# Modifica valores con update()
paises.update({"Bolivia": 650})
paises.update({"Jamaica": 750})

print("\nDiccionario modificado:")
print(paises)