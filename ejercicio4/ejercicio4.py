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


# f) Mostrar todo al usuario
print("-" * (10 + (m * 12) + 11))

## Encabezado de la tabla
print(f"{'':10}", end="")
for col in range(m):
    print(f"|{f"Col {col + 1}":>10}", end="")
print("| Total Col |")
print("-" * (10 + (m * 12) + 11))

## Cuerpo de la tabla con encabezado lateral
for fila in range(n):
    print(f"{f'Fila {fila + 1}':<10}", end="")
    for columna in range(m):
        print(f"|{matriz[fila][columna]:>10}", end="")
    print(f"|{suma_fila[fila]:11}|")
    if fila < n:
        print("-" * (10 + (m * 12) + 11))

## Fila de promedio
print(f"{'Promedio':<10}", end="")
for columna in range(m):
    print(f"|{prom_columna[columna]:>10.2f}", end="")
print("|", f" " * 9, "|")
print("-" * (10 + (m * 12) + 11))