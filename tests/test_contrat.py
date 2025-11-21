from tests.conftest import *
from unittest.mock import patch
from datetime import date
from controleur.controleur_contrat import creation_contrat


@patch('controleur.controleur_contrat.verification_role')
@patch('controleur.controleur_contrat.recherche_client')
@patch('controleur.controleur_contrat.vue_creation_contrat')
@patch('controleur.controleur_contrat.simple_print')
def test_creation_contrat_succes(
    mock_print,
    mock_vue_creation,
    mock_recherche_client,
    mock_verif_role,
    fake_collaborateurs,
    client_factory,
    mock_session
):
    # Préparer les données
    collaborateur = fake_collaborateurs[2]  # Collaborateur gestion
    client = client_factory()
    mock_verif_role.return_value = True
    mock_recherche_client.return_value = client
    mock_vue_creation.return_value = {
        "id": 1,
        "id client": client.id,
        "id collaborateur": collaborateur.id,
        "montant total": 1000.0,
        "reste a payer": 1000.0,
        "date creation contrat": date.today(),
        "statut contrat": False
    }


    # Appeler la fonction
    creation_contrat(collaborateur, mock_session)

    # Vérifications
    mock_verif_role.assert_called_once()
    mock_recherche_client.assert_called_once()
    mock_vue_creation.assert_called_once()
    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()
    mock_print.assert_called_with("Contrat créé avec succès")


@patch('controleur.controleur_contrat.verification_role')
@patch('controleur.controleur_contrat.recherche_client')
@patch('controleur.controleur_contrat.vue_creation_contrat')
@patch('controleur.controleur_contrat.simple_print')
def test_creation_contrat_client_non_trouve(
    mock_print,
    mock_vue_creation,
    mock_recherche_client,
    mock_verif_role,
    fake_collaborateurs,
    mock_session
):
    # Préparer les données
    collaborateur = fake_collaborateurs[2]  # Collaborateur gestion
    mock_verif_role.return_value = True
    mock_recherche_client.return_value = None  # Client n'existe pas

    # Appeler la fonction
    creation_contrat(collaborateur, mock_session)

    # Vérifications
    mock_verif_role.assert_called_once()
    mock_recherche_client.assert_called_once()
    mock_print.assert_called_once_with("Création de contrat annulée.")

    mock_vue_creation.assert_not_called()
    mock_session.add.assert_not_called()
    mock_session.commit.assert_not_called()


@patch('controleur.controleur_contrat.verification_role')
@patch('controleur.controleur_contrat.recherche_client')
@patch('controleur.controleur_contrat.vue_creation_contrat')
@patch('controleur.controleur_contrat.simple_print')
def test_creation_contrat_pas_authorisation(
    mock_print,
    mock_vue_creation,
    mock_recherche_client,
    mock_verif_role,
    fake_collaborateurs,
    mock_session
):
    # Préparer les données
    collaborateur = fake_collaborateurs[0]  # Collaborateur commercial
    mock_verif_role.return_value = False  # Pas d'autorisation

    # Appeler la fonction
    creation_contrat(collaborateur, mock_session)

    # Vérifications
    mock_verif_role.assert_called_once()

    mock_recherche_client.assert_not_called()
    mock_print.assert_not_called()
    mock_vue_creation.assert_not_called()
    mock_session.add.assert_not_called()
    mock_session.commit.assert_not_called()
