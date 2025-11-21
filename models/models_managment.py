import bcrypt
from database import SessionLocal
from models.models_permission import PERMISSIONS
from models.models import Collaborateur
from vue.vue import simple_print, input_user_identifient


def hashing_password(password):
    bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash.decode("utf-8")


def verification_password(hash_password, user_password):
    bytes = hash_password.encode("utf-8")
    user_bytes = user_password.encode('utf-8')
    result = bcrypt.checkpw(user_bytes, bytes)
    return result


def verification_role(action, user_role):
    if action not in PERMISSIONS:
        print(f"Erreur: Action '{action}' inconnue")
        return False

    if user_role in PERMISSIONS[action]:
        return True

    else:
        simple_print(f"Accès refusé, votre rôle de {user_role} ne permet pas l'opération.")
        return False


def user_connexion(session):
    identifient_user = input_user_identifient()
    user_email = identifient_user[0]
    user_password = identifient_user[1]
    collaborateur = session.query(Collaborateur).filter(Collaborateur.email == user_email).first()
    if collaborateur and verification_password(collaborateur.password, user_password):
        simple_print(f"Connexion réussi.\nBonjour {collaborateur.nom}")
        return collaborateur
    else:
        simple_print("Identifiants incorrects")
        return False


def user_deconnexion():
    simple_print("Au revoir")
    connexion = False
    SessionLocal.exit()
    return connexion
