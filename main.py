# import function
# from function import input_number
from package.function import input_number

from ipyllogger import Logger
from ipyllogger import level

logger = Logger()

def main():

    logger.log("Session start", level=level.WARNING)

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
            logger.log("Session ends", level=level.WARNING)
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
            while nombre2 == 0:
                print("On ne peut pas diviser par 0")
                nombre2 = input_number("Entrer le second nombre : ")
            resultat = nombre1 / nombre2
        else:
            # exit()
            logger.log("Session ends", level=level.WARNING)
            return

        print(f"Le resultat est: {resultat}")

        choix = input("Voulez vous continuer (o/n) [n]: ")

        if choix == 'o' or choix == 'O':
            continuer = True
        else:
            logger.log("Session ends", level=level.WARNING)
            continuer = False

if __name__ == "__main__":
    main()
