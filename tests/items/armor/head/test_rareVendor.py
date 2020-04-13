from XivDbReader.scrape import ParseItems
from XivDbReader.collections import *
import pytest

pytest.html = ''
pytest.url = 'https://na.finalfantasyxiv.com/lodestone/playguide/db/item/89ad15e24d2/'
pytest.item: Equipment = Armor()

@pytest.fixture
def getHtmlSource():
    if pytest.html == '':
        pi = ParseItems()
        pytest.html = pi.GetHtmlSource(pytest.url)

@pytest.fixture
def parseItemData(getHtmlSource):
    w = Armor()
    if pytest.item.defense == 0:
        # value is defaulted
        pi = ParseItems()
        pytest.item = pi.getDetails(html=pytest.html)

def test_itemName(parseItemData):
    if pytest.item.name == 'Augmented Ironworks Visor of Maiming':
        assert True
    else: assert False

def test_glamourOptions(parseItemData):
    if pytest.item.companyCrest == False and \
        pytest.item.glamourChest == True and \
        pytest.item.armorie == False:
        assert True
    else: assert False

def test_itemLevel(parseItemData):
    res = pytest.item.itemLevel
    if res == 130:
        assert True
    else: assert False

def test_magicDefense(parseItemData):
    res = pytest.item.magicDefense
    if res == 68:
        assert True
    else: assert False

def test_defense(parseItemData):
    res = pytest.item.defense
    if res == 85:
        assert True
    else: assert False

def test_itemAutoAttack(parseItemData):
    try:
        if pytest.item.autoAttack == 0:
            assert False
    except:
        # property does not exist for Armor class
        assert True

def test_delay(parseItemData):
    try:
        if pytest.item.delay == 2.00:
            assert False
    except:
        assert True

def test_jobCount(parseItemData):
    if pytest.item.jobs.__len__() == 2:
        assert True
    else: assert False

def test_itemJobs(parseItemData):
    if "DRG" in pytest.item.jobs:
        assert True
    else: assert False

def test_jobLevel(parseItemData):
    if pytest.item.level == 50:
        assert True
    else: assert False

def test_attributes(parseItemData):
    if pytest.item.stats.strength == 31 and \
        pytest.item.stats.vitality == 36 and \
        pytest.item.stats.dexterity == 0 and \
        pytest.item.stats.intelligence == 0 and \
        pytest.item.stats.mind == 0 and \
        pytest.item.stats.determination == 0 and \
        pytest.item.stats.skillSpeed == 0 and \
        pytest.item.stats.spellSpeed == 0 and \
        pytest.item.stats.criticalHit == 20 and \
        pytest.item.stats.directHitRate == 29 and \
        pytest.item.stats.tenacity == 0 and \
        pytest.item.stats.piety == 0:
        assert True
    else: assert False

## Materia

def test_materiaSlots(parseItemData):
    if pytest.item.materia.slots == 0:
        assert True
    else: assert False

def test_materiaMelderClass(parseItemData):
    if pytest.item.materia.melderJob == None:
        assert True
    else: assert False

def test_materiaMelderLevel(parseItemData):
    if pytest.item.materia.melderLevel == 0:
        assert True
    else: assert False
    

def test_materiaAdvanced(parseItemData):
    if pytest.item.materia.advancedMelding == True:
        assert True 
    else: assert False       

## Repair

def test_repairClass(parseItemData):
    if pytest.item.repair.job == "Armorer":
        assert True
    else: assert False

def test_repairClassLevel(parseItemData):
    if pytest.item.repair.level == 40:
        assert True
    else: assert False

def test_repairMaterial(parseItemData):
    if pytest.item.repair.material == 'Grade 5 Dark Matter':
        assert True
    else: assert False

def test_extractable(parseItemData):
    if pytest.item.extractable == True:
        assert True
    else: assert False
def test_projectable(parseItemData):
    if pytest.item.projectable == True:
        assert True
    else: assert False

def test_dyeable(parseItemData):
    if pytest.item.dyeable == True:
        assert True
    else: assert False

def test_desynth(parseItemData):
    if pytest.item.desynth == 130.0:
        assert True
    else: assert False

## Vendors

def test_sellsFor(parseItemData):
    if pytest.item.vendors.sell == 336:
        assert True
    else: assert False

def test_buyFor(parseItemData):
    if pytest.item.vendors.buy == 0:
        assert True
    else: assert False

def test_vendors(parseItemData):
    if len(pytest.item.vendors.buyFrom) == 0:
        assert True
    else: assert False

def test_vendorsNames(parseItemData):
    if pytest.item.vendors.buyFrom.__len__() == 0:
        assert True
    else:
        assert False

def test_vendorLocations(parseItemData):
    if pytest.item.vendors.buyFrom.__len__() == 0:
        assert True
    else: assert False

## Instances/Fights

def test_dropsFrom(parseItemData):
    if pytest.item.relatedDuties.__len__() == 0:
        assert True

def test_dropsFromLevel(parseItemData):
    if pytest.item.relatedDuties.__len__() == 0:
        assert True
    else:
        assert False
    
def test_dropsFromRequiredItemLevel(parseItemData):
    if pytest.item.relatedDuties.__len__() == 0:
        assert True
    else:
        assert False

def test_RequiredItemName(parseItemData):
    res = pytest.item.requiredItems
    
    if res[0].items[0].name == 'Carbontwine' and \
        res[0].items[1].name == 'Ironworks Visor of Maiming':
        assert True
    else: 
        assert False

def test_RequiredItemCount(parseItemData):
    if pytest.item.requiredItems[0].items[0].amount == 1 and \
        pytest.item.requiredItems[0].items[1].amount == 1:
        assert True 
    else:
        assert False

def test_RequiredItemNpc(parseItemData):
    if pytest.item.requiredItems[0].npc == 'Drake':
        assert True 
    else:
        assert False

def test_RequiredItemNpcLocation(parseItemData):
    if pytest.item.requiredItems[0].location == 'North Shroud (X:30.3 Y:20.1)':
        assert True 
    else:
        assert False

def test_isUniqueUntradable(parseItemData):
    if pytest.item.untradable == True and \
        pytest.item.unique == False:
        assert True