def main():

    saisie_in_correct = True

    while saisie_in_correct:
        try:

            nombre1 = float(input("Entrer le premier nombre: "))
            nombre2 = float(input("Entre le second nombre: "))

            saisie_in_correct = False

            print(f"La somme est: {nombre1 + nombre2}")
        except ValueError:
            print("Saisie Incorrect ! Veuillez utiliser des nombres .")


if __name__ == "__main__":
    main()
