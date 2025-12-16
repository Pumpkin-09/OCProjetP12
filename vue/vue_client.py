from vue.vue import verification_input, clear_terminal, demander_modification, vue_choix
import re


def vue_recherche_client():
    clear_terminal()
    print("Veuillez saisir le nom et prénom du client à chercer:")
    recherche_client = verification_input(" - ", lambda nom: re.match(r"^[a-zA-Z\s]{2,150}$", nom))
    return recherche_client


def vue_creation_client():
    print("Veuillez saisir le nom et prénom du client.")
    infos_client = {
    "nom": verification_input(" - ", lambda nom: re.match(r"^[a-zA-Z\s]{2,150}$", nom)),
    "email": verification_input("Veuillez saisir l'email du client':\n - ", lambda mail: mail != ""),
    "telephone": verification_input("Veuillez saisir le numero de telephone du client:\n - ", lambda telephone: re.match(r"^\+\d+$", telephone)),
    "entreprise": verification_input("Veuillez saisir le nom de l'entreprise:\n - ", lambda entreprise: entreprise != "")
    }
    return infos_client


def vue_modification_client(client):
    nom = demander_modification(
        "Nom",
        client.nom_complet,
        "Veuillez saisir le nom et prénom du client.\n - ",
        lambda nom: re.match(r"^[a-zA-Z\s]{2,150}$", nom)
    )

    email = demander_modification(
        "L'email",
        client.email,
        "Veuillez saisir l'email du client:\n - ",
        lambda mail: mail != ""
    )

    telephone = demander_modification(
        "Le numéro de telephone",
        client.telephone,
        "Veuillez saisir le numero de telephone du client:\n - ",
        lambda telephone: re.match(r"^\+\d+$", telephone)
    )

    entreprise = demander_modification(
        "Nom de l'entreprise",
        client.nom_entreprise,
        "Veuillez saisir le nom de l'entreprise:\n - ",
        lambda entreprise: entreprise != ""
    )

    id_collaborateur = demander_modification(
        "Collaborateur",
        client.id_collaborateur,
        "Veuillez saisir l'ID du collaborateur:\n - ",
        lambda id_collaborateur: re.match(r"^\d+$", id_collaborateur)
    )

    infos_client = {
        "nom": nom,
        "email": email,
        "telephone": telephone,
        "entreprise": entreprise,
        "collaborateur": id_collaborateur
        }

    return infos_client


def vue_filtre_client():
    print("Pour afficher tous les clients, veuillez saisir 1\n")
    print("Pour afficher vos clients, veuillez saisir 2\n")
    return vue_choix(2)
