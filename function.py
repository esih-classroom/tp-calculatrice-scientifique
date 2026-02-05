def input_number(message: str) -> float:
    saisie_in_correct = True

    while saisie_in_correct:
        try:
            nombre = float(input(message))
            saisie_in_correct = False
        except ValueError:
            print("Saisie Incorrect ! Veuillez utiliser un nombre.")

    return nombre


def read_file(path: str) -> list:
    try:
        with open(path) as f:
            return f.readlines()
    except FileNotFoundError:
        return []
    
def write_line(path: str, line: str) -> None:
    with open(path, 'a') as file:
        file.write(line)
