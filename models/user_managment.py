import bcrypt
from database import SessionLocal
from vue.vue import simple_print
from models.models_permission import PERMISSIONS


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
    authorization_role = False

    if action not in PERMISSIONS:
        print(f"Erreur: Action '{action}' inconnue")
        return False

    if user_role in PERMISSIONS[action]:
        return True

    else:
        simple_print(f"Accès refuser, votre role de {user_role} ne permet pas l'operation.")
        return False


def user_deconnexion():
    simple_print("au revoir")
    connexion = False
    SessionLocal.exit()
    return connexion
