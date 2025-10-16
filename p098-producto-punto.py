# p098-producto-punto.py
# Calcula el producto punto de dos vectores

print('\033[H\033[J')
print("--- Cálculo del Producto Punto ---\n")
A = [1, 3, -5]
B = [4, -2, -1]
C = []

print(f"Vector A: {A}")
print(f"Vector B: {B}\n")

# 1. Verificar que los vectores tengan la misma longitud
if len(A) == len(B):
        print ("Calculando el producto punto")
# 2. Multiplicar elementos y sumar los resultados
        for i in range(len(A)):
            producto = A[i] * B[i]
            C.append(producto)
# 3. Mostrar el resultado
        print(f"Vector C: {C}")
        print(f"El producto punto es: {sum(C)}")
# El cálculo sería: (1*4) + (3*-2) + (-5*-1) = 4 - 6 + 5 = 3
else:
    print("Los vectores deben ser del mismo tamaño")