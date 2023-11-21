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
#función para sumar los elementos de la misma posición en cada fila
def suma_columna(matriz, columna):
  suma = 0
  for fila in matriz:
    #verifica si la columna seleccionada para su respectiva fila.
    if columna < len(fila):
      suma += fila[columna]
    return suma

#Se ingresa el número de filas y columnas
filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))

#Se ingresa los valores la matriz fila por fila
matriz = []
for i in range(filas):
  fila = input(f"Ingrese los elementos de la fila {i + 1} separados por espacios: ").split()
  fila = [int(x) for x in fila]
  matriz.append(fila)

#se pide la columna que se desea sumar
columna_a_sumar = int(input(f"Ingrese el número de la columna que desea sumar (0 - {columnas - 1}): "))

#resultado
resultado = suma_columna(matriz, columna_a_sumar)
print(f"La suma de la columna {columna_a_sumar} es: {resultado}")
 
```

# 5. Desarrollar un programa que sume los elementos de una fila dada de una matriz:
```
def CrearMatriz(matriz):# Para que el usuario cree la matriz
  fila=[]
  filas=int(input("Ingrese el número de filas: "))  # Ingresar el número de filas que quiere
  columnas=int(input("Ingrese el número de columnas: ")) # Ingresar el número de columnas que quiere
  print("--------------------------------------------")
   # Para ir creando cada fila
  for i in range(filas):                                                     
    for j in range(columnas):                      
 # Para añadir los valores de la fila (cada columna)
      valor=int(input("Ingrese el valor de la fila " + str(i) + ": "))
      fila.append(valor)                                                     
# Se añade el valor a la fila
    matriz.append(fila)                                                      
# Se añade la fila terminada a la matriz
    fila=[]                                                                 
 # Se deja vacía la fila para seguir con las demás
  print("--------------------------------------------")
  for k in range(len(matriz)):                                               
# Para imprimir la matriz con forma de matriz ;)
    print(matriz[k])

def SumaFila(matriz):                                                      
 # Para la suma de las filas
  suma=0
  print("--------------------------------------------")
  for i in matriz:                                                           
# Selecciona la fila de la matriz
    for j in i:                                                              
# Selecciona cada elemento de esa fila
      suma+=j                                                                
# Suma los elementos
    print("La suma de la fila " + str(i) + " es: " + str(suma))
    suma=0

if __name__ == "__main__":
  matriz=[]                                                                 
# Se crea la matriz vacía
  CrearMatriz(matriz)                                                       
# Se llama la función para crear la matriz
  SumaFila(matriz)                                                         


```
