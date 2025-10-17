import datetime


def simple_print(word):
    print(word)


def choix_modification():
    while True:
        choix = input(" Voulez vous le modifier?\n 0. Non\n 1. Oui\n - ")
        if choix == "0":
            return False
        if choix =="1":
            return True
        else:
            print("Choix invalide, veuillez saisir 0 ou 1")


def input_user_identifient():
    identifient = input("veuiller saisir votre identifient:/n - ")
    password = input("Veuillez saisir votre mot de passe:/n - ")
    
    return [identifient, password]


def vue_affichage_informations(objets):
    for objet in objets:
        print(f"\n\n------------")
        print(objet)


def clear_terminal():
    print("\033[2J", end="")
    print(f"\033[{6};{0}H", end="")


def verification_input(question, condition_validite):
    while True:
        reponse = input(question)
        if condition_validite(reponse):
            return reponse
        else:
            print("Saisie invalide. Veuillez réessayer.")


def verification_date(date_str):
    # Vérification si la date est au format JJ/MM/AAAA
    try:
        jour, mois, annee = map(int, date_str.split('/'))
        datetime.date(annee, mois, jour)
        return True

    except ValueError:
        return False


def demander_modification(label, valeur_actuelle, question, validation):
    print(f"\n{label} actuel: {valeur_actuelle}")
    if choix_modification():
        return verification_input(question, validation)
    return valeur_actuelle


def vue_choix(nombre_choix):
    while True:
        print("Pour quiter, veuillez saisir 0:")
        choix_str = input(" - ")
        choix = int(choix_str)
        if choix == 0:
            return None
        if choix in range(1, nombre_choix +1):
            return choix
        else:
            print(f"Choix invalide, veuillez saisir un nombre compris entre 0 et {nombre_choix}")
