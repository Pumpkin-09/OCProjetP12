from models.models import MyEnum


PERMISSIONS = {
    "creer client": [MyEnum.commercial],
    "afficher clients": [MyEnum.gestion, MyEnum.commercial, MyEnum.support],
    "modifier client": [MyEnum.gestion, MyEnum.commercial],
    
    "creer contrat": [MyEnum.gestion, MyEnum.commercial],
    "afficher contrats": [MyEnum.gestion, MyEnum.commercial, MyEnum.support],
    "modifier contrat": [MyEnum.gestion],
    
    "creer evenement": [MyEnum.commercial],
    "afficher evenements": [MyEnum.gestion, MyEnum.commercial, MyEnum.support],
    "modifier evenement": [MyEnum.gestion, MyEnum.support],
    
    "creer collaborateur": [MyEnum.gestion],
    "afficher collaborateurs": [MyEnum.gestion],
    "modifier collaborateur": [MyEnum.gestion],
    "supprimer collaborateur": [MyEnum.gestion],
}
