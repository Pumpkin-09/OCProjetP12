import bcrypt
from database import SessionLocal
from vue.vue_connexion import simple_print


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


def verification_role(role_required, user_role):
    authorization_role = False

    if role_required == user_role:
        authorization_role = True

    else:
        word = f"Accès refuser, votre role est {user_role} et l'operation nécessite le role de {role_required}"
        simple_print(word)
    
    return authorization_role


def user_deconnexion():
    word = "au revoir"
    simple_print(word)
    connexion = False
    SessionLocal.exit()
    return connexion
