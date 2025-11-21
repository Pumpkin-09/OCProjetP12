from tests.conftest import *
from unittest.mock import patch
from controleur.controleur_client import creation_client


@patch('controleur.controleur_client.simple_print')
@patch('controleur.controleur_client.vue_creation_client')
@patch('controleur.controleur_client.verification_role')
def test_creation_client_succes(
    mock_verif_role,
    mock_vue_creation,
    mock_print,
    fake_collaborateurs,
    mock_session
):
    # Préparer les données
    collaborateur = fake_collaborateurs[0]  # Collaborateur commercial
    mock_verif_role.return_value = True
    mock_vue_creation.return_value = {
        "nom": "Client Test",
        "email": "client@exemple.com",
        "telephone": "0123456789",
        "entreprise": "Entreprise Test"
    }
    mock_session.query().filter().first.return_value = None  # Email n'existe pas

    # Appeler la fonction
    creation_client(collaborateur, mock_session)

    # Vérifications
    mock_verif_role.assert_called_once()
    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()
    mock_print.assert_called_with("Client 'Client Test' créé avec succès")


@patch('controleur.controleur_client.simple_print')
@patch('controleur.controleur_client.vue_creation_client')
@patch('controleur.controleur_client.verification_role')
def test_creation_client_email_existe(
    mock_verif_role,
    mock_vue_creation,
    mock_print,
    fake_collaborateurs,
    mock_session,
    client_factory
):
    # Préparer les données
    client = client_factory(email="client@exemple.com")
    collaborateur = fake_collaborateurs[0]  # Collaborateur commercial
    mock_verif_role.return_value = True
    mock_vue_creation.return_value = {
        "nom": "Client email existe",
        "email": "client@exemple.com",
        "telephone": "0123456789",
        "entreprise": "Entreprise Test"
    }
    mock_session.query().filter().first.return_value = client  # Email existe

    # Appeler la fonction
    creation_client(collaborateur, mock_session)

    # Vérifications
    mock_verif_role.assert_called_once()
    mock_print.assert_called_with("Email déjà utilisé")

    mock_session.add.assert_not_called()
    mock_session.commit.assert_not_called()


@patch('controleur.controleur_client.simple_print')
@patch('controleur.controleur_client.vue_creation_client')
@patch('controleur.controleur_client.verification_role')
def test_creation_client_pas_authorisation(
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
    creation_client(collaborateur, mock_session)

    # Vérifications
    mock_verif_role.assert_called_once()

    mock_session.add.assert_not_called()
    mock_session.commit.assert_not_called()
    mock_print.assert_not_called()
    mock_vue_creation.assert_not_called()
