"""
Ejercicio 5.5. Escribir un programa que reciba, una a una, las calificaciones del usuario,
preguntando a cada paso si desea ingresar más notas; finalmente, el programa debe
imprimir el promedio correspondiente y el valor de la calificación más baja.
"""
def main():
    notas_total=0
    cant=0
    nota_minima=10000
    ingreso=input("Quiere ingresar notas escriba si o no: ")
    while ingreso.lower() == "si":
        nota=int(input("Ingrese valor de la nota: "))
        cant+=1
        notas_total+=nota
        if nota<nota_minima :
            nota_minima=nota

        ingreso=input("Quiere volver a ingresar notas escriba si o no: ")
    if cant > 0 :
        promedio=notas_total/cant
        print("Promedio de las notas: ",promedio)
        print("Nota mas baja: ", nota_minima)
    else:
        print("No se ingresaron Notas")
        print("----Exit----")
main()

