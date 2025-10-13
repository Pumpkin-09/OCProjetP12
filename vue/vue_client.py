from vue.vue_menu import menu
from vue.vue import verification_input, choix_modification, clear_terminal, demander_modification
import re


def vue_recherche_client():
    pass


def vue_creation_client():
    print("Veuillez saisir le nom et prénom du client.")
    infos_client = {
    "nom_complet": verification_input(" - ", lambda nom: re.match(r"^[a-zA-Z\s]{2,150}$", nom)),
    "email": verification_input("Veuillez saisir l'email du client':\n - ", lambda mail: mail != ""),
    "telephone": verification_input("Veuillez saisir le numero de telephone du client:\n - ", lambda telephone: re.match(r"^\+\d+$", telephone)),
    "nom_entreprise": verification_input("Veuillez saisir le nom de l'entreprise:\n - ", lambda entreprise: entreprise != "")
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

    collaborateur = demander_modification(
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





