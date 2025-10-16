import re
from vue.vue import(
                    verification_input,
                    clear_terminal,
                    demander_modification,
                    vue_affichage_informations,
                    vue_choix,
                    verification_date
                    )


def vue_choix_recherche_evenement():
    clear_terminal()
    print("Pour chercher l'événemen par le nom du client, veuillez saisir 1\n")
    print("Pour chercher l'événement par l'ID de l'événement, veuillez saisir 2\n")
    return vue_choix(2)


def vue_creation_evenement():
    infos_evenement = {}
    print("Veuillez saisir un nom pour l'événement:")
    infos_evenement["nom"] = verification_input(" - ", lambda nom: re.match(r"^[a-zA-Z\s]{2,150}$", nom))

    print("Veuillez saisir la date de début de l'événement, au format JJ/MM/AAAA:")
    infos_evenement["date debut"] = verification_input(" - ", verification_date)
    
    print("Veuillez saisir la date de fin de l'événement, au format JJ/MM/AAAA:")
    infos_evenement["date fin"] = verification_input(" - ", verification_date)

    print("Veuillez saisir une location pour l'événement:")
    infos_evenement["location"] = verification_input(" - ", lambda location: location != "")

    print("Veuillez saisir le nombre de personne attendu à l'événement:")
    infos_evenement["attente"] = verification_input(" - ", lambda attente: re.match(r"^\d+$", attente))

    choix_note = input("Voulez-vous ajouter une remarque pour cet événement?\nSaisissez Oui ou Non\n")
    if re.match(r"^OUI$", choix_note, re.I):
        notes = []
        print("Pour allez à la ligne pressez une fois \"Entrée\".\nPour quitter, presser deux fois \"Entrée\".")
        while True:
            note = input("\nSaissisez vos notes pour cet événement:\n - ")
            if note == "":
                break
            notes.append(note)
    else:
        notes = ["Aucune remarque"]
    infos_evenement["notes"] = notes

    return infos_evenement


def vue_modification_evenement(evenement):
    client = demander_modification(
        "ID client",
        evenement.id_client,
        "Veuillez saisir l'ID du client.\n - ",
        lambda id_client: re.match(r"^\d+$", id_client)
    )

    collaborateur = demander_modification(
        "ID collaborateur",
        evenement.id_collaborateur,
        "Veuillez saisir l'ID du collaborateur:\n - ",
        lambda id_collaborateur: re.match(r"^\d+$", id_collaborateur)
    )

    collaborateur_support = demander_modification(
        "ID collaborateur support",
        evenement.id_collaborateur_support,
        "Veuillez saisir l'ID du collaborateur support:\n - ",
        lambda id_collaborateur_support: re.match(r"^\d+$", id_collaborateur_support)
    )

    date_debut = demander_modification(
        "La date de début",
        evenement.event_date_start,
        "Veuillez saisir la date de début de l'événement, au format JJ/MM/AAAA:\n - ",
        verification_date
    )

    date_fin = demander_modification(
        "La date de fin",
        evenement.event_date_stop,
        "Veuillez saisir la date de fin de l'événement, au format JJ/MM/AAAA:\n - ",
        verification_date
    )

    location = demander_modification(
        "Location",
        evenement.location,
        "Veuillez saisir une location pour l'événement:\n - ",
        lambda location: location != ""
    )

    attente = demander_modification(
        "Attente",
        evenement.attente,
        "Veuillez saisir le nombre de personne attendu à l'événement:\n - ",
        lambda attente: re.match(r"^\d+$", attente)
    )

    print(f"Note acctuelle:\n{evenement.note}")
    choix_note = input("Voulez-vous rajouter une remarque pour cet événement?\nSaisissez Oui ou Non\n")
    notes = []
    if re.match(r"^OUI$", choix_note, re.I):
        print("Pour allez à la ligne pressez une fois \"Entrée\".\nPour quitter, presser deux fois \"Entrée\".")
        while True:
            note = input("\nSaissisez vos notes pour cet événement:\n - ")
            if note == "":
                break
            notes.append(note)

    infos_evenement = {
        "id_client": client,
        "id_collaborateur": collaborateur,
        "id_collaborateur_support": collaborateur_support,
        "date_debut": date_debut,
        "date_fin": date_fin,
        "location": location,
        "attente": attente,
        "notes": notes
        }

    return infos_evenement

def vue_choix_evenement(evenements):
    if evenements:
        vue_affichage_informations(evenements)
    choix = input("Veuillez saisir l'ID de l'événement\n - ")
    return choix


def vue_filtre_evenement():
    print("Pour afficher tous les événements, veuillez saisir 1\n")
    print("Pour afficher vos événements, veuillez saisir 2\n")
    print("Pour afficher les événements sans collaborateur support, veuillez saisir 3\n")
    return vue_choix(3)
