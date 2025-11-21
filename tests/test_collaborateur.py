from tests.conftest import *
from unittest.mock import patch
from controleur.controleur_collaborateur import creation_collaborateur
from models.models import MyEnum


@patch('controleur.controleur_collaborateur.hashing_password')
@patch('controleur.controleur_collaborateur.simple_print')
@patch('controleur.controleur_collaborateur.vue_creation_collaborateur')
@patch('controleur.controleur_collaborateur.verification_role')
def test_creation_collaborateur_succes(
    mock_verif_role,
    mock_vue_creation,
    mock_print,
    mock_hashing_password,
    fake_collaborateurs,
    mock_session
):
    # Préparer les données
    collaborateur = fake_collaborateurs[2]  # Collaborateur gestion
    mock_verif_role.return_value = True
    mock_vue_creation.return_value = {
        "nom": "Collaborateur Test",
        "email": "collaborateur@exemple.com",
        "password": "1234",
        "role": MyEnum.commercial.value
    }
    mock_session.query().filter().first.return_value = None  # Email n'existe pas

    # Appeler la fonction
    creation_collaborateur(collaborateur, mock_session)

    # Vérifications
    mock_verif_role.assert_called_once()
    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()
    mock_hashing_password.assert_called_once_with("1234")
    mock_print.assert_called_with("Collaborateur 'Collaborateur Test' créé avec succès")


@patch('controleur.controleur_collaborateur.simple_print')
@patch('controleur.controleur_collaborateur.vue_creation_collaborateur')
@patch('controleur.controleur_collaborateur.verification_role')
def test_creation_collaborateur_email_existe(
    mock_verif_role,
    mock_vue_creation,
    mock_print,
    mock_session,
    collaborateur_factory
):
    # Préparer les données
    collaborateur = collaborateur_factory(email="email.existe@exemple.com")

    mock_verif_role.return_value = True
    mock_vue_creation.return_value = {
        "id": 5,
        "nom": "Collaborateur Test",
        "email": "email.existe@exemple.com",
        "password": "1234",
        "role": MyEnum.commercial.value
    }
    mock_session.query().filter().first.return_value = collaborateur  # Email existe

    # Appeler la fonction
    creation_collaborateur(collaborateur, mock_session)

    # Vérifications
    mock_verif_role.assert_called_once()
    mock_print.assert_called_with("Email déjà utilisé")

    mock_session.add.assert_not_called()
    mock_session.commit.assert_not_called()


@patch('controleur.controleur_collaborateur.simple_print')
@patch('controleur.controleur_collaborateur.vue_creation_collaborateur')
@patch('controleur.controleur_collaborateur.verification_role')
def test_creation_collaborateur_pas_authorisation(
    mock_verif_role,
    mock_vue_creation,
    mock_print,
    fake_collaborateurs,
    mock_session
):
    # Préparer les données
    collaborateur = fake_collaborateurs[1]  # Collaborateur support
    mock_verif_role.return_value = False

    # Appeler la fonction
    creation_collaborateur(collaborateur, mock_session)

    # Vérifications
    mock_verif_role.assert_called_once()

    mock_session.add.assert_not_called()
    mock_session.commit.assert_not_called()
    mock_print.assert_not_called()
    mock_vue_creation.assert_not_called()
