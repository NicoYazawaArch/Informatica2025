"""
Ejercicio 7.2. Definir una función …
a) que reciba como parámetro una tupla tup con nombres, y para cada nombre imprima
el mensaje “Estimado <nombre>, vote por mí “.
b) modificar la solución anterior, para que el mensaje distinga el género del destinatario,
considerando que tup es una tupla integrada por tuplas de la forma (nombre,
género). [ Valores de género: ‘M’ → masculino; ‘F’ → femenino; ‘O’ → otres ]

recorro la tupla nombres de inicio a fin tomando cada nombre en la variable nombre
    imprimir la frase dada insertada en el nombre

"""

def mensajeA(tup):
    for nombre in tup:
        print(f"Estimado {nombre}, vote por mí")

def main():
    nombres = ("Juan", "Ana", "Luis", "Maria")
    mensajeA(nombres)
#main()

def mensajeB(tup):
    for nombre, genero in tup:
        if genero=="F":
            print(f"Estimada {nombre}, vote por mi.")
        elif genero == "M":
            print(f"Estimado {nombre}, vote por mi.")   

        elif genero == "O":
            print(f"Estimade {nombre}, vote por mi.")

        else:
            print(f"Estimado/a {nombre}, vote por mi.")


def main2():
    datos=(
    ("Juan", "M"),
    ("Ana", "F"),
    ("Luis", "M"),
    ("Alex", "O"),
    ("Maria", "F"))
    mensajeB(datos)
#main2()

"""a) con el profesor"""
def vote (t_nombres):
    for elem in t_nombres:
        print("Hola", elem, " Vote por mi")

def main3():
    nombres = ("Juan", "Ana", "Luis", "Maria")
    vote(nombres)
main3()