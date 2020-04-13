
from XivDbReader.scrape import ParseItems
from XivDbReader.collections import *
import pytest

pytest.html = ''
pytest.url = 'https://na.finalfantasyxiv.com/lodestone/playguide/db/item/e6e352371d7/'
pytest.item: Weapon = Weapon()

@pytest.fixture
def getHtmlSource():
    if pytest.html == '':
        pi = ParseItems()
        pytest.html = pi.GetHtmlSource(pytest.url)

@pytest.fixture
def parseItemData(getHtmlSource):
    w = Weapon()
    if pytest.item.delay == 0.0:
        # value is defaulted
        pi = ParseItems()
        pytest.item = pi.getDetails(html=pytest.html)

def test_itemName(parseItemData):
    if pytest.item.name == 'Lakeland Grimoire':
        assert True
    else: assert False

def test_glamourOptions(parseItemData):
    if pytest.item.companyCrest == False and \
        pytest.item.glamourChest == True and \
        pytest.item.armorie == False:
        assert True
    else: assert False

def test_itemLevel(parseItemData):
    if pytest.item.itemLevel == 390:
        assert True
    else: assert False

def test_physicalDamage(parseItemData):
    if pytest.item.physicalDamage == 0:
        assert True
    else: assert False

def test_itemAttack(parseItemData):
    res = pytest.item.magicDamage
    if res == 144:
        assert True
    else: assert False

def test_itemAutoAttack(parseItemData):
    res = pytest.item.autoAttack
    if res == 111.28:
        assert True
    else: assert False

def test_delay(parseItemData):
    res = pytest.item.delay
    if res == 3.12:
        assert True
    else: assert False

def test_itemJobs(parseItemData):
    res = pytest.item.jobs
    if "SMN" in res:
        assert True
    else: assert False

def test_jobLevel(parseItemData):
    if pytest.item.level == 71:
        assert True
    else: assert False

def test_attributes(parseItemData):
    if pytest.item.stats.spellSpeed == 337 and \
        pytest.item.stats.determination == 236 and \
        pytest.item.stats.intelligence == 381 and \
        pytest.item.stats.vitality == 384:
        assert True
    else: assert False

## Materia

def test_materiaSlots(parseItemData):
    if pytest.item.materia.slots == 2:
        assert True
    else: assert False

def test_materiaMelderClass(parseItemData):
    if pytest.item.materia.melderJob == "Alchemist":
        assert True
    else: assert False

def test_materiaMelderLevel(parseItemData):
    if pytest.item.materia.melderLevel == 71:
        assert True
    else: assert False

def test_materiaAdvanced(parseItemData):
    if pytest.item.materia.advancedMelding == False:
        assert True
    else: assert False

## Repair

def test_repairClass(parseItemData):
    if pytest.item.repair.job == "Alchemist":
        assert True
    else: assert False

def test_repairClassLevel(parseItemData):
    if pytest.item.repair.level == 61:
        assert True
    else: assert False

def test_repairMaterial(parseItemData):
    if pytest.item.repair.material == 'Grade 7 Dark Matter':
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
    if pytest.item.dyeable == False:
        assert True
    else: assert False

def test_desynth(parseItemData):
    if pytest.item.desynth == 390.0:
        assert True
    else: assert False

def test_sellsFor(parseItemData):
    if pytest.item.vendors.sell == 1062:
        assert True
    else: assert False

def test_buyFor(parseItemData):
    if pytest.item.vendors.buy == 0:
        assert True
    else: assert False

def test_vendors(parseItemData):
    if len(pytest.item.vendors.buyFrom) == 0:
        assert True
    else:
        assert False

def test_vendorsNames(parseItemData):
    res = pytest.item.vendors.buyFrom
    if res == 0:
        assert True

def test_vendorLocations(parseItemData):
    res = pytest.item.vendors.buyFrom
    if res.__len__() == 0:
        assert True

def test_dropsFrom(parseItemData):
    res = pytest.item.relatedDuties
    if res[0].name == 'Holminster Switch':
        assert True
    else: 
        assert False

def test_dropsFromLevel(parseItemData):
    res = pytest.item.relatedDuties 
    if res[0].level == 71:
        assert True
    else: 
        assert False
    
def test_dropsFromRequiredItemLevel(parseItemData):
    res = pytest.item.relatedDuties
    if res[0].itemLevel == 370:
        assert True

def test_RequiredItemName(parseItemData):
    res = pytest.item.requiredItems
    if res.__len__() == 0:
        assert True
    else: 
        assert False

def test_RequiredItemCount(parseItemData):
    if pytest.item.requiredItems.__len__() == 0:
        assert True 
    else: 
        assert False

def test_RequiredItemNpc(parseItemData):
    if pytest.item.requiredItems.__len__() == 0:
        assert True 
    else: 
        assert False

def test_RequiredItemNpcLocation(parseItemData):
    if pytest.item.requiredItems.__len__() == 0:
        assert True 
    else: 
        assert False

def test_isUniqueUntradable(parseItemData):
    if pytest.item.untradable == True and \
        pytest.item.unique == True:
        assert True
    else: 
        assert False
