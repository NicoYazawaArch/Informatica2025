def main():
    cadena4="2022 Argentina campeon del Mundo"
    cad_incognita=""
    for elem in cadena4:
        if elem in "0123456789":
            cad_incognita+="*"
        else:
            cad_incognita+=elem

    print("Debug",cad_incognita)

main()