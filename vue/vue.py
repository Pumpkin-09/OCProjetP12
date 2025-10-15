import datetime


MENUS = {
    "principal": {
        "titre": "Menu",
        "options": {
            "1": {"label": "Menu client", "action": "menu_client"},
            "2": {"label": "Menu événement", "action": "menu_evenement"},
            "3": {"label": "Menu contrat", "action": "menu_contrat"},
            "4": {"label": "Menu collaborateur", "action": "menu_collaborateur"},
            "0": {"label": "Quitter l'application", "action": "quitter"}
        }
    },
    "client": {
        "titre": "Menu client",
        "options": {
            "1": {"label": "Afficher clients", "message": "Affichage de tous les clients:\n"},
            "2": {"label": "Nouveau client", "message": "Créer un nouveau client:\n"},
            "3": {"label": "Modifier client", "message": "Modifier un client:\n"},
            "0": {"label": "retour", "action": "retour"}
        }
    },
    "collaborateur": {
        "titre": "Menu collaborateur",
        "options": {
            "1": {"label": "Afficher collaborateurs", "message": "Affichage de tous les collaborateurs:\n"},
            "2": {"label": "Nouveau collaborateur", "message": "Créer un nouveau collaborateur:\n"},
            "3": {"label": "Modifier collaborateur", "message": "Modifier un collaborateur:\n"},
            "4": {"label": "Supprimer collaborateur", "message": "Supprimer un collaborateur:\n"},
            "0": {"label": "retour", "action": "retour"}
        }
    },
    "contrat": {
        "titre": "Menu contrat",
        "options": {
            "1": {"label": "Afficher contrats", "message": "Affichage de tous les contrats:\n"},
            "2": {"label": "nouveau contrat", "message": "Création d'un nouveau contrat:\n"},
            "3": {"label": "Modifier contrat", "message": "Modifier un contrat:\n"},
            "0": {"label": "retour", "action": "retour"}
        }
    },
    "evenement": {
        "titre": "Menu événement",
        "options": {
            "1": {"label": "Afficher événements", "message": "Affichage de tous les événements:\n"},
            "2": {"label": "Nouvel événement", "message": "Création d'un nouvel événement:\n"},
            "3": {"label": "Modifier événement", "message": "Modifier un événement:\n"},
            "0": {"label": "retour", "action": "retour"}
        }
    },
}


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
        if choix in range(1 in nombre_choix +1):
            return choix
        else:
            print(f"Choix invalide, veuillez saisir un nombre compris entre 0 et {nombre_choix}")
