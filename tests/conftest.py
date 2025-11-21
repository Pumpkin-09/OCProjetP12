import pytest
from unittest.mock import MagicMock
from datetime import date, timedelta
from models.models import MyEnum


# Fixtures et mocks pour les tests

@pytest.fixture
def mock_session():
    """Session DB mockée"""
    session = MagicMock()
    return session


@pytest.fixture
def client_factory():
    """Factory pour créer des clients personnalisés"""
    def _create_client(
        id=1,
        nom_complet="Client Test",
        email="client@exemple.com",
        telephone="0123456789",
        nom_entreprise="Entreprise Test",
        date_creation=None,
        date_mise_a_jour=None,
        id_collaborateur=1
    ):
        client = MagicMock()
        client.id = id
        client.nom_complet = nom_complet
        client.email = email
        client.telephone = telephone
        client.nom_entreprise = nom_entreprise
        client.date_creation = date_creation or date.today()
        client.date_mise_a_jour = date_mise_a_jour or date.today() + timedelta(days=1)
        client.id_collaborateur = id_collaborateur
        return client

    return _create_client


@pytest.fixture
def collaborateur_factory():
    """Factory pour créer des collaborateurs personnalisés"""
    def _create_collaborateur(
        id=1,
        nom="collaborateur Test",
        email="collaborateur@exemple.com",
        password="1234",
        role=MyEnum.gestion.value
    ):
        collaborateur = MagicMock()
        collaborateur.id = id
        collaborateur.nom = nom
        collaborateur.email = email
        collaborateur.password = password
        collaborateur.role = role
        return collaborateur

    return _create_collaborateur


@pytest.fixture
def fake_collaborateurs():
    """Liste de collaborateurs factices"""
    collab1 = MagicMock()
    collab1.id = 1
    collab1.nom = "collaborateur 1"
    collab1.email = "collab1@exemple.com"
    collab1.role = MyEnum.commercial.value

    collab2 = MagicMock()
    collab2.id = 2
    collab2.nom = "collaborateur 2"
    collab2.email = "collab2@exemple.com"
    collab2.role = MyEnum.support.value

    collab3 = MagicMock()
    collab3.id = 3
    collab3.nom = "collaborateur 3"
    collab3.email = "collab3@exemple.com"
    collab3.role = MyEnum.gestion.value

    return [collab1, collab2, collab3]


@pytest.fixture
def contrat_factory():
    """Factory pour créer des contrats personnalisés"""
    def _create_contrat(
        id=1,
        id_client=1,
        id_collaborateur=1,
        montant_total=1000.0,
        reste_a_payer=1000.0,
        date_creation_contrat=None,
        statut_contrat=False
    ):
        contrat = MagicMock()
        contrat.id = id
        contrat.id_client = id_client
        contrat.id_collaborateur = id_collaborateur
        contrat.montant_total = montant_total
        contrat.reste_a_payer = reste_a_payer
        contrat.date_creation_contrat = date_creation_contrat or date.today()
        contrat.status_contrat = statut_contrat
        return contrat
    
    return _create_contrat


@pytest.fixture
def evenement_factory():
    """Factory pour créer des événements personnalisés"""
    def _create_evenement(
        id=1,
        id_client=1,
        id_collaborateur=1,
        id_support_contrat=2,
        event_date_start=None,
        event_date_stop=None,
        location="Lieu Test",
        attente=100,
        note="Note test"
    ):
        evenement = MagicMock()
        evenement.id = id
        evenement.id_client = id_client
        evenement.id_collaborateur = id_collaborateur
        evenement.id_support_contrat = id_support_contrat
        evenement.event_date_start = event_date_start or date.today()
        evenement.event_date_stop = event_date_stop or date.today() + timedelta(days=1)
        evenement.location = location
        evenement.attente = attente
        evenement.note = note
        return evenement
    
    return _create_evenement
