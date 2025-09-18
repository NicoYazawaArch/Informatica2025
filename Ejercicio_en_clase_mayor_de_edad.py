def mayor_de_edad(edad):
    if edad>=100:
        print("Hola Mirta")
        
    elif edad>=18:
        print("La persona es mayor de edad")
    else:
        print("No es mayor de edad")
    print("Debug: exit ")

def main():
    edad=int(input("Ingrese edad: "))
    mayor_de_edad(edad)

main()
    
