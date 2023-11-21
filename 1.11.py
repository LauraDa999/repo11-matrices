B = [[7, 8, 9], [10, 11, 12]]

# Para obtener la suma y resta de las matrices
suma = suma_matrices(A, B)
resta = resta_matrices(A, B)

# Para impriir los resultados si son válidos
if suma and resta:
    print("Suma de matrices:")
    for fila in suma:
        print(fila)

    print("\nResta de matrices:")
    for fila in resta:
        print(fila)
