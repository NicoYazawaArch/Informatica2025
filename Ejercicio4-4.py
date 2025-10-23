"""
Ejercicio 4.4. Escribir un programa que pida al usuario que ingrese dos números naturales,
n1 y n2, e imprima en pantalla la secuencia de enteros comprendida entre n1 y n2
(incluidos) con la siguiente particularidad: si el número es múltiplo de 3, en lugar del número
debe imprimir “TRES”, si es múltiplo de 5, en vez del número debe imprimir “CINCO” y si es
múltiplo de 3 y de 5, en lugar del número debe imprimir “TRES Y CINCO”.

"""
def secuencia():
    #Ingresos del usuario
    n1=int(input("Ingrese primer numero: "))
    n2=int(input("Ingrese segundo numero: "))
    #Cambia de posicion si el primer numero es menor al mayor porque no imprime nada si no
    if n1>n2:
        n1,n2=n2,n1
    #Bucle qque busca los multiplis de 3 y 5    
    for i in range(n1,n2+1):
        if i %3 == 0 and i %5 == 0:
            print("Tres y Cinco")
        elif i % 3 == 0 :
            print("Tres")
        elif i % 5 ==0:
            print("Cinco")
        else:
            print(i)
secuencia()

