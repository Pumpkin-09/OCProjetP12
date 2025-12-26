from models.models import Evenement
from datetime import datetime
from models.models_managment import verification_role
from models.models import EnumPermission as EP
from controleur.controleur_client import recherche_client
from vue.vue import simple_print, vue_affichage_informations
from vue.vue_menu import menu_choix
from vue.vue_evenement import(
                            vue_choix_recherche_evenement,
                            vue_choix_evenement,
                            vue_filtre_evenement,
                            vue_creation_evenement,
                            vue_modification_evenement
                            )


def controleur_menu_evenement(collaborateur, session):
    while True:
        choix = menu_choix("événement")
        if choix == 1:
            affichage_evenements(collaborateur, session)
        if choix == 2:
            creation_evenement(collaborateur, session)
        if choix == 3:
            modification_evenement(collaborateur, session)
        if choix == None:
            return


def creation_evenement(collaborateur, session):
    action = EP.creer_evenement
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        client = recherche_client(session)
        if client is None:
            simple_print("Client introuvable.")
            return

        infos_evenement = vue_creation_evenement()

        try:
            nouvel_evenement = Evenement(
                name_event = infos_evenement["nom"],
                id_client = client.id,
                id_collaborateur = collaborateur.id,
                event_date_start = datetime.strptime(infos_evenement["date debut"], "%d/%m/%Y").date(),
                event_date_stop = datetime.strptime(infos_evenement["date fin"], "%d/%m/%Y").date(),
                location = infos_evenement["location"],
                attente = int(infos_evenement["attente"]),
                note = infos_evenement["note"]
                )
            session.add(nouvel_evenement)
            session.commit()
            simple_print(f"Evenement créé avec succès")

        except Exception as e:
            session.rollback()
            simple_print(f"Erreur lors de la création:/n - {e}")


def affichage_evenements(collaborateur, session):
    action = EP.afficher_evenement
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        choix_evenement = vue_filtre_evenement()
        if choix_evenement == 1:
            evenements = session.query(Evenement).all()
        if choix_evenement == 2:
            evenements = session.query(Evenement).filter(Evenement.id_collaborateur == collaborateur.id).all()
        if choix_evenement == 3:
            evenements = session.query(Evenement).filter(Evenement.id_support_contrat.is_(None)).all()
        if choix_evenement == None:
            return
        if evenements:
            vue_affichage_informations(evenements)
        else:
            simple_print("Aucun événement correspondant.")


def modification_evenement(collaborateur, session):
    action = EP.modifier_contrat
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        choix_recherche = vue_choix_recherche_evenement()
        if choix_recherche is None:
            return

        if choix_recherche == 1:
            client = recherche_client(session)
            if client is None:
                return
            else:
                evenements = session.query(Evenement).filter(Evenement.id_client == client.id).all()

            if len(evenements) > 1:
                choix_evenement_str = vue_choix_evenement(evenements)
                choix_evenement = int(choix_evenement_str)
                evenement = session.query(Evenement).filter(Evenement.id == choix_evenement).first()

            elif evenements is None:
                simple_print("Aucun événement trouvé.")

        if choix_recherche == 2:
            choix_evenement_str = vue_choix_evenement(None)
            choix_evenement = int(choix_evenement_str)
            evenement = session.query(Evenement).filter(Evenement.id == choix_evenement).first()
            if evenement is None:
                simple_print("Aucun événement trouvé.")
                return

        try:
            modification = vue_modification_evenement(evenement)
            if isinstance(modification["date debut"], str):
                date_start = datetime.strptime(modification["date debut"], "%d/%m/%Y").date()
            else:
                date_start = modification["date debut"]

            if isinstance(modification["date fin"], str):
                date_stop = datetime.strptime(modification["date fin"], "%d/%m/%Y").date()
            else:
                date_stop = modification["date fin"]

            evenement.name_event = modification["nom"]
            evenement.id_client = int(modification["ID client"])
            evenement.id_collaborateur = int(modification["ID collaborateur"])
            evenement.event_date_start = date_start
            evenement.event_date_stop = date_stop
            evenement.id_support_contrat= int(modification["ID collaborateur support"])
            evenement.location = modification["location"]
            evenement.attente = int(modification["attente"])
            evenement.note = modification["note"]

            session.commit()
            simple_print(f"Evenement modiffié avec succès")

        except Exception as e:
            session.rollback()
            simple_print(f"Erreur lors de la modification:/n - {e}")
