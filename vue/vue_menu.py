import re
from vue.vue import clear_terminal, MENUS




def menu():
    while True:

        print("\n\n--------------Menu--------------")
        print("     Choisissez une option:")
        print("1. Menu client")
        print("2. Menu évenement")
        print("3. Menu collaborateur")
        print("0. Quitter l'applicaiton")
        print("---------------------------------")

        choix = input("Saisir 1, 2, 3 ou 0:\n - ")

        if choix == "1":
            clear_terminal()
            print("Menu client:\n")
            return choix

        if choix == "2":
            clear_terminal()
            print("Menu évenement:\n")
            return choix

        if choix == "3":
            clear_terminal()
            print("Menu collaborateur:\n")
            return choix

        if choix == "0":
            clear_terminal()
            return choix

        else:
            print("\nChoix invalide, Réessayez.")


def quitter():
    while True:
        choix = input("Voulez-vous quitter l'application?\nOui\nNon\n")
        if re.match(r"^OUI$", choix, re.I):
            return True
        if re.match(r"^NON$", choix, re.I):
            return False
        else:
            print("Choix non valide, entrez oui ou non\n")

def menu_client():
    while True:

        print("\n\n-----------Menu client-----------")
        print("     Choisissez une option:")
        print("1. Afficher clients")
        print("2. Nouveau client")
        print("3. Modifier client")
        print("4. Supprimer client")
        print("0. retour")
        print("---------------------------------")

        choix = input("Saisir 1, 2, 3, 4 ou 0:\n - ")

        if choix == "1":
            clear_terminal()
            print("Affichage de tous les clients:\n")
            return choix

        if choix == "2":
            clear_terminal()
            print("Créer un nouveau client:\n")
            return choix

        if choix == "3":
            clear_terminal()
            print("Modifier un client:\n")
            return choix

        if choix == "4":
            clear_terminal()
            print("Suppriner un client:\n")
            return choix

        if choix == "0":
            clear_terminal()
            return choix

        else:
            print("\nChoix invalide, Réessayez.")


def menu_evenement():
    while True:

        print("\n\n-----------Menu évenement-----------")
        print("     Choisissez une option:")
        print("1. Afficher évenements")
        print("2. Nouvel évenement")
        print("2. Modifier évenement")
        print("4. Supprimer évenement")
        print("0. retour")
        print("---------------------------------")

        choix = input("Saisir 1, 2, 3, 4 ou 0:\n - ")

        if choix == "1":
            clear_terminal()
            print("Affichage de tous les évenements:\n")
            return choix

        if choix == "2":
            clear_terminal()
            print("Création d'un nouvel évenement:\n")
            return choix

        if choix == "3":
            clear_terminal()
            print("Modifier un évenement:\n")
            return choix

        if choix == "4":
            clear_terminal()
            print("Supprimer un évenement:\n")
            return choix

        if choix == "0":
            clear_terminal()
            return choix

        else:
            print("\nChoix invalide, Réessayez.")


def menu_collaborateur():
    while True:

        print("\n\n-----------Menu collaborateur-----------")
        print("     Choisissez une option:")
        print("1. Afficher collaborateurs")
        print("1. Nouveau collaborateur")
        print("2. Modifier collaborateur")
        print("3. Supprimer collaborateur")
        print("0. retour")
        print("---------------------------------")

        choix = input("Saisir 1, 2, 3, 4 ou 0:\n - ")

        if choix == "1":
            clear_terminal()
            print("Affichage de tous les collaborateurs:\n")
            return choix

        if choix == "2":
            clear_terminal()
            print("Créer un nouveau collaborateur:\n")
            return choix

        if choix == "3":
            clear_terminal()
            print("Modifier un collaborateur:\n")
            return choix

        if choix == "4":
            clear_terminal()
            print("Supprimer un collaborateur:\n")
            return choix

        if choix == "0":
            clear_terminal()
            return choix

        else:
            print("\nChoix invalide, Réessayez.")


def afficher_menu(menu_config):
    titre = menu_config["titre"]
    options = menu_config("options")








