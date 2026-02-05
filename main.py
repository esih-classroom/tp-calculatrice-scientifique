from ipyllogger import Logger
from ipyllogger import level

from function import input_number, read_file, write_line

logger = Logger()

file_path = 'data.txt'

def main():

    logger.log("Session start", level=level.WARNING)

    continuer = True

    while continuer:
        print("Choisir une option: \n")

        options = [
            'Quitter',
            'Addition',
            'Soustraction',
            'Multiplication',
            'Division',
            'Historique des opérations'
        ]
        
        for position, op in enumerate(options):
            print(f"{position}.- {op}")

        option = input_number(">>> ")

        if 0 >= option < len(options):
            print(f"Choix invalide. Vous devez choisir un nombre entre 0 et {len(options)}")
            continue

        if option == 0:
            logger.log("Session ends", level=level.WARNING)
            exit()

        if option == 5:
            lines = read_file(file_path)
            if len(lines) < 0:
                print("Aucune donnees disponible")
            else:
                for line in lines:
                    print(line)

        nombre1 = input_number("Entrer le premier nombre: ")
        nombre2 = input_number("Entrer le second nombre : ")

        resultat = 0
        operateur = ""

        if option == 1:
            operateur = "+"
            resultat = nombre1 + nombre2
        elif option == 2:
            operateur = '-'
            resultat = nombre1 - nombre2
        elif option == 3:
            operateur = '*'
            resultat = nombre1 * nombre2
        elif option == 4:
            operateur = '/'
            while nombre2 == 0:
                print("On ne peut pas diviser par 0")
                nombre2 = input_number("Entrer le second nombre : ")
            resultat = nombre1 / nombre2
        else:
            # exit()
            logger.log("Session ends", level=level.WARNING)
            return

        print(f"Le resultat est: {resultat}")

        write_line(file_path, f"{nombre1} {operateur} {nombre2} = {resultat}\n")

        choix = input("Voulez vous continuer (o/n) [n]: ")

        if choix == 'o' or choix == 'O':
            continuer = True
        else:
            logger.log("Session ends", level=level.WARNING)
            continuer = False

if __name__ == "__main__":
    main()
