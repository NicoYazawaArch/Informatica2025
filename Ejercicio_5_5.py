"""
Ejercicio 5.5. Escribir un programa que reciba, una a una, las calificaciones del usuario,
preguntando a cada paso si desea ingresar más notas; finalmente, el programa debe
imprimir el promedio correspondiente y el valor de la calificación más baja.
"""
def main():
    notas_total=0
    cant=0
    nota_minima=10000 #Utiliza un valor absurdo para poder sobrescribirse luego
    ingreso=input("Quiere ingresar notas escriba si o no: ")
    
    while ingreso.lower() == "si": #ingreso.lower() utilizar para que cualquier valor de si sea validoo aunqque este en mayuscula
        nota=int(input("Ingrese valor de la nota: "))
        cant+=1
        notas_total+=nota
        if nota<nota_minima : #Evalua cual es la nota mas baja y sobre escribe el valor de nota_minima
            nota_minima=nota

        ingreso=input("Quiere volver a ingresar notas escriba si o no: ")
    if cant > 0 :
        promedio=notas_total/cant
        print("Promedio de las notas: ",promedio)
        print("Nota mas baja: ", nota_minima)
    else:
        print("No se ingresaron Notas.")
        print("----Exit----")
main()

