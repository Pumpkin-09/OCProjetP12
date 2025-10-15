from database import SessionLocal
from models.models_managment import user_deconnexion, verification_password, verification_role
from models.models import Collaborateur, Client, Evenement
from vue.vue import simple_print, input_user_identifient
from vue.vue_client import vue_creation_client



def main():
    session = SessionLocal()
    connexion = False

    while not connexion:
        simple_print("Vous devez être connecté pour utiliser cette application")
        identifient_user = input_user_identifient()
        user_email = identifient_user[0]
        user_password = identifient_user[1]
        collaborateur = session.query(Collaborateur).filter(Collaborateur.email == user_email).first()
        if collaborateur and verification_password(collaborateur.password, user_password):
            connexion = True
            word = f"connexion réussi./n Bonjour {collaborateur.nom}"
        else:
            word = "Identifiants incorecte"
        simple_print(word)




    connexion = user_deconnexion()
    return


if __name__ == "__main__":
    main()
