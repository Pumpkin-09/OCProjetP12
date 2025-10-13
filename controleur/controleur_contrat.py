from models.models import Contrat
from models.models_managment import verification_role
from models.models import EnumPermission as EP
from sqlalchemy import func
from controleur_client import recherche_client
from vue.vue import simple_print, vue_affichage_informations
from vue.vue_contrat import vue_recherche_contrat, vue_creation_contrat, vue_modification_contrat, vue_choix_contrat


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
                montant_total = infos_contrat["montant"],
                reste_a_payer = infos_contrat["reste_a_payer"]
            )
            session.add(nouveau_contrat)
            session.commit()
            simple_print(f"Contrat créé avec succès")

        except Exception as e:
            session.rollback()
            simple_print(f"Erreur lors de la création:/n - {e}")


def afficher_mes_contrats(collaborateur, session):
    action = EP.afficher_contrat
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        contrats = session.query(Contrat).filter(Contrat.id_collaborateur == collaborateur.id).all()
        if len(contrats) > 0:
            vue_affichage_informations(contrats)
        else:
            simple_print("Aucun contrat")


def afficher_tous_contrats(collaborateur, session):
    action = EP.afficher_contrat
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        contrats = session.query(Contrat).all()
        if len(contrats) > 0:
            vue_affichage_informations(contrats)
        else:
            simple_print("Aucun contrat")


def filtre_afficher_contrats(collaborateur, session):
    action = EP.afficher_contrat
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        choix_contrat = vue_filtre_contrat()
        if choix_contrat:
            contrats = session.query(Contrat).filter(Contrat.reste_a_payer > 0).all()
        else:
            contrats = session.query(Contrat).filter(Contrat.status_contrat == False).all()
        if len(contrats) > 0:
            vue_affichage_informations(contrats)
        else:
            simple_print("Aucun contrat")


def modification_contrat(collaborateur, session):
    action = EP.modifier_contrat
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        contrat = vue_recherche_contrat()
        if contrat is None:
            client = recherche_client()
            if client is None:
                simple_print("Ce client n'existe pas.")
                return
            contrats = session.query(Contrat).filter(Contrat.id_client == client.id).all()
            if len(contrats) > 1:
                choix_contrat = vue_choix_contrat(contrats)
                contrat = contrats[choix_contrat-1]
            elif len(contrats) == 0:
                simple_print("Contrat non trouvé.")

        try:
            modification = vue_modification_contrat(contrat)

            contrat.id_client = modification["id"]
            contrat.id_collaborateur = modification["collaborateur"]
            contrat.montant_total = modification["montant"]
            contrat.reste_a_payer = modification["reste_a_payer"]
            contrat.status_contrat = modification["status_contrat "]

            session.commit()
            simple_print(f"Contrat modiffié avec succès")

        except Exception as e:
            session.rollback()
            simple_print(f"Erreur lors de la modification:/n - {e}")
