from database import Base
from sqlalchemy import Column, Integer, String, Date, DateTime, Float, Boolean, ForeignKey, Enum
from sqlalchemy.sql import func
import enum


class EnumPermission(enum.Enum):
    creer_client = "creer client"
    afficher_client = "afficher clients"
    modifier_client = "modifier client"
    
    creer_contrat = "creer contrat"
    afficher_contrat = "afficher contrats"
    modifier_contrat = "modifier contrat"
    
    creer_evenement = "creer evenement"
    afficher_evenement = "afficher evenements"
    modifier_evenement = "modifier evenement"
    
    creer_collaborateur = "creer collaborateur"
    afficher_collaborateurs = "afficher collaborateurs"
    modifier_collaborateur = "modifier collaborateur"
    supprimer_collaborateur = "supprimer collaborateur"


class MyEnum(enum.Enum):
    gestion = "equipe gestion"
    commercial = "equipe commercial"
    support = "equipe support"


class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nom_complet = Column(String(150), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    telephone = Column(String(14), nullable=False)
    nom_entreprise = Column(String(250), nullable=False)
    date_creation = Column(Date, default=func.curdate())
    date_mise_a_jour = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())
    id_collaborateur = Column(Integer, ForeignKey("collaborateur.id"), nullable=False)

    def __str__(self):
        return f"""
        Informations du client:
        ID: {self.id}
        Nom: {self.nom_complet}
        Email: {self.email}
        Telephone: {self.telephone}
        Nom de l'entreprise: {self.nom_entreprise}
        Date de création: {self.date_creation}
        Date de mise a jour: {self.date_mise_a_jour}
        ID du collaborateur: {self.id_collaborateur}
        """

class Collaborateur(Base):
    __tablename__ = "collaborateur"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nom = Column(String(150), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    role = Column(Enum(MyEnum), nullable=False)

    def __str__(self):
        return f"""
        Informations du collaborateur:
        ID: {self.id}
        Nom: {self.nom}
        Email: {self.email}
        Role: {self.role}
        """


class Contrat(Base):
    __tablename__ = "contrat"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    id_client = Column(Integer, ForeignKey("client.id"), nullable=False)
    id_collaborateur = Column(Integer, ForeignKey("collaborateur.id"), nullable=False)
    montant_total = Column(Float, nullable=False)
    reste_a_payer = Column(Float, nullable=False)
    date_creation_contrat = Column(Date, default=func.curdate())
    status_contrat = Column(Boolean, default=False)

    def __str__(self):
        return f"""
        Information sur le contrat:
        ID: {self.id}
        ID client: {self.id_client}
        ID collaborateur: {self.id_collaborateur}
        Montant total: {self.montant_total}
        Reste a payer: {self.reste_a_payer}
        Date de création: {self.date_creation_contrat}
        Status du contrat: {self.status_contrat}
        """


class Evenement(Base):
    __tablename__ = "evenement"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name_event = Column(String(150), nullable=False)
    id_client = Column(Integer, ForeignKey("client.id"), nullable=False)
    id_collaborateur = Column(Integer, ForeignKey("collaborateur.id"), nullable=False)
    event_date_start = Column(Date, nullable=False)
    event_date_stop = Column(Date, nullable=False)
    id_support_contrat = Column(Integer, ForeignKey("collaborateur.id"), nullable=True)
    location = Column(String(300), nullable=True)
    attente = Column(Integer, nullable=True)
    note = Column(String(500), nullable=True)

    def __str__(self):
        return f"""
        Informations de l'évenement:
        ID: {self.id}
        ID client: {self.id_client}
        ID collaborateur: {self.id_collaborateur}
        ID collaborateur equipe support: {self.id_support_contrat}
        Date de début: {self.event_date_start}
        Date de fin: {self.event_date_stop}
        Location: {self.location}
        Nombre attendu: {self.attente}
        Note: {self.note}
        """
