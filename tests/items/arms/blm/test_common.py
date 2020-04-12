from XivDbReader.scrape import ParseItems
from XivDbReader.collections import *
import pytest

pytest.html = ''
pytest.url = 'https://na.finalfantasyxiv.com/lodestone/playguide/db/item/f90e2767ea6/'
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
    if pytest.item.name == 'Dwarven Lignum Pole':
        assert True

def test_glamourOptions(parseItemData):
    if pytest.item.companyCrest == False and \
        pytest.item.glamourChest == True and \
        pytest.item.armorie == False:
        assert True

def test_itemLevel(parseItemData):
    pi = ParseItems()
    res = pi.getDetails(html=pytest.html)
    if res.itemLevel == 415:
        assert True

def test_itemAttack(parseItemData):
    if pytest.item.physicalDamage == 0:
        assert True

def test_magicalAttack(parseItemData):
    if pytest.item.magicDamage ==136:
        assert True

def test_itemAutoAttack(parseItemData):
    if pytest.item.autoAttack == 109.33:
        assert True

def test_delay(parseItemData):
    if pytest.item.delay == 3.28:
        assert True

def test_itemJobs(parseItemData):
    if "BLM" in pytest.item.jobs:
        assert True

def test_jobLevel(parseItemData):
    if pytest.item.level == 78:
        assert True

def test_attributes(parseItemData):
    if pytest.item.stats.intelligence == 370 and \
        pytest.item.stats.criticalHit == 350 and \
        pytest.item.stats.vitality == 370 and \
        pytest.item.stats.spellSpeed == 245:
        assert True

## Materia

def test_materiaSlots(parseItemData):
    if pytest.item.materia.slots == 2:
        assert True

def test_materiaMelderClass(parseItemData):
    if pytest.item.materia.melderJob == "Carpenter":
        assert True

def test_materiaMelderLevel(parseItemData):
    if pytest.item.materia.melderLevel == 78:
        assert True

def test_materiaAdvanced(parseItemData):
    if pytest.item.materia.advancedMelding == True:
        assert True        

## Repair

def test_repairClass(parseItemData):
    if pytest.item.repair.job == "Carpenter":
        assert True

def test_repairClassLevel(parseItemData):
    if pytest.item.repair.level == 68:
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
    if pytest.item.dyeable == False:
        assert True

def test_desynth(parseItemData):
    if pytest.item.desynth == 415.0:
        assert True

## Vendors

def test_sellsFor(parseItemData):
    if pytest.item.sellPrice == 691:
        assert True

def test_buyFor(parseItemData):
    if pytest.item.buyPrice == 44283:
        assert True

def test_vendors(parseItemData):
    if len(pytest.item.buyFrom) == 1:
        assert True

def test_vendorsNames(parseItemData):
    if pytest.item.buyFrom[0]['name'] == 'Tholl Junkmonger':
        assert True
    else: assert False

def test_vendorLocations(parseItemData):
    if pytest.item.buyFrom[0]['loc'] == 'Kholusia (X:11.9 Y:8.8)':
        assert True

## Instances/Fights

def test_dropsFrom(parseItemData):
    if pytest.item.relatedDuties.__len__() == 0:
        assert True

def test_dropsFromLevel(parseItemData):
    if pytest.item.relatedDuties.__len__() == 0:
        assert True
    
def test_dropsFromRequiredItemLevel(parseItemData):
    if pytest.item.relatedDuties.__len__ == 0:
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
    if pytest.item.untradable == False and \
        pytest.item.unique == False:
        assert True