from vue.vue_menu import menu
from vue.vue_verification import verification_input, verification_date
from models.models import MyEnum
import re


def nouveau_client(list_email):
    print("Veuillez saisir le nom et prénom du client.")
    nom_complet = verification_input(" - ", lambda nom: re.match(r"^[a-zA-Z\s]{2,150}$", nom))
    email = verification_input("Veuillez saisir l'email du client':\n - ", lambda mail: mail != "")
    if email in list_email:
        print(f"l'email {email} est déjà présent dans la base de données.")
        return None
    telephone = verification_input("Veuillez saisir le numero de telephone du client:\n - ", lambda telephone: telephone != "")
    nom_entreprise = verification_input("Veuillez saisir le nom de l'entreprise:\n - ", lambda entreprise: entreprise != "")
    infos_client = (nom_complet, email, telephone, nom_entreprise)
    return infos_client


def choix_role():
    roles = list(MyEnum)
    print("     Choisissez un rôle:")
    for i, role in enumerate(roles, 1):
        print(f"{i}. {role.value}.")
    while True:
        choix = verification_input("Veuillez saisir le numero conrespondant:\n - ", lambda numero: numero != "")
        if choix in ["1", "2", "3"]:
            index = int(choix)-1
            return roles[index]
        else:
            print("Choix non valide, entrez 1, 2 ou 3\n")


def nouveau_collaborateur(list_email):
    print("Veuillez saisir le nom et prénom du collaborateur.")
    nom_complet = verification_input(" - ", lambda nom: re.match(r"^[a-zA-Z\s]{2,150}$", nom))
    email = verification_input("Veuillez saisir l'email du collaborateur':\n - ", lambda mail: mail != "")
    if email in list_email:
        print(f"l'email {email} est déjà présent dans la base de données.")
        return None
    password = verification_input("Veuillez saisir le mot de passe:\n - ", lambda telephone: telephone != "")
    role = choix_role()
    infos_collaborateur = (nom_complet, email, password, role)
    return infos_collaborateur


#def nouveau_contrat():
    print("Veuillez saisir le nom et prénom du client.")
    nom_complet = verification_input(" - ", lambda nom: re.match(r"^[a-zA-Z\s]{2,150}$", nom))
    email = verification_input("Veuillez saisir l'email du client':\n - ", lambda mail: mail != "")
    if email in settings:
        print(f"l'email {email} est déjà présent dans la base de données.")
        return None
    telephone = verification_input("Veuillez saisir le numero de telephone du client:\n - ", lambda telephone: telephone != "")
    nom_entreprise = verification_input("Veuillez saisir le nom de l'entreprise:\n - ", lambda entreprise: entreprise != "")
    infos_client = (nom_complet, email, telephone, nom_entreprise)
    return infos_client


#def nouveau_evenement():
    print("Veuillez saisir le nom et prénom du client.")
    nom_complet = verification_input(" - ", lambda nom: re.match(r"^[a-zA-Z\s]{2,150}$", nom))
    email = verification_input("Veuillez saisir l'email du client':\n - ", lambda mail: mail != "")
    if email in settings:
        print(f"l'email {email} est déjà présent dans la base de données.")
        return None
    telephone = verification_input("Veuillez saisir le numero de telephone du client:\n - ", lambda telephone: telephone != "")
    nom_entreprise = verification_input("Veuillez saisir le nom de l'entreprise:\n - ", lambda entreprise: entreprise != "")
    infos_client = (nom_complet, email, telephone, nom_entreprise)
    return infos_client
