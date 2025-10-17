import re
from vue.vue import clear_terminal, vue_choix


def menu():

    clear_terminal()
    print("--------------Menu--------------")
    print("     Choisissez une option:")
    print("Pour le menu client, veuillez saisir 1")
    print("Pour le menu événement, veuillez saisir 2")
    print("Pour le menu Contrat, veuillez saisir 3")
    print("Pour le menu collaborateur, veuillez saisir 4")
    choix = vue_choix(4)
    print("---------------------------------")

    return choix


def menu_choix(item):

    clear_terminal()
    print(f"-----------Menu {item}-----------")
    print("     Choisissez une option:")
    print(f"Pour afficher les {item}, veuillez saisir 1")
    print(f"Pour crée un {item}, veuillez saisir 2")
    print(f"Pour modifier un {item}, veuillez saisir 3")
    choix = vue_choix(3)
    print("---------------------------------")

    return choix


def menu_choix_collaborateur():

    clear_terminal()
    print("-----------Menu collaborateur-----------")
    print("     Choisissez une option:")
    print("Pour le afficher les collaborateurs, veuillez saisir 1")
    print("Pour crée un collaborateur, veuillez saisir 2")
    print("Pour modifier un collaborateur, veuillez saisir 3")
    print("Pour supprimer un collaborateur, veuillez saisir 4")
    choix = vue_choix(4)
    print("---------------------------------")

    return choix


def quitter():
    while True:
        choix = input("Voulez-vous quitter l'application?\nOui\nNon\n")
        if re.match(r"^OUI$", choix, re.I):
            return True
        if re.match(r"^NON$", choix, re.I):
            return False
        else:
            print("Choix non valide, entrez oui ou non\n")
