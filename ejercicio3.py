# Paso 1: Pedir al usuario el número de filas
filas = int(input("Ingresa el número de filas: "))

# Paso 2: Pedir al usuario el número de columnas
columnas = int(input("Ingresa el número de columnas: "))

# Paso 3: Crear una lista vacía para guardar la matriz
matriz = []

# Paso 4: Llenar la matriz con datos ingresados por el usuario
print("\nIngresa los elementos de la matriz fila por fila:")
for i in range(filas):
    fila = []  # Lista vacía temporal para almacenar una fila
    for j in range(columnas):
        # Pedir al usuario un valor
        valor = int(input(f"Elemento en posición [{i}][{j}]: "))
        fila.append(valor)  # Agregar el valor a la fila
    matriz.append(fila)  # Agregar la fila completa a la matriz

# Paso 5: Mostrar la matriz ingresada
print("\nMatriz original:")
for fila in matriz:
    print(fila)

# Paso 6: Crear una lista vacía para almacenar el resultado linealizado
arreglo_lineal = []

# Paso 7: Recorrer la matriz por columnas
for c in range(columnas):           # Para cada columna
    for f in range(filas):          # Recorrer cada fila dentro de esa columna
        # Agregar el elemento en la posición [f][c] al arreglo lineal
        arreglo_lineal.append(matriz[f][c])

# Paso 8: Mostrar el arreglo linealizado
print("\nArreglo linealizado por columnas:")
print(arreglo_lineal)