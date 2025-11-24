from tests.conftest import *
from unittest.mock import patch
from controleur.controleur_collaborateur import creation_collaborateur, controleur_menu_collaborateur
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


@patch('controleur.controleur_collaborateur.menu_choix_collaborateur')
@patch('controleur.controleur_collaborateur.afficher_tous_collaborateur')
@patch('controleur.controleur_collaborateur.creation_collaborateur')
@patch('controleur.controleur_collaborateur.modification_collaborateur')
@patch('controleur.controleur_collaborateur.suppression_collaborateur')
def test_choix_menu_collaborateur_affichage_collaborateur(
    mock_suppression_collaborateur,
    mock_modification_collaborateur,
    mock_creation_collaborateur,
    mock_affichage_collaborateurs,
    mock_menu_choix
):
    # Préparer les données
    mock_menu_choix.side_effect = [1, None]  # Choix pour afficher les collaborateurs
    # Appeler la fonction
    controleur_menu_collaborateur(None, None)

    # Vérifications
    mock_affichage_collaborateurs.assert_called_once()

    mock_creation_collaborateur.assert_not_called()
    mock_modification_collaborateur.assert_not_called()
    mock_suppression_collaborateur.assert_not_called()


@patch('controleur.controleur_collaborateur.menu_choix_collaborateur')
@patch('controleur.controleur_collaborateur.afficher_tous_collaborateur')
@patch('controleur.controleur_collaborateur.creation_collaborateur')
@patch('controleur.controleur_collaborateur.modification_collaborateur')
@patch('controleur.controleur_collaborateur.suppression_collaborateur')
def test_choix_menu_collaborateur_creation_collaborateur(
    mock_suppression_collaborateur,
    mock_modification_collaborateur,
    mock_creation_collaborateur,
    mock_affichage_collaborateurs,
    mock_menu_choix
):
    # Préparer les données
    mock_menu_choix.side_effect = [2, None]  # Choix pour créer des collaborateurs
    # Appeler la fonction
    controleur_menu_collaborateur(None, None)

    # Vérifications
    mock_creation_collaborateur.assert_called_once()

    mock_affichage_collaborateurs.assert_not_called()
    mock_modification_collaborateur.assert_not_called()
    mock_suppression_collaborateur.assert_not_called()


@patch('controleur.controleur_collaborateur.menu_choix_collaborateur')
@patch('controleur.controleur_collaborateur.afficher_tous_collaborateur')
@patch('controleur.controleur_collaborateur.creation_collaborateur')
@patch('controleur.controleur_collaborateur.modification_collaborateur')
@patch('controleur.controleur_collaborateur.suppression_collaborateur')
def test_choix_menu_collaborateur_modification_collaborateur(
    mock_suppression_collaborateur,
    mock_modification_collaborateur,
    mock_creation_collaborateur,
    mock_affichage_collaborateurs,
    mock_menu_choix
):
    # Préparer les données
    mock_menu_choix.side_effect = [3, None]  # Choix pour modifier les collaborateurs
    # Appeler la fonction
    controleur_menu_collaborateur(None, None)

    # Vérifications
    mock_modification_collaborateur.assert_called_once()

    mock_affichage_collaborateurs.assert_not_called()
    mock_creation_collaborateur.assert_not_called()
    mock_suppression_collaborateur.assert_not_called()

@patch('controleur.controleur_collaborateur.menu_choix_collaborateur')
@patch('controleur.controleur_collaborateur.afficher_tous_collaborateur')
@patch('controleur.controleur_collaborateur.creation_collaborateur')
@patch('controleur.controleur_collaborateur.modification_collaborateur')
@patch('controleur.controleur_collaborateur.suppression_collaborateur')
def test_choix_menu_collaborateur_suppression_collaborateur(
    mock_suppression_collaborateur,
    mock_modification_collaborateur,
    mock_creation_collaborateur,
    mock_affichage_collaborateurs,
    mock_menu_choix
):
    # Préparer les données
    mock_menu_choix.side_effect = [4, None]  # Choix pour supprimer les collaborateurs
    # Appeler la fonction
    controleur_menu_collaborateur(None, None)

    # Vérifications
    mock_suppression_collaborateur.assert_called_once()

    mock_modification_collaborateur.assert_not_called()
    mock_affichage_collaborateurs.assert_not_called()
    mock_creation_collaborateur.assert_not_called()

@patch('controleur.controleur_collaborateur.menu_choix_collaborateur')
@patch('controleur.controleur_collaborateur.afficher_tous_collaborateur')
@patch('controleur.controleur_collaborateur.creation_collaborateur')
@patch('controleur.controleur_collaborateur.modification_collaborateur')
@patch('controleur.controleur_collaborateur.suppression_collaborateur')
def test_choix_menu_collaborateur_quitter(
    mock_suppression_collaborateur,
    mock_modification_collaborateur,
    mock_creation_collaborateur,
    mock_affichage_collaborateurs,
    mock_menu_choix
):
    # Préparer les données
    mock_menu_choix.return_value = None  # Choix pour quitter le menu collaborateurs

    # Appeler la fonction
    controleur_menu_collaborateur(None, None)

    # Vérifications
    mock_affichage_collaborateurs.assert_not_called()
    mock_creation_collaborateur.assert_not_called()
    mock_modification_collaborateur.assert_not_called()
    mock_suppression_collaborateur.assert_not_called()
