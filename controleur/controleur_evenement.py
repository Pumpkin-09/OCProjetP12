from models.models import Evenement
from models.models_managment import verification_role
from models.models import EnumPermission as EP
from sqlalchemy import func
from controleur_client import recherche_client
from vue.vue import simple_print, vue_affichage_informations
from vue.vue_contrat import vue_recherche_evenement, vue_creation_evenement, vue_modification_evenement


def creation_evenement(collaborateur, session):
    action = EP.creer_evenement
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        client = recherche_client()
        if client is None:
            simple_print("Client introuvable.")
            return

        infos_evenement = vue_creation_evenement()

        try:
            nouvel_evenement = Evenement(
                name_event = infos_evenement["name_event"],
                id_client = client.id,
                id_collaborateur = collaborateur.id,
                event_date_start = infos_evenement["date_start"],
                event_date_stop = infos_evenement["date_stop"],
                location = infos_evenement["location"],
                attente = infos_evenement["attente"],
                note = infos_evenement["note"]
                )
            session.add(nouvel_evenement)
            session.commit()
            simple_print(f"Evenement créé avec succès")

        except Exception as e:
            session.rollback()
            simple_print(f"Erreur lors de la création:/n - {e}")


def afficher_evenements(collaborateur, session):
    action = EP.afficher_evenement
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        evenements = session.query(Evenement).all()
        if evenements > 0:
            vue_affichage_informations(evenements)
        else:
            simple_print("Aucun évenement")


def afficher_evenements_sans_support(collaborateur, session):
    action = EP.afficher_evenement
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        evenements = session.query(Evenement).filter(Evenement.id_support_contrat == False).all()
        if evenements > 0:
            vue_affichage_informations(evenements)
        else:
            simple_print("Aucun évenement")


def modification_evenement(collaborateur, session):
    action = EP.modifier_evenement
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        evenement = vue_recherche_evenement()
        if evenement is None:
            client = recherche_client()
            if client is None:
                simple_print("Ce client n'existe pas.")
                return
            evenements = session.query(Evenement).filter(Evenement.id_client == client.id).all()
            if len(evenements) > 1:
                choix_evenement = vue_choix_evenement(evenements)
                evenement = evenements[choix_evenement - 1]
            elif len(evenements) == 0:
                simple_print("Evenement non trouvé.")
                return

        try:
            modification = vue_modification_evenement(evenement)

            evenement.name_event = modification["name_event"]
            evenement.id_client = modification["id_client"]
            evenement.id_collaborateur = modification["id_collaborateur"]
            evenement.event_date_start = modification["date_start"]
            evenement.event_date_stop = modification["date_stop"]
            evenement.id_support_contrat= modification["id_support_contrat"]
            evenement.location = modification["location"]
            evenement.attente = modification["attente"]
            evenement.note = modification["note"]

            session.commit()
            simple_print(f"Evenement modiffié avec succès")

        except Exception as e:
            session.rollback()
            simple_print(f"Erreur lors de la modification:/n - {e}")
