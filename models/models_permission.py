from models.models import MyEnum
from models.models import EnumPermission as EP


PERMISSIONS = {
    EP.creer_client: [MyEnum.commercial],
    EP.afficher_client: [MyEnum.gestion, MyEnum.commercial, MyEnum.support],
    EP.modifier_client: [MyEnum.gestion, MyEnum.commercial],
    
    EP.creer_contrat: [MyEnum.gestion],
    EP.afficher_contrat: [MyEnum.gestion, MyEnum.commercial, MyEnum.support],
    EP.modifier_contrat: [MyEnum.gestion, MyEnum.commercial],
    
    EP.creer_evenement: [MyEnum.commercial],
    EP.afficher_evenement: [MyEnum.gestion, MyEnum.commercial, MyEnum.support],
    EP.modifier_evenement: [MyEnum.gestion, MyEnum.support],
    
    EP.creer_collaborateur: [MyEnum.gestion],
    EP.afficher_collaborateurs: [MyEnum.gestion],
    EP.modifier_collaborateur: [MyEnum.gestion],
    EP.supprimer_collaborateur: [MyEnum.gestion],
}
