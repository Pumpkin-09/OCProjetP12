from vue.vue_menu import menu
from vue.vue import verification_input
from models.models import MyEnum
import re


def choix_role():
    roles = list(MyEnum)
    len_roles = len(roles)
    print("     Choisissez un rôle:")
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
    nom_complet = verification_input(" - ", lambda nom: re.match(r"^[a-zA-Z\s]{2,150}$", nom))
    email = verification_input("Veuillez saisir l'email du collaborateur':\n - ", lambda mail: mail != "")
    password = verification_input("Veuillez saisir le mot de passe:\n - ", lambda password: password != "")
    role = choix_role()
    infos_collaborateur = (nom_complet, email, password, role)
    return infos_collaborateur


def vue_affichage_collaborateur():
    pass


def vue_modification_collaborateur():
    pass


def vue_suppretion_collaborateur():
    pass
