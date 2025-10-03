from models.models import Collaborateur
from models.user_managment import verification_role
from vue.vue import simple_print
from sqlalchemy import func
from vue.vue_collaborateur import vue_recherche_collaborateur, vue_creation_collaborateur, vue_affichage_collaborateur, vue_modification_collaborateur


def recherche_collaborateur(session):
    collaborateur_chercher = vue_recherche_collaborateur()
    collaborateur = session.query(Collaborateur).filter(func.lower(Collaborateur.nom_complet) == collaborateur_chercher.lower()).first()
    return collaborateur


def creation_collaborateur(collaborateur, session):
    action = "creer collaborateur"
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        infos_collaborateur = vue_creation_collaborateur()
        email_existe = session.query(Collaborateur).filter(Collaborateur.email == infos_collaborateur["email"]).first()
        if email_existe:
            simple_print("Email déjà utilisé")
            return
        try:
            nouveau_collaborateur = Collaborateur(
                nom_complet = infos_collaborateur["nom"],
                email = infos_collaborateur["email"],
                password = infos_collaborateur["password"],
                role = infos_collaborateur["role"]
            )
            session.add(nouveau_collaborateur)
            session.commit()
            simple_print(f"Collaborateur '{infos_collaborateur['nom']}' créé avec succès")

        except Exception as e:
            session.rollback()
            simple_print(f"Erreur lors de la création:/n - {e}")


def afficher_tous_collaborateur(collaborateur, session):
    action = "affichage collaborateur"
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        collaborateurs = session.query(Collaborateur).all()
        vue_affichage_collaborateur(collaborateurs)


def modification_collaborateur(collaborateur, session):
    action = "modifier collaborateur"
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        collaborateur = recherche_collaborateur()
        if collaborateur is None:
            simple_print("Ce collaborateur n'existe pas.")
            return

        try:
            modification = vue_modification_collaborateur(collaborateur)

            Collaborateur(
                nom_complet = modification["nom"],
                email = modification["email"],
                password = modification["password"],
                role = modification["role"]
            )
            session.commit()
            simple_print(f"Collaborateur '{modification['nom']}' modiffié avec succès")

        except Exception as e:
            session.rollback()
            simple_print(f"Erreur lors de la modification:/n - {e}")
