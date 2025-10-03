from vue.vue_menu import menu
from vue.vue import verification_input
import re


def vue_recherche_client():
    pass


def vue_creation_client():
    print("Veuillez saisir le nom et prénom du client.")
    nom_complet = verification_input(" - ", lambda nom: re.match(r"^[a-zA-Z\s]{2,150}$", nom))
    email = verification_input("Veuillez saisir l'email du client':\n - ", lambda mail: mail != "")
    telephone = verification_input("Veuillez saisir le numero de telephone du client:\n - ", lambda telephone: re.match(r"^\+\d+$", telephone))
    nom_entreprise = verification_input("Veuillez saisir le nom de l'entreprise:\n - ", lambda entreprise: entreprise != "")
    infos_client = (nom_complet, email, telephone, nom_entreprise)
    return infos_client


def vue_affichage_client():
    pass


def vue_modification_client():
    pass





