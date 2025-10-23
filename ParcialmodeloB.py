"""
b.Escribir un programa que le pida al usuario que ingrese, una a una, las distancias recorridas por un vehículo, 
preguntando a cada paso, si desea ingresar más datos. Finalmente, 
el programa debe mostrar, con descripciones expresivas, 
la cantidad de distancias ingresadas, la suma total de las mismas y la mayor distancia ingresada. 
[No es necesario validar los datos]
"""

def main():
    """
    Pide al usuario que ingrese una distacia(float)
    inicializo distancia_mayot con el valor de la distancia
    contador inicializo <- 1
    acumulaodr <- distacia
    preguno si ingresa mas distacias
    si respuesta es S
        pide al usuario que ingrese una distacia(float)
    si distancia_mayor a ddistancia mayor
        distancia_mayor <- distancia
    contador <- contador +1
    acumulador <- acumulador + distacia
    pregunto si ingresa mas distancias
    imprimir contador 
    imprimir acumulador
    imprimir distancia_mayor


    """
    dist=float(input("Ingrese la distacia recorrida: "))
    distancia_mayor=dist
    cont=1
    acum=dist
    respuesta=(input("Quiere ingresar distancias S o N: "))
    while respuesta == "S" or respuesta == "s":
        dist=float(input("Ingrese la distacia recorrida: "))
        if dist > distancia_mayor :
            distancia_mayor=dist   
        acum+=dist
        cont+=1
        respuesta=(input("Quiere ingresar distancias S o N:"))

    print(f"Se ingresaron {cont} , distacias ")
    print(f"La distancia total acumulado es {acum}")
    print(f"La mayor distacia ingresadas {distancia_mayor}")

main()