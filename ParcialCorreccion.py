"""
Escribir una función que reciba tres enteros positivos mayores a 1 (lim, n1, n2). 
La función deberá recorrer el intervalo entre 1 y lim (extremos incluidos) 
y contar (por separado) cuántos múltiplos de n1 hay y cuántos múltiplos de n2 hay.

Si el número de múltiplos de n1 es mayor que de múltiplos de n2, debe retornar True. 
En caso contrario, debe retornar False.
b)escribir un programa (main que pida al usuria que ingrese varios conjuntos)

recorro el intervalo 1 hasta lim(incluido)
    para cada valor de i miro si es multiplo de n1
    si es multiplo de n1, cuento que hay otro multiplo de n1
    para cada valor de i miro si es multiplo de n2
    si es multiplo de n2, cuento que hay otro multiplo de n2

si el numero de multiplos de n1 es mayor al numero de multiplos de n2
    retorno True
si no 
    retorno False

"""

def decicion_cant_multiplos(lim,n1,n2):
    """
cont_mult_n1 <-0
cont_mult_n2 <-0
recorro coon la variable i el intervalo 1 hasta lim(incluido)
    si i % n1==0
        cont_mult_n1 aumento en 1
    si i % n2==0
        cont_mult_n2 aumento en 1
si el numero de multiplos de n1 es mayor al numero de mmultiplos de n2 
    retorno True
si no
    retorno False
    """ 
    cont_mult_n1=0
    cont_mult_n2=0
    for i in range(1,lim+1):
        if i % n1==0 :
            cont_mult_n1+=1
        if i % n2==0:
            cont_mult_n2+=1
    if cont_mult_n1>cont_mult_n2:
        return True
    else:
        return False
    
"""def main():
    print("Operacion",decicion_cant_multiplos(10,2,3))
main()"""

"""
b)Escribir un programa (main) que pida al usuario que ingrese varios conjuntos de valores para lim, n1 y n2.

El programa deberá llamar a la función anterior e imprimir CON EXPRESIONES DESCRIPTIVAS el resultado que ella retorna.

El ingreso de datos se termina cuando el usuario ingresa un número menor o igual a 0.


"""
def main():
    
    lim=int(input("Ingerse el valor del limite: "))
    while lim>0:
        n1=int(input("Ingerse el valor del n1: "))
        n2=int(input("Ingerse el valor del n2: "))

    
        if decicion_cant_multiplos(lim,n1,n2):
            print(f"{n1} Tiene mas multiplos que, {n2} en el intervalo 1 a {lim}")
        else:
            print(f"{n1} No tiene mas multiplos que, {n2} en el intervalo 1 a {lim}")
        
        lim=int(input("Ingerse el valor del limite: "))
main()