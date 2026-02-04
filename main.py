def input_number(message: str) -> float:
    saisie_in_correct = True

    while saisie_in_correct:
        try:
            nombre = float(input(message))
            saisie_in_correct = False
        except ValueError:
            print("Saisie Incorrect ! Veuillez utiliser un nombre.")

    return nombre


def main():

    continuer = True

    while continuer:

        print("Choisir une option: \n")
        
        print("1: Addition")
        print("2: Soustraction")
        print("3: Multiplication")
        print("4: Division")
        print("0: Quitter")

        option = input_number(">>> ")

        if option == 0:
            exit()

        if option not in [1, 2, 3, 4]:
            print("Choix invalide.")
            continue
        

        nombre1 = input_number("Entrer le premier nombre: ")
        nombre2 = input_number("Entrer le second nombre : ")

        resultat = 0

        if option == 1:
            resultat = nombre1 + nombre2
        elif option == 2:
            resultat = nombre1 - nombre2
        elif option == 3:
            resultat = nombre1 * nombre2
        elif option == 4:
            resultat = nombre1 / nombre2
        else:
            # exit()
            return

        print(f"Le resultat est: {resultat}")

        choix = input("Voulez vous continuer (o/n) [n]: ")

        if choix == 'o' or choix == 'O':
            continuer = True
        else:
            continuer = False

if __name__ == "__main__":
    main()
