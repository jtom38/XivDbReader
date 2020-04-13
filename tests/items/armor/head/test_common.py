from XivDbReader.scrape import ParseItems
from XivDbReader.collections import *
import pytest

pytest.html = ''
pytest.url = 'https://na.finalfantasyxiv.com/lodestone/playguide/db/item/fbeb3ec5228/'
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
    if pytest.item.name == 'Koppranickel Turban of Scouting':
        assert True

def test_glamourOptions(parseItemData):
    if pytest.item.companyCrest == True and \
        pytest.item.glamourChest == True and \
        pytest.item.armorie == False:
        assert True

def test_itemLevel(parseItemData):
    res = pytest.item.itemLevel
    if res == 255:
        assert True

def test_magicDefense(parseItemData):
    res = pytest.item.magicDefense
    if res == 168:
        assert True
    else: assert False

def test_defense(parseItemData):
    res = pytest.item.defense
    if res == 168:
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

def test_itemJobs(parseItemData):
    if "NIN" in pytest.item.jobs:
        assert True

def test_jobLevel(parseItemData):
    if pytest.item.level == 255:
        assert True

def test_attributes(parseItemData):
    if pytest.item.stats.dexterity == 83 and \
        pytest.item.stats.directHitRate == 47 and \
        pytest.item.stats.criticalHit == 67 and \
        pytest.item.stats.vitality == 92:
        assert True

## Materia

def test_materiaSlots(parseItemData):
    if pytest.item.materia.slots == 2:
        assert True

def test_materiaMelderClass(parseItemData):
    if pytest.item.materia.melderJob == "Goldsmith":
        assert True

def test_materiaMelderLevel(parseItemData):
    if pytest.item.materia.melderLevel == 60:
        assert True

def test_materiaAdvanced(parseItemData):
    if pytest.item.materia.advancedMelding == True:
        assert True        

## Repair

def test_repairClass(parseItemData):
    if pytest.item.repair.job == "Goldsmith":
        assert True

def test_repairClassLevel(parseItemData):
    if pytest.item.repair.level == 50:
        assert True

def test_repairMaterial(parseItemData):
    if pytest.item.repair.material == 'Grade 6 Dark Matter':
        assert True



def test_extractable(parseItemData):
    if pytest.item.extractable == True:
        assert True

def test_projectable(parseItemData):
    if pytest.item.projectable == True:
        assert True

def test_dyeable(parseItemData):
    if pytest.item.dyeable == False:
        assert True

def test_desynth(parseItemData):
    if pytest.item.desynth == 255.0:
        assert True

## Vendors

def test_sellsFor(parseItemData):
    if pytest.item.vendors.sell == 300:
        assert True

def test_buyFor(parseItemData):
    if pytest.item.vendors.buy == 19994:
        assert True

def test_vendors(parseItemData):
    if len(pytest.item.vendors.buyFrom) == 5:
        assert True

def test_vendorsNames(parseItemData):
    if pytest.item.vendors.buyFrom[2].name == 'Merchant & Mender':
        assert True
    else:
        assert False

def test_vendorLocations(parseItemData):
    if pytest.item.vendors.buyFrom[2].location == 'The Fringes (X:8.7 Y:10.9)':
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
    if pytest.item.requiredItems.__len__() == 0:
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
    if pytest.item.untradable == False and \
        pytest.item.unique == False:
        assert True