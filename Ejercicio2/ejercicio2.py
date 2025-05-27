

matriz=[] #Crear una matriz vacía para guardar sus datos mas adeante
contador=0 #Se utilizara para llevar un contador de los estudiantes
for _ in range (0,5): #de 0 a los 5 estudiantes que pide el ejercicio
    contador+=1
    estudiante=input(f"\nEstudiante {contador}: ") #pide el nombre del estudiante
    calificacion_1= float(input("Ingrese la calificación del estudiante: ")) #pedira las 3 calificaciones
    calificacion_2= float(input("Ingrese la calificación del estudiante: "))
    calificacion_3= float(input("Ingrese la calificación del estudiante: "))
    calificacion_final = calificacion_1 + calificacion_2 + calificacion_3 #calcula la calificación final
    promedio = calificacion_final / 3 #Calcula el promedio

    
    matriz.append([estudiante, calificacion_1, calificacion_2,calificacion_3, calificacion_final, promedio]) #Guardamos los datos en una lista

    print("-" * 97)
print(f"| {"Estudiante":>10} | {"Calificacion1":>10} | {"Calificacion2":>10} | {"Calificacion3":>10} | {"Calificacion final":>10} | {"Promedio":>10} |") #Creamos el encabezado de la tabla
print("-" *97)

for fila in matriz: # recorre la lista y la imprime en la tabla
    estudiante, calificacion_1, calificacion_2, calificacion_3, calificacion_final, promedio = fila
    print(f"| {estudiante:>10} | {calificacion_1:>13.2f} | {calificacion_2:>13.2f} | {calificacion_3:>13.2f} | {calificacion_final:>18.2f} | {promedio:>10.2f} |") #nos ordena la tabla con los datos de los 5 estudiantes
print("-" *97 ) 