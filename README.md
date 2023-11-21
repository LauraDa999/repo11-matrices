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
#Para imprimir una matriz
def matriz(matriz):
  for fila in matriz:
    for elemento in fila:
      print(elemento, end="\t")
        #genera el salto entre filas   
    print()  

#funcion para obtener la matriza transpuesta
def transpuesta(matriz):
  #verifica si la matriz esta vacia
  if not matriz:
    return []
  #Para el numero de filas y columnas
  filas = len(matriz)
  columnas = len(matriz[0])
  #inicia una matriz vacia para ivertir las dimenciones
  transpuesta = [[0] * filas for _ in range(columnas)]
  #transpone a la matriz ingresada
  for i in range(filas):
    for j in range(columnas):
            #intercambia las posisciones
            transpuesta[j][i] = matriz[i][j]

  return transpuesta
#pedimos la cantidad de filas, nosotros definimos las columnas
filas = int(input("Ingrese el número de filas de la matriz: "))

#una matriz vacía
m = []

print("Ingrese los elementos de la matriz fila por fila: ")
for i in range(filas):
  fila = input(f"Ingrese los elementos de la fila {i + 1} separados por espacios: ").split()
  fila = [int(elemento) for elemento in fila]
  m.append(fila)

# Se imprime la matriz 
resultante = transpuesta(m)
for fila in resultante:
  print(fila)



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
