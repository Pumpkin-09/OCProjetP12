from models.models import Contrat
from models.models_managment import verification_role, verification_type
from models.models import EnumPermission as EP
from controleur.controleur_client import recherche_client
from controleur_client import recherche_client
from vue.vue import simple_print, vue_affichage_informations
from vue.vue_contrat import vue_choix_recherche_contrat, vue_creation_contrat, vue_modification_contrat, vue_choix_contrat, vue_filtre_contrat


def creation_contrat(collaborateur, session):
    action = EP.creer_contrat
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        client = recherche_client()
        infos_contrat = vue_creation_contrat()

        try:
            nouveau_contrat = Contrat(
                id_client = client.id,
                id_collaborateur = verification_type(infos_contrat["id collaborateur"]),
                montant_total = verification_type(infos_contrat["montant"]),
                reste_a_payer = verification_type(infos_contrat["reste_a_payer"]),
                status_contrat = infos_contrat["statu du contrat"]
            )
            session.add(nouveau_contrat)
            session.commit()
            simple_print(f"Contrat créé avec succès")

        except Exception as e:
            session.rollback()
            simple_print(f"Erreur lors de la création:/n - {e}")


def filtre_afficher_contrats(collaborateur, session):
    action = EP.afficher_contrat
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        choix_contrat = vue_filtre_contrat()
        if choix_contrat == 1:
            contrats = session.query(Contrat).all()
        if choix_contrat == 2:
            contrats = session.query(Contrat).filter(Contrat.id_collaborateur == collaborateur.id).all()
        if choix_contrat == 3:
            contrats = session.query(Contrat).filter(Contrat.reste_a_payer > 0).all()
        if choix_contrat == 4:
            contrats = session.query(Contrat).filter(Contrat.status_contrat == False).all()
        if choix_contrat == None:
            return

        if len(contrats):
            vue_affichage_informations(contrats)
        else:
            simple_print("Aucun contrat correspondant.")


def modification_contrat(collaborateur, session):
    action = EP.modifier_contrat
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        choix_recherche = vue_choix_recherche_contrat()
        if choix_recherche is None:
            return

        if choix_recherche == 1:
            client = recherche_client(session)
            if client is None:
                return
            else:
                contrats = session.query(Contrat).filter(Contrat.id_client == client.id).all()

            if len(contrats) > 1:
                choix_contrat_str = vue_choix_contrat(contrats)
                choix_contrat = int(choix_contrat_str)
                contrat = session.query(Contrat).filter(Contrat.id == choix_contrat).first()

            elif contrats is None:
                simple_print("Aucun contrat trouvé.")

        if choix_recherche == 2:
            choix_contrat_str = vue_choix_contrat(None)
            choix_contrat = int(choix_contrat_str)
            contrat = session.query(Contrat).filter(Contrat.id == choix_contrat).first()
        
        try:
            modification = vue_modification_contrat(contrat)

            contrat.id_client = verification_type(modification["id_client"])
            contrat.id_collaborateur = verification_type(modification["id_collaborateur"])
            contrat.montant_total = verification_type(modification["montant_total"])
            contrat.reste_a_payer = verification_type(modification["reste_a_payer"])
            contrat.status_contrat = modification["status_contrat"]

            session.commit()
            simple_print(f"Contrat modiffié avec succès")

        except Exception as e:
            session.rollback()
            simple_print(f"Erreur lors de la modification:/n - {e}")
