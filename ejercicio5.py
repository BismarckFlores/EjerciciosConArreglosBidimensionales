ventas = [[50, 88, 30, 45], [9, 45, 30, 20], [59, 90, 10, 60]]
zonas = ["zona 1", "Zona 2", "Zona 3", "Zona 4"]
vendedores = ["Vendedor 1", "Vendedor 2", "Vendedor 3", "Vendedor 4"]
num_vendedores = len(ventas)
num_zonas = len(ventas[0])

print(num_vendedores, num_zonas)

# a) Suma de ventas por zona
ventas_zona = []

for zona in range(num_zonas):
    suma = 0
    for vendedor in range(num_vendedores):
        suma += ventas[vendedor][zona]
    ventas_zona.append(suma)
print(ventas_zona)

## Encontrar la zona que vendio mas
mas_ventas_zona = 0
zona_max = 0
venta = 0

for zona in range(num_zonas):
    venta = ventas_zona[zona]
    if venta > mas_ventas_zona:
        mas_ventas_zona = venta
        zona_max = zona

print(f"La zona con mas ventas es la {zonas[zona_max]}, con una venta de {mas_ventas_zona} computadoras")