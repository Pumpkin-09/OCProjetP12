from database import Base
from sqlalchemy import Column, Integer, String, Date, DateTime, Float, Boolean, ForeignKey, Enum

'''from sqlalchemy.orm import relationship'''

from sqlalchemy.sql import func
import enum


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


class Collaborateur(Base):
    __tablename__ = "collaborateur"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nom = Column(String(150), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    role = Column(Enum(MyEnum), nullable=False)


class Contrat(Base):
    __tablename__ = "contrat"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    id_client = Column(Integer, ForeignKey("client.id"), nullable=False)
    id_collaborateur = Column(Integer, ForeignKey("collaborateur.id"), nullable=False)
    montant_total = Column(Float, nullable=False)
    reste_a_payer = Column(Float, nullable=False, nullable=True)
    date_creation_contrat = Column(Date, default=func.curdate())
    status_contrat = Column(Boolean, default=False)


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
