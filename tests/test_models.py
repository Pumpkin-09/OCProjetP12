from models.models import MyEnum, Collaborateur
from models.models_managment import verification_role
from models.models import EnumPermission as EP


# Tests des permissions

def test_commercial_ne_peut_pas_creer_Collaborateur():
    """Test que l'équipe commerciale ne peut PAS créer des collaborateurs"""
    
    commercial = Collaborateur(role=MyEnum.commercial)
    assert verification_role(EP.creer_collaborateur, commercial.role) == False


def test_support_ne_peut_pas_creer_collaborateur():
    """Test que l'équipe support ne peut PAS créer des collaborateurs"""
    
    support = Collaborateur(role=MyEnum.support)
    assert verification_role(EP.creer_collaborateur, support.role) == False


def test_gestion_peut_creer_collaborateur():
    """Test que l'équipe gestion peut créer des collaborateurs"""
    
    gestion = Collaborateur(role=MyEnum.gestion)
    assert verification_role(EP.creer_collaborateur, gestion.role) == True


def test_commercial_ne_peut_pas_afficher_Collaborateur():
    """Test que l'équipe commerciale ne peut PAS afficher des collaborateurs"""
    
    commercial = Collaborateur(role=MyEnum.commercial)
    assert verification_role(EP.afficher_collaborateurs, commercial.role) == False


def test_support_ne_peut_pas_afficher_collaborateur():
    """Test que l'équipe support ne peut PAS affiocher des collaborateurs"""
    
    support = Collaborateur(role=MyEnum.support)
    assert verification_role(EP.afficher_collaborateurs, support.role) == False


def test_gestion_peut_afficher_collaborateur():
    """Test que l'équipe gestion peut afficher des collaborateurs"""
    
    gestion = Collaborateur(role=MyEnum.gestion)
    assert verification_role(EP.afficher_collaborateurs, gestion.role) == True


def test_commercial_ne_peut_pas_modifier_Collaborateur():
    """Test que l'équipe commerciale ne peut PAS modifier des collaborateurs"""
    
    commercial = Collaborateur(role=MyEnum.commercial)
    assert verification_role(EP.modifier_collaborateur, commercial.role) == False


def test_support_ne_peut_pas_modifier_collaborateur():
    """Test que l'équipe support ne peut PAS modifier des collaborateurs"""
    
    support = Collaborateur(role=MyEnum.support)
    assert verification_role(EP.modifier_collaborateur, support.role) == False


def test_gestion_peut_modifier_collaborateur():
    """Test que l'équipe gestion peut modifier des collaborateurs"""
    
    gestion = Collaborateur(role=MyEnum.gestion)
    assert verification_role(EP.modifier_collaborateur, gestion.role) == True


def test_commercial_ne_peut_pas_supprimer_Collaborateur():
    """Test que l'équipe commerciale ne peut PAS supprimer des collaborateurs"""
    
    commercial = Collaborateur(role=MyEnum.commercial)
    assert verification_role(EP.supprimer_collaborateur, commercial.role) == False


def test_support_ne_peut_pas_supprimer_collaborateur():
    """Test que l'équipe support ne peut PAS supprimer des collaborateurs"""
    
    support = Collaborateur(role=MyEnum.support)
    assert verification_role(EP.supprimer_collaborateur, support.role) == False


def test_gestion_peut_supprimer_collaborateur():
    """Test que l'équipe gestion peut supprimer des collaborateurs"""
    
    gestion = Collaborateur(role=MyEnum.gestion)
    assert verification_role(EP.supprimer_collaborateur, gestion.role) == True
