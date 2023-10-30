# repo11-matrices

#  1. Desarrolle un programa que permita realizar la suma/resta de matrices:
```A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8, 9], [10, 11, 12]]

# Obtener la suma y resta de las matrices
suma = suma_matrices(A, B)
resta = resta_matrices(A, B)

# Imprimir los resultados si son válidos
if suma and resta:
    print("Suma de matrices:")
    for fila in suma:
        print(fila)

    print("\nResta de matrices:")
    for fila in resta:
        print(fila)

```
#  2. Desarrolle un programa que permita realizar el producto de matrices:
```
 print("No se pueden multiplicar las matrices dadas. Revise las dimensiones.")

# Ejemplo de uso 2
C = [[2, 4], [1, 3], [5, 6]]
D = [[3, 2], [1, 7]]

resultado2 = producto_de_matrices(C, D)

if resultado2:
    print("\nProducto de matrices 2:")
    for fila in resultado2:
        print(fila)
else:
    print("No se pueden multiplicar las matrices dadas. Revise las dimensiones.")
```

#  3. Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada:
```
def obtener_transpuesta(matriz):
    if not matriz:
        return None

    filas = len(matriz)
    columnas = len(matriz[0])

    transpuesta = [[matriz[j][i] for j in range(filas)] for i in range(columnas)]
    return transpuesta

# Ejemplo de uso
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_transpuesta = obtener_transpuesta(matriz_ejemplo)

if matriz_transpuesta:
    print("Matriz original:")
    for fila in matriz_ejemplo:
        print(fila)

    print("\nMatriz transpuesta:")
    for fila in matriz_transpuesta:
        print(fila)
else:
    print("La matriz está vacía. No se puede obtener la transpuesta.")

```
#  4 . Desarrollar un programa que sume los elementos de una columna dada de una matriz:
```
def sum_column(matrix, column_index):
    if not matrix:
        return None
    if column_index < 0 or column_index >= len(matrix[0]):
        return None

    return sum(row[column_index] for row in matrix)

# Ejemplo de uso
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
column_index = 1  # Índice de la columna que quieres sumar

result = sum_column(matrix, column_index)
if result is not None:
    print(f"La suma de los elementos de la columna {column_index} es: {result}")
else:
    print("La matriz está vacía o el índice de columna está fuera de rango.")
```

# 5. Desarrollar un programa que sume los elementos de una fila dada de una matriz:
```
def sum_row(matrix, row_index):
    if not matrix:
        return None
    if row_index < 0 or row_index >= len(matrix):
        return None

    return sum(matrix[row_index])

# Ejemplo de uso
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
row_index = 1  # Índice de la fila que quieres sumar

result = sum_row(matrix, row_index)
if result is not None:
    print(f"La suma de los elementos de la fila {row_index} es: {result}")
else:
    print("La matriz está vacía o el índice de fila está fuera de rango.")

```

#
