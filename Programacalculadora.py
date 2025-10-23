
def entrada():
    n1=float(input("Ingrese el primer numero: "))
    n2=float(input("Ingrese el segundo numero: "))
    return n1, n2

def suma(n1,n2):
    resultado=n1+n2
    return resultado

def resta(n1,n2):
    resultado=n1-n2
    return resultado

def multiplicacion(n1,n2):
    resultado=n1*n2
    return resultado

def division(n1,n2):
    resultado=n1/n2
    return resultado

def calculo():
    n1, n2 = entrada()
    print("El resultado de la suma es:", suma(n1, n2))
    print("El resultado de la resta es:", resta(n1, n2))
    print("El resultado de la multiplicacion es:", multiplicacion(n1, n2))
    print("El resultado de la division es:", division(n1, n2))

calculo()    
