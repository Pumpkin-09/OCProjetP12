from models.models import Client
from models.models_managment import verification_role
from vue.vue import simple_print, vue_affichage_informations
from sqlalchemy import func
from vue.vue_client import vue_recherche_client, vue_creation_client, vue_modification_client
from models.models import EnumPermission as EP


def creation_client(collaborateur, session):
    action = EP.creer_client
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        infos_client = vue_creation_client()
        email_existe = session.query(Client).filter(Client.email == infos_client["email"]).first()
        if email_existe:
            simple_print("Email déjà utilisé")
            return
        try:
            nouveau_client = Client(
                nom_complet = infos_client["nom"],
                email = infos_client["email"],
                telephone = infos_client["telephone"],
                nom_entreprise = infos_client["entreprise"],
                id_collaborateur = collaborateur.id
            )
            session.add(nouveau_client)
            session.commit()
            simple_print(f"Client '{infos_client['nom']}' créé avec succès")

        except Exception as e:
            session.rollback()
            simple_print(f"Erreur lors de la création:\n - {e}")


def afficher_mes_clients(collaborateur, session):
    action = EP.afficher_client
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        clients = session.query(Client).filter(Client.id_collaborateur == collaborateur.id).all()
        if len(clients) > 0:
            vue_affichage_informations(clients)
        else:
            simple_print("Aucun clients.")


def afficher_tous_clients(collaborateur, session):
    action = EP.afficher_client
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        clients = session.query(Client).all()
        if len(clients) > 0:
            vue_affichage_informations(clients)
        else:
            simple_print("Aucun clients.")


def recherche_client(session):
    client_chercher = vue_recherche_client()
    client = session.query(Client).filter(func.lower(Client.nom_complet) == client_chercher.lower()).first()
    if client is None:
        simple_print("Ce client n'existe pas.")
        return None
    else:
        return client


def modification_client(collaborateur, session):
    action = EP.modifier_client
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        client = recherche_client(session)

        try:
            modification = vue_modification_client(client)

            client.nom_complet = modification["nom"]
            client.email = modification["email"]
            client.telephone = modification["telephone"]
            client.nom_entreprise = modification["entreprise"]
            client.id_collaborateur = modification["collaborateur"]

            session.commit()
            simple_print(f"Client '{modification['nom']}' modiffié avec succès")

        except Exception as e:
            session.rollback()
            simple_print(f"Erreur lors de la modification:\n - {e}")
