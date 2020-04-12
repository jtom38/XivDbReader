
from typing import List

class Item():
    def __init__(self):
        self.url: str
        self.pictureUrl: str
        self.name: str
        self.rarity: str
        self.untradable: bool = False
        self.unique: bool = False

        self.itemLevel: int = 0
        self.physicalDamage: int = 0
        self.autoAttack: float = 0.0
        self.delay: float = 0.0

        self.sellPrice: str = ''
        self.buyPrice: str = ''
        self.buyFrom: List = ()
        self.marketProhibited: bool = False

class Equipment(Item):
    def __init__(self):
        self.reset()
        pass

    def reset(self):
        self.slot: str = "main"
        self.itemLevel: int = 0
        self.jobs: List = []
        self.level: int = 0

        self.stats = Stats()
        
        self.companyCrest: bool = False
        self.armorie: bool = False
        self.glamourChest: bool = False
        
        self.dyeable: bool
        self.extractable: bool = False
        self.projectable: bool = False
        self.desynth: float = 0.0

        self.repair = RepairInfo()
        self.materia = Materia()

        self.relatedDuties: List = []
        self.requiredItems: List = []
        pass

class Weapon(Equipment):
    def __init__(self):
        self.physicalDamage: int = 0
        self.magicDamage: int = 0
        self.autoAttack: float = 0.0
        self.delay: float = 0.0
        
class Armor(Equipment):
    def __init__(self):
        self.defense: int = 0
        self.magicDefense: int = 0

class Tool():
    pass


class RepairInfo():
    """
    About: Describes the what is required to repair a item
    """

    def __init__(self):
        self.job: str = ''
        self.level: int = 0
        self.material: str = ''
        pass

class Materia():
    def __init__(self):
        self.slots: int = 0
        self.melderJob: str = ''
        self.melderLevel: int = 0
        self.advancedMelding: bool = True
        pass

class Stats():
    def __init__(self):
        self.strength: int = 0        
        self.vitality: int = 0
        self.dexterity: int = 0
        self.intelligence: int = 0
        self.mind: int = 0

        self.determination: int = 0
        self.skillSpeed: int = 0
        self.spellSpeed: int = 0
        self.criticalHit: int = 0
        self.directHitRate: int = 0
        self.tenacity: int = 0
        self.piety: int = 0
        pass

class RequiredItems():
    def __init__(self):
        pass

    def __setDefaults__(self):
        pass
