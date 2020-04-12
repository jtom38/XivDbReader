from XivDbReader.scrape import ParseItems
from XivDbReader.collections import *
import pytest

pytest.html = ''
pytest.url = 'https://na.finalfantasyxiv.com/lodestone/playguide/db/item/2984c426c25/'
pytest.item: Equipment = Weapon()

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
    if pytest.item.name == 'Gliderskin Codex':
        assert True
    else: assert False

def test_glamourOptions(parseItemData):
    if pytest.item.companyCrest == False and \
        pytest.item.glamourChest == True and \
        pytest.item.armorie == False:
        assert True
    else: assert False

def test_itemLevel(parseItemData):
    pi = ParseItems()
    res = pi.getDetails(html=pytest.html)
    if res.itemLevel == 395:
        assert True
    else: assert False

def test_itemAttack(parseItemData):
    if pytest.item.physicalDamage == 0:
        assert True
    else: assert False

def test_magicalAttack(parseItemData):
    if pytest.item.magicDamage ==131:
        assert True
    else: assert False

def test_itemAutoAttack(parseItemData):
    if pytest.item.autoAttack == 99.83:
        assert True
    else: assert False

def test_delay(parseItemData):
    if pytest.item.delay == 3.12:
        assert True
    else: assert False
    
def test_itemJobs(parseItemData):
    if "SCH" in pytest.item.jobs:
        assert True
    else: assert False

def test_jobLevel(parseItemData):
    if pytest.item.level == 72:
        assert True
    else: assert False

def test_attributes(parseItemData):
    if pytest.item.stats.mind == 351 and \
        pytest.item.stats.criticalHit == 309 and \
        pytest.item.stats.vitality == 355 and \
        pytest.item.stats.piety == 216:
        assert True
    else: assert False

## Materia

def test_materiaSlots(parseItemData):
    if pytest.item.materia.slots == 2:
        assert True
    else: assert False
def test_materiaMelderClass(parseItemData):
    if pytest.item.materia.job == "Alchemist":
        assert True
    else: assert False

def test_materiaMelderLevel(parseItemData):
    if pytest.item.materia.melderLevel == 72:
        assert True
    else: assert False

def test_materiaAdvanced(parseItemData):
    if pytest.item.materia.advancedMelding == True:
        assert True        
    else: assert False

## Repair

def test_repairClass(parseItemData):
    if pytest.item.repair.job == "Alchemist":
        assert True
    else: assert False

def test_repairClassLevel(parseItemData):
    if pytest.item.repair.level == 62:
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
    if pytest.item.dyeable == True:
        assert True
    else: assert False

def test_desynth(parseItemData):
    if pytest.item.desynth == 395.0:
        assert True
    else: assert False

## Vendors

def test_sellsFor(parseItemData):
    if pytest.item.sellPrice == 638:
        assert True
    else: assert False

def test_buyFor(parseItemData):
    if pytest.item.buyPrice == 40878:
        assert True
    else: assert False

def test_vendors(parseItemData):
    if len(pytest.item.buyFrom) == 2:
        assert True
    else: assert False

def test_vendorsNames(parseItemData):
    if pytest.item.buyFrom[0]['name'] == 'Pixie Hoarder' and \
        pytest.item.buyFrom[1]['name'] == 'Ys Gyuf':
        assert True
    else: assert False

def test_vendorLocations(parseItemData):
    if pytest.item.buyFrom[0]['loc'] == 'Il Mheg (X:14.8 Y:32.2)' and \
        pytest.item.buyFrom[1]['loc'] == 'Il Mheg (X:19.7 Y:4.1)':
        assert True
    else: assert False

## Instances/Fights

def test_dropsFrom(parseItemData):
    if pytest.item.relatedDuties.__len__() == 0:
        assert True
    else: assert False

def test_dropsFromLevel(parseItemData):
    if pytest.item.relatedDuties.__len__() == 0:
        assert True
    else: assert False

def test_dropsFromRequiredItemLevel(parseItemData):
    if pytest.item.relatedDuties.__len__ == 0:
        assert True
    else: assert False

def test_RequiredItemName(parseItemData):
    if pytest.item.requiredItems.__len__() == 0:
        assert True
    else: assert False

def test_RequiredItemCount(parseItemData):
    if pytest.item.requiredItems.__len__() == 0:
        assert True 
    else: assert False

def test_RequiredItemNpc(parseItemData):
    if pytest.item.requiredItems.__len__() == 0:
        assert True 
    else: assert False

def test_RequiredItemNpcLocation(parseItemData):
    if pytest.item.requiredItems.__len__() == 0:
        assert True 
    else: assert False
    
def test_isUniqueUntradable(parseItemData):
    if pytest.item.untradable == False and \
        pytest.item.unique == False:
        assert True
    else: assert False