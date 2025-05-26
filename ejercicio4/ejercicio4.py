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
        m = int(input("Ingrese cuantas columnas quiere que tenga la matriz"))
        if m <= 0:
            print("Error. El valor ingresado tiene que ser positivo y mayor a 0")
            continue
        break
    except ValueError:
        print("Error. Porfavor ingrese un valor válido")