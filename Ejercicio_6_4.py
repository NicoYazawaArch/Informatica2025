"""
Ejercicio 6.4. Definir una función que reciba una cadena de caracteres como parámetro e
imprima la cadena original yuxtapuesta a la cadena invertida. [Ej: para el argumento ‘espejo’
debería imprimir ‘espejoojepse’ ]. ¿Qué función debería invocar?
"""
import Ejercicio_6_3
def espejo(cadena):
    txt=""
    inverso=Ejercicio_6_3.invertircad(cadena)
    txt=cadena+inverso
    return txt

def main():
    palabra=input("ingrese palabra para espejo: ")
    print(f"palabra reflectada: {espejo(palabra)}")
main()