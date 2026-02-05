def input_number(message: str) -> float:
    saisie_in_correct = True

    while saisie_in_correct:
        try:
            nombre = float(input(message))
            saisie_in_correct = False
        except ValueError:
            print("Saisie Incorrect ! Veuillez utiliser un nombre.")

    return nombre