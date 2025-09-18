"""Ejercicio 5.7. Definir y documentar una función que, dados dos números naturales pasados
como argumentos (parámetros de la función), devuelva la suma de todas las potencias de 2
que hay en el rango formado por esos números (0, si no hay potencia de 2 entre ellos).
Utilice la función “es_potencia_de_dos” del ejercicio anterior."""
import Ejercicio_5_6
def suma_de_potencias(n1,n2):
    total_suma=0
    if not Ejercicio_5_6.es_potencia_de_dos(n1):
        return False
    else:
        for suma in range(0,n2+1):
            total_suma+=(n1**2)
        return total_suma

def main():
    n1=int(input("Ingrese numero natural: "))
    n2=int(input("Ingrese cantidad de veces a sumar: "))
    if suma_de_potencias(n1,n2):
        print(f"El resultado es {suma_de_potencias(n1,n2)}")
    else:
        print("Valor invalido")
main()