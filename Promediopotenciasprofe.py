"""Escriba una función en Python llamada promedio_potencias(n, k) que reciba dos números enteros positivos n y k.
La función debe calcular y devolver el promedio aritmético de las potencias:
1k,2k,3k, .... ,nk

Tenemos un intervalo de enteros desde 1 hasta n (incluidos)
Tenemos que recorrer ese intervalo de a 1, elevar cada uno de esos numeros a potencia k. Los voy acumulando y contando.
Cuando termino de recorrer el intervalo, divido la suma acumulada por la cuenta
Ese es el promedio. Lo retorno.

Preparo un acumulador vacio.

*Para todos los valores en 1 y n (incluidos y saltando de a 1) 
    Lo elevo a la potencia k
    Lo sumo al acumulado
Promedio <- dividir al acumularo por n.
Retornar el promedio
n<-5
k<-2
acum <-0
1**2 -> 1   a<- 1
2**2 -> 4   a<- 5 
3**2 -> 9   a<- 5+9=14

"""

def promedio_potencias(n,k):
    """
    Recibido como parametro dos numeros enteros (n,k),
    Calcularr el promedio de las k-esimas de todas los numeros entre 1 y n 
    Retorna dicho promedio
    """
    acum=0
    for i in range(1,n+1): #Recorre todo el intervalo
        potencia=i**k
        acum+=potencia     #acum = acum + potencia
    #Salida del bucle
    promedio=acum / n
    return promedio

def main():
    n=int(input("Ingrese el valor de n: "))
    k=int(input("Ingrese el valor de k: "))
    prom_pot=promedio_potencias(n,k)
    print("El promedio de las potencias es ",prom_pot)
main()




