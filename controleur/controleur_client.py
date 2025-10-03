from models.models import Client
from models.user_managment import verification_role
from vue.vue import simple_print
from sqlalchemy import func
from vue.vue_client import vue_recherche_client, vue_creation_client, vue_affichage_client, vue_modification_client


def recherche_client(session):
    client_chercher = vue_recherche_client()
    client = session.query(Client).filter(func.lower(Client.nom_complet) == client_chercher.lower()).first()
    return client


def creation_client(collaborateur, session):
    action = "creer client"
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
            simple_print(f"Erreur lors de la création:/n - {e}")


def afficher_mes_clients(collaborateur, session):
    action = "affichage client"
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        clients = session.query(Client).filter(Client.id_collaborateur == collaborateur.id).all()
        vue_affichage_client(clients)


def afficher_tous_clients(collaborateur, session):
    action = "affichage client"
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        clients = session.query(Client).all()
        vue_affichage_client(clients)


def modification_client(collaborateur, session):
    action = "modifier client"
    user_role = collaborateur.role
    authorisation = verification_role(action, user_role)
    if authorisation:
        client = recherche_client()
        if client is None:
            simple_print("Ce client n'existe pas.")
            return

        try:
            modification = vue_modification_client(client)

            Client(
                nom_complet = modification["nom"],
                email = modification["email"],
                telephone = modification["telephone"],
                nom_entreprise = modification["entreprise"],
                id_collaborateur = modification["collaborateur"]
            )
            session.commit()
            simple_print(f"Client '{modification['nom']}' modiffié avec succès")

        except Exception as e:
            session.rollback()
            simple_print(f"Erreur lors de la modification:/n - {e}")
