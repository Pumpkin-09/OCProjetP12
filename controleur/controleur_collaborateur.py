from models.models import Collaborateur
from models.models_managment import verification_role, hashing_password
from vue.vue import simple_print, vue_affichage_informations
from sqlalchemy import func
from vue.vue_collaborateur import vue_recherche_collaborateur, vue_creation_collaborateur, vue_modification_collaborateur
from vue.vue_menu import menu_choix_collaborateur
from models.models import EnumPermission as EP


def controleur_menu_collaborateur(collaborateur, session):
    while True:
        choix = menu_choix_collaborateur()
        if choix == 1:
            afficher_tous_collaborateur(collaborateur, session)
        if choix == 2:
            creation_collaborateur(collaborateur, session)
        if choix == 3:
            modification_collaborateur(collaborateur, session)
        if choix == 4:
            suppression_collaborateur(collaborateur, session)
        if choix == None:
            return


def recherche_collaborateur(session):
    collaborateur_chercher = vue_recherche_collaborateur()
    collaborateur = session.query(Collaborateur).filter(func.lower(Collaborateur.nom_complet) == collaborateur_chercher.lower()).first()
    return collaborateur


def creation_collaborateur(collaborateur, session):
    action = EP.creer_collaborateur
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
                nom = infos_collaborateur["nom"],
                email = infos_collaborateur["email"],
                password = hashing_password(infos_collaborateur["password"]),
                role = infos_collaborateur["role"]
            )
            session.add(nouveau_collaborateur)
            session.commit()
            simple_print(f"Collaborateur '{infos_collaborateur['nom']}' créé avec succès")

        except Exception as e:
            session.rollback()
            simple_print(f"Erreur lors de la création:/n - {e}")


def afficher_tous_collaborateur(collaborateur, session):
    action = EP.afficher_collaborateurs
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        collaborateurs = session.query(Collaborateur).all()
        if len(collaborateurs) > 0:
            vue_affichage_informations(collaborateurs)
        else:
            simple_print("Aucun collaborateur.")


def modification_collaborateur(collaborateur, session):
    action = EP.modifier_collaborateur
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        collaborateur_modifier = recherche_collaborateur()
        if collaborateur_modifier is None:
            simple_print("Ce collaborateur n'existe pas.")
            return

        try:
            modification = vue_modification_collaborateur(collaborateur_modifier)
            if collaborateur_modifier.password != modification["password"]:
                collaborateur_modifier.password = hashing_password(modification["password"])

            collaborateur_modifier.nom = modification["nom"]
            collaborateur_modifier.email = modification["email"]
            collaborateur_modifier.role = modification["role"]

            session.commit()
            simple_print(f"Collaborateur '{modification['nom']}' modiffié avec succès")

        except Exception as e:
            session.rollback()
            simple_print(f"Erreur lors de la modification:/n - {e}")


def suppression_collaborateur(collaborateur, session):
    action = EP.supprimer_collaborateur
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        delete_collaborateur = recherche_collaborateur()
        if delete_collaborateur is None:
            simple_print("Ce collaborateur n'existe pas.")
            return
        if delete_collaborateur.id == collaborateur.id:
            simple_print("Vous ne pouvez pas supprimer votre propre compte")
            return
        
        try:
            session.delete(delete_collaborateur)
            session.commit()
            simple_print(f"Collaborateur '{delete_collaborateur['nom']}' supprimé avec succès")

        except Exception as e:
            session.rollback()
            simple_print(f"Erreur lors de la suppression:/n - {e}")
