def main():
    a = 1
    b = 3.5
    seguir = True
    producto = 1
    while a < 4 and seguir:
        producto *= b - a
    if producto < 2:
        print("Muy bajo")
    elif producto > 5:
        print("Demasiado alto")
        seguir = False
    else:
        print("Valor aceptable")
    a += 1
    print("Producto:", producto)
    
    
main()