from models.models import Evenement
from models.models_managment import verification_role, verification_type
from models.models import EnumPermission as EP
from controleur_client import recherche_client
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
        client = recherche_client()
        if client is None:
            simple_print("Client introuvable.")
            return

        infos_evenement = vue_creation_evenement()

        try:
            nouvel_evenement = Evenement(
                name_event = infos_evenement["nom"],
                id_client = client.id,
                id_collaborateur = collaborateur.id,
                event_date_start = infos_evenement["date debut"],
                event_date_stop = infos_evenement["date fin"],
                location = infos_evenement["location"],
                attente = verification_type(infos_evenement["attente"]),
                note = infos_evenement["notes"]
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
            evenements = session.query(Evenement).filter(Evenement.id_support_contrat == False).all()
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
        try:
            modification = vue_modification_evenement(evenement)

            evenement.name_event = modification["name_event"]
            evenement.id_client = verification_type(modification["id_client"])
            evenement.id_collaborateur = verification_type(modification["id_collaborateur"])
            evenement.event_date_start = modification["date_start"]
            evenement.event_date_stop = modification["date_stop"]
            evenement.id_support_contrat= verification_type(modification["id_support_contrat"])
            evenement.location = modification["location"]
            evenement.attente = verification_type(modification["attente"])
            evenement.note = modification["note"]

            session.commit()
            simple_print(f"Evenement modiffié avec succès")

        except Exception as e:
            session.rollback()
            simple_print(f"Erreur lors de la modification:/n - {e}")
