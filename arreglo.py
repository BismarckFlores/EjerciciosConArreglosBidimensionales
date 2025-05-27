# Este programa calcula las ventas totales de varias tiendas ABSA y determina cuál tienda tuvo la mayor y menor venta.

#Primero almacenamos los datos de ventas en una matriz 

ventas = [
    [50000, 60000, 65000, 62000, 78000, 95000],  # ABSA 1
    [89000, 90000, 98000, 80000, 85000, 90000],  # ABSA 2
    [65000, 72000, 85000, 72000, 83000, 98000],  # ABSA 3
    [92000, 88000, 90000, 76000, 82000, 93000]   # ABSA 4
]

#Calculamos las ventas totales por tienda
ventas_totales = [sum(tienda) for tienda in ventas]
print(f"Venta total de todas las tiendas: {sum(ventas_totales)}")

for i, total in enumerate(ventas_totales, start=1):
    print(f"Venta total de ABSA {i}: {total}")
#Mostramos los resultados
print(f"La tienda que más vendió es ABSA {ventas_totales.index(max(ventas_totales)) + 1}")
print(f"La tienda que menos vendió es ABSA {ventas_totales.index(min(ventas_totales)) + 1}")