"""
Definir una función, denominada “determina_dto”, que reciba como parámetros dos números enteros (que representan el tipo de artículo y el nro. de día de la semana) y que devuelva como resultado un número flotante, que representa el porcentaje de descuento respectivo, de acuerdo a la siguiente regla [No es necesario validar los datos]:
- Para vinos finos ( 14 )  el descuento es  0.30   los días sábado ( 7 ) y domingo ( 1 ).

- Para lácteos ( 10 )  el descuento es  0.10   los días martes ( 3 ) y jueves ( 5 ).

- Para pescadería ( 19 )  el descuento es  0.20   los días martes ( 3 ).

- Para carnicería ( 49 )  el descuento es  0.15   los días martes ( 3 ) y jueves ( 5 ).

Dé un ejemplo de invocación y utilización de “determina_dto”, desde una función “main".

Nota: La fórmula de cálculo del descuento es:   descuento  =  precio  x  porcentaje de descuento

b.      Escribir un programa que le pida al usuario que ingrese, una a una, las distancias recorridas por un vehículo, preguntando a cada paso, si desea ingresar más datos. Finalmente, el programa debe mostrar, con descripciones expresivas, la cantidad de distancias ingresadas, la suma total de las mismas y la mayor distancia ingresada. [No es necesario validar los datos]


SI el articulo es 14 y (el dia es 7 o el dia es 1)
    el desscuetno es 0.30
si no pero el articulo es 19 y el dia es 3
    el descuento es de 0.20
si no pero articulo es 40 y (el dia es 3 o el dia es 5)
    el descuento es de 0,15
si no 
    el descuento es 0.0
retornar el descuento
"""

def determina_dto(art,dia):
    """domingo 1, lunes 2, martes 3 miercoles 4, jueves 5, viernes 6, sabado 7"""
    if art == 14 and (dia == 7 or dia ==1):
        descuento=0.30
    elif art==19 and dia == 3:
        descuento=0.20
    elif art==40 and (dia==3 or dia==5):
        descuento=0.15
    else:
        descuento=0.0
    return descuento
def main():
    art=int(input("Ingrese un Numero de articulo: "))
    dia=int(input("Ingrese una dia valido en numero del 1 al 7 : "))
    descuento=determina_dto(art,dia)
    print(f"Al articulo {art} el dia {dia} le correspon un descuento de {descuento*100}")
main()