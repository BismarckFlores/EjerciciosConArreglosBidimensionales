ventas = [[50, 88, 30, 45], [9, 45, 30, 20], [59, 90, 10, 60]]
zonas = ["zona 1", "Zona 2", "Zona 3", "Zona 4"]
vendedores = ["Vendedor 1", "Vendedor 2", "Vendedor 3", "Vendedor 4"]

num_vendedores = len(ventas)
num_zonas = len(ventas[0])


# a) Suma de ventas por zona
ventas_zona = []

for zona in range(num_zonas):
    suma = 0
    for vendedor in range(num_vendedores):
        suma += ventas[vendedor][zona]
    ventas_zona.append(suma)

## Encontrar la zona que vendio mas
mas_ventas_zona = 0
zona_max = 0
venta = 0

for zona in range(num_zonas):
    venta = ventas_zona[zona]
    if venta > mas_ventas_zona:
        mas_ventas_zona = venta
        zona_max = zona

print(ventas_zona)
print(f"La zona con mas ventas es la {zonas[zona_max]}, con una venta de {mas_ventas_zona} computadoras")


# b) Sumar ventas por vendedor
suma_vendedor = []

for vendedor in range(num_vendedores):
    suma = sum(ventas[vendedor])
    suma_vendedor.append(suma)

## Encontrar el vendedor que menos vendio
min_ventas_vendedor = suma_vendedor[0]
vendedor_min = 0
venta = 0

for vendedor in range(num_vendedores):
    venta = suma_vendedor[vendedor]
    if venta < min_ventas_vendedor:
        min_ventas_vendedor = venta
        vendedor_min = vendedor

print(suma_vendedor)
print(f"El vendedor con menos ventas fue el {vendedores[vendedor_min]}, con un total de {min_ventas_vendedor}")

# c) Suma de todas las ventas
total_ventas = 0

for vendedor in range(num_vendedores):
    total_ventas += sum(ventas[vendedor])
print(f"Las ventas totales son de {total_ventas} computadoras")