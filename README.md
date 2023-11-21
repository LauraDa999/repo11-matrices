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
#funcion para validar que ambas matrices tienen el mismo tamañaño
def validar(m1, m2):
  num_columnas_m1 = len(m1[0])
  num_filas_m2 = len(m2)

  return num_columnas_m1 == num_filas_m2

 
#función para multiplicar matrices
def producto(m1, m2):
  if validar(m1, m2):
    resultado = []

    for i in range(len(m1)):
      fila = []
      #recorremos las columnas de la segunda matriz.
      for j in range(len(m2[0])):
        punto = 0
        #ahora las columnas 
        for k in range(len(m2)):
          #operamos y añadimos a la fila el resultado para luego añadirlo a la respuesta
          punto += m1[i][k] * m2[k][j]
        fila.append(punto)
      resultado.append(fila)
    return resultado
  
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
