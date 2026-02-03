def main():
    nombre1 = 0
    nombre2 = 0
    
    saisie_in_correct = True

    while saisie_in_correct:
        try:
            nombre1 = float(input("Entrer le premier nombre: "))
            saisie_in_correct = False
        except ValueError:
            print("Saisie Incorrect ! Veuillez utiliser un nombre.")

    saisie_in_correct = True

    while saisie_in_correct:
        try:
            nombre2 = float(input("Entre le second nombre: "))
            saisie_in_correct = False
        except ValueError:
            print("Saisie Incorrect ! Veuillez utiliser un nombre.")

    print(f"La somme est: {nombre1 + nombre2}")

if __name__ == "__main__":
    main()
