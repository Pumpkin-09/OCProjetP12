from database import SessionLocal
from models.models_managment import user_connexion, user_deconnexion
from models.models import Collaborateur
from vue.vue import simple_print
from vue.vue_menu import menu, quitter
from controleur.controleur_client import controleur_menu_client
from controleur.controleur_collaborateur import controleur_menu_collaborateur, creation_first_collaborateur
from controleur.controleur_contrat import controleur_menu_contrat
from controleur.controleur_evenement import controleur_menu_evenement


def main():
    session = SessionLocal()
    collaborateur = False
    collaborateur_existe = session.query(Collaborateur).first()
    if not collaborateur_existe:
        creation_first_collaborateur(session)

    while not collaborateur:
        simple_print("Vous devez être connecté pour utiliser cette application")
        collaborateur = user_connexion(session)
        if not collaborateur:
            stop = quitter()
            if stop:
                return

    while True:
        choix_menu = menu()
        if choix_menu == 1:
            controleur_menu_client(collaborateur, session)

        if choix_menu == 2:
            controleur_menu_evenement(collaborateur, session)

        if choix_menu == 3:
            controleur_menu_contrat(collaborateur, session)

        if choix_menu == 4:
            controleur_menu_collaborateur(collaborateur, session)

        if choix_menu == None:
            stop = quitter()
            if stop:
                user_deconnexion(session)
                return


if __name__ == "__main__":
    main()
