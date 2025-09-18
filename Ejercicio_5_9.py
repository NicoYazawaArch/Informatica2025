"""
Ejercicio 5.9. Escribir un programa que le pida al usuario que ingrese una sucesión de
calificaciones de estudiantes (primero el número de legajo, luego la calificación, y así para
cada estudiante, hasta que el usuario ingrese el legajo -1 como condición de salida). Al
ﬁnal, el programa debe imprimir cuántas calificaciones fueron ingresadas, su valor máximo
ingresado, la suma total de las calificaciones y el promedio.
"""
def main():
 """"
1. Inicialización:
   - notasuma = 0 (variable para acumular la suma de las notas).
   - cant_notas = 0 (contador para el número total de notas).
   - nota_alta = 0 (variable para guardar la nota más alta, se inicializa en 0).
   - nota_baja = 10000000 (variable para guardar la nota más baja, se inicializa con un valor alto).

2. Bucle de Entrada:
   - Solicitar al usuario el número de legajo.
   - Usar un bucle 'while' que continúe mientras el legajo ingresado no sea -1.

3. Dentro del Bucle:
   - Solicitar al usuario el valor de la nota.
   - Incrementar el contador `cant_notas` en 1.
   - Sumar la nota ingresada a `notasuma`.
   - Comparar la nota con `nota_alta`: si la nota actual es mayor, actualizar `nota_alta`.
   - Comparar la nota con `nota_baja`: si la nota actual es menor, actualizar `nota_baja`.
   - Volver a solicitar el número de legajo para la siguiente iteración del bucle.

4. Fuera del Bucle (cuando el usuario ingresa -1):
   - Verificar si se ingresó al menos una nota (`cant_notas > 0`).
   - Si es así:
     - Calcular el promedio (`promedio = notasuma / cant_notas`).
     - Imprimir los resultados: el promedio, la nota más baja y la nota más alta.
   - Si no se ingresó ninguna nota:
     - Imprimir un mensaje indicando que no se ingresaron notas.
""""
    notasuma=0
    cant_notas=0
    nota_alta=0
    nota_baja=10000000

    legajo=int(input("Ingrese numerode de legajo(-1 finaliza ingreso): "))
    while legajo != -1:
        nota=int(input("Ingrese valor de la nota: "))
        cant_notas+=1
        notasuma+=nota
        #esto funciona pero no me parece correcto
        if nota>nota_alta:
            nota_alta=nota
            print(f"debug: na {nota_alta}")
        if nota<nota_baja:
            nota_baja=nota
            print(f"debug: nb {nota_baja}")

        legajo=int(input("Ingrese numerode de legajo(-1 finaliza ingreso): "))
    if cant_notas>0:
        promedio=notasuma/cant_notas
        print("Promedio de las notas: ",promedio)
        print("Nota mas baja: ", nota_baja)
        print("Nota mas alta: ", nota_alta)
    else:
        print("No se ingresaron Notas")
        print("----Exit----")
main()

