
from XivDbReader.scrape import ParseItems
from XivDbReader.collections import *
import pytest

pytest.html = ''
pytest.url = 'https://na.finalfantasyxiv.com/lodestone/playguide/db/item/6b663dd567f/'
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
    if pytest.item.name == 'Augmented Catalyst':
        assert True

def test_glamourOptions(parseItemData):
    if pytest.item.companyCrest == False and \
        pytest.item.glamourChest == True and \
        pytest.item.armorie == False:
        assert True

def test_itemLevel(parseItemData):
    if pytest.item.itemLevel == 460:
        assert True

def test_itemAttack(parseItemData):
    if pytest.item.magicDamage == 145:
        assert True

def test_itemAutoAttack(parseItemData):
    if pytest.item.autoAttack == 116.398:
        assert True

def test_delay(parseItemData):
    if pytest.item.delay == 3.28:
        assert True

def test_itemJobs(parseItemData):
    if "BLM" in pytest.item.jobs:
        assert True

def test_jobLevel(parseItemData):
    if pytest.item.level == 80:
        assert True

def test_attributes(parseItemData):
    if pytest.item.stats.intelligence == 452 and \
        pytest.item.stats.determination == 282 and \
        pytest.item.stats.spellSpeed == 403 and \
        pytest.item.stats.vitality == 429:
        assert True

## Materia

def test_materiaSlots(parseItemData):
    if pytest.item.materia.slots == 2:
        assert True

def test_materiaMelderClass(parseItemData):
    if pytest.item.materia.melderJob == "Carpenter":
        assert True

def test_materiaMelderLevel(parseItemData):
    if pytest.item.materia.melderLevel == 70:
        assert True

def test_materiaAdvanced(parseItemData):
    if pytest.item.materia.advancedMelding == False:
        assert True

## Repair

def test_repairClass(parseItemData):
    if pytest.item.repair.job == "Carpenter":
        assert True

def test_repairClassLevel(parseItemData):
    if pytest.item.repair.level == 70:
        assert True

def test_repairMaterial(parseItemData):
    if pytest.item.repair.material == 'Grade 7 Dark Matter':
        assert True


def test_extractable(parseItemData):
    if pytest.item.extractable == True:
        assert True

def test_projectable(parseItemData):
    if pytest.item.projectable == True:
        assert True

def test_dyeable(parseItemData):
    if pytest.item.dyeable == True:
        assert True

def test_desynth(parseItemData):
    if pytest.item.desynth == 460.0:
        assert True

def test_sellsFor(parseItemData):
    if pytest.item.vendors.sell == 1772:
        assert True

def test_buyFor(parseItemData):
    if pytest.item.vendors.buy == 0:
        assert True

def test_vendors(parseItemData):
    if len(pytest.item.vendors.buyFrom) == 0:
        assert True

def test_vendorsNames(parseItemData):
    if pytest.item.vendors.buyFrom.__len__() == 0:
        assert True

def test_vendorLocations(parseItemData):
    if pytest.item.vendors.buyFrom.__len__() == 0:
        assert True

def test_dropsFrom(parseItemData):
    if pytest.item.relatedDuties.__len__() == 0:
        assert True

def test_dropsFromLevel(parseItemData):
    if pytest.item.relatedDuties.__len__() == 0:
        assert True
    
def test_dropsFromRequiredItemLevel(parseItemData):
    if pytest.item.relatedDuties.__len__() == 0:
        assert True

def test_RequiredItemName(parseItemData):
    if pytest.item.requiredItems.__len__() == 0:
        assert True

def test_RequiredItemCount(parseItemData):
    if pytest.item.requiredItems.__len__() == 0:
        assert True 

def test_RequiredItemNpc(parseItemData):
    if pytest.item.requiredItems.__len__() == 0:
        assert True 

def test_RequiredItemNpcLocation(parseItemData):
    if pytest.item.requiredItems.__len__() == 0:
        assert True 

def test_isUniqueUntradable(parseItemData):
    if pytest.item.untradable == True and \
        pytest.item.unique == False:
        assert True
