# a) Solicitar los datos al usuario
while True:
    try:
        n = int(input("Ingrese cuantas filas quiere que tenga la matriz: "))
        if n <= 0:
            print("Error. El valor ingresado tiene que ser positivo y mayor a 0")
            continue
        break
    except ValueError:
        print("Error. Porfavor ingrese un valor válido")

while True:
    try:
        m = int(input("Ingrese cuantas columnas quiere que tenga la matriz: "))
        if m <= 0:
            print("Error. El valor ingresado tiene que ser positivo y mayor a 0")
            continue
        break
    except ValueError:
        print("Error. Porfavor ingrese un valor válido")

# b) Crear la matriz
matriz = []

## Pedir los valores al usuario
for fila in range(n):
    nueva_fila = []
    for columna in range(m):
        while True:
            try:
                num = int(input(f"Ingresa el valor de la fila {fila + 1} columna {columna + 1}: "))
                break
            except ValueError:
                print("Error. Porfavor ingrese un valor válido")
        nueva_fila.append(num)
    matriz.append(nueva_fila)

# c) Suma por filas
suma_fila = []

for fila in matriz:
    suma = sum(fila)
    suma_fila.append(suma)

# d) Promedio por columna
prom_columna = []

for columna in range(m):
    suma = 0
    prom = 0
    for fila in range(n):
        suma += matriz[fila][columna]
    prom = suma / n
    prom_columna.append(prom)

# e) Valor mas grande
valor_grande = 0

for fila in matriz:
    for columna in fila:
        if columna > valor_grande:
            valor_grande = columna

print("-" * 17)
for fila in matriz:
    for columna in fila:
        print(f"|{columna:>6}", end = " ")
    print("|")
    print("-" * 17)

print(suma_fila)
print(prom_columna)
print(valor_grande)