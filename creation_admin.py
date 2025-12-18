from database import SessionLocal
from models.models import Collaborateur
from models.models_managment import hashing_password
from vue.vue import simple_print


session = SessionLocal()

def creation_collaborateur_admin(session):
    ADMIN_DATA = {
        "nom": "Admin",
        "email": "admin@epicevents.com",
        "password": "password123",
        "role": "equipe gestion"
}
    email_existe = session.query(Collaborateur).filter(Collaborateur.email == ADMIN_DATA["email"]).first()
    if email_existe:
        simple_print("Email déjà utilisé")
        return
    try:
        nouveau_collaborateur = Collaborateur(
            nom = ADMIN_DATA["nom"],
            email = ADMIN_DATA["email"],
            password = hashing_password(ADMIN_DATA["password"]),
            role = ADMIN_DATA["role"]
        )
        session.add(nouveau_collaborateur)
        session.commit()
        simple_print(f"Collaborateur '{ADMIN_DATA['nom']}' créé avec succès")
    except Exception as e:
        session.rollback()
        simple_print(f"Erreur lors de la création:/n - {e}")


if __name__ == "__main__":
    creation_collaborateur_admin(session)
