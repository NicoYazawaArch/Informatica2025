"""Definir una función denominada “pinta_cuadro”, que reciba como
parámetro un número natural n y dibuje con el carácter ‘x’ un cuadrado relleno, de
lado igual al parámetro. Ejemplo: pinta_cuadro (3)"""
def pinta_cuadrado(n):
    for i in range(n):
        print("x"*n)
    
def main():
    entrada=int(input("Ingrese de cantidad a pintar: "))
    pinta_cuadrado(entrada)
main()

