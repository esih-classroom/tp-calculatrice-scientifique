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
    nombre1 = input_number("Entrer le premier nombre: ")
    nombre2 = input_number("Entrer le second nombre : ")
    
    print(f"La somme est: {nombre1 + nombre2}")

if __name__ == "__main__":
    main()
