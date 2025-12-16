from vue.vue import verification_input, clear_terminal, demander_modification, choix_modification
from models.models import MyEnum
import re


def choix_role():
    roles = list(MyEnum)
    len_roles = len(roles)
    print("------Choisissez un rôle:")
    for i, role in enumerate(roles, 1):
        print(f"{i}. {role.value}.")
    while True:
        choix = verification_input("Veuillez saisir le numero correspondant:\n - ", lambda numero: numero != "")
        int_choix = int(choix)
        if int_choix in range(1, len_roles + 1):
            index = int(choix)-1
            return roles[index]
        else:
            print("Choix non valide, veuillez saisir un numero valide\n")


def vue_creation_collaborateur():
    print("Veuillez saisir le nom et prénom du collaborateur.")
    infos_collaborateur = {
    "nom": verification_input(" - ", lambda nom: re.match(r"^[a-zA-Z\s]{2,150}$", nom)),
    "email": verification_input("Veuillez saisir l'email du collaborateur':\n - ", lambda mail: mail != ""),
    "password": verification_input("Veuillez saisir le mot de passe:\n - ", lambda password: password != ""),
    "role": choix_role()
    }
    return infos_collaborateur


def vue_recherche_collaborateur():
    clear_terminal()
    print("Veuillez saisir le nom et prénom du collaborateur à chercer:")
    recherche_collaborateur = verification_input(" - ", lambda nom: re.match(r"^[a-zA-Z\s]{2,150}$", nom))
    return recherche_collaborateur


def vue_modification_collaborateur(collaborateur):
    nom = demander_modification(
        "Nom",
        collaborateur.nom,
        "Veuillez saisir le nom et prénom du collaborateur.\n - ",
        lambda nom: re.match(r"^[a-zA-Z\s]{2,150}$", nom)
    )

    email = demander_modification(
        "Email",
        collaborateur.email,
        "Veuillez saisir l'email du collaborateur:\n - ",
        lambda mail: mail != ""
    )

    print("Voulez-vous modifier le mot de passe ?")
    choix = choix_modification()
    if choix:
        password = verification_input("Veuillez saisir le mot de passe:\n - ", lambda password: password != "")
    else:
        password = collaborateur.password


    print(f"\nRole actuel: {collaborateur.role.value}")
    choix = choix_modification()
    if choix:
        role = choix_role()
    else:
        role = collaborateur.role

    infos_collaborateur = {
        "nom": nom,
        "email": email,
        "password": password,
        "role": role
        }

    return infos_collaborateur
