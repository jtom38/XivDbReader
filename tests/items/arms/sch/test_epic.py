from XivDbReader.scrape import ParseItems
from XivDbReader.collections import *
import pytest

pytest.html = ''
pytest.url = 'https://na.finalfantasyxiv.com/lodestone/playguide/db/item/b6dda0ded2e/'
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
    if pytest.item.name == 'Jebat Eureka':
        assert True

def test_glamourOptions(parseItemData):
    if pytest.item.companyCrest == False and \
        pytest.item.glamourChest == False and \
        pytest.item.armorie == False:
        assert True

def test_itemLevel(parseItemData):
    pi = ParseItems()
    res = pi.getDetails(html=pytest.html)
    if res.itemLevel == 405:
        assert True

def test_itemAttack(parseItemData):
    if pytest.item.physicalDamage == 0:
        assert True

def test_magicDamage(parseItemData):
    if pytest.item.magicDamage == 147:
        assert True
    else: 
        assert False

def test_itemAutoAttack(parseItemData):
    if pytest.item.autoAttack == 5.33:
        assert True

def test_delay(parseItemData):
    if pytest.item.delay == 3.12:
        assert True

def test_itemJobs(parseItemData):
    if "SCH" in pytest.item.jobs:
        assert True

def test_jobLevel(parseItemData):
    if pytest.item.level == 70:
        assert True

def test_attributes(parseItemData):
    if pytest.item.mind == 403 and \
        pytest.item.vitality == 410:
        assert True

## Materia

def test_materiaSlots(parseItemData):
    if pytest.item.materiaSlots == 0:
        assert True

def test_materiaMelderClass(parseItemData):
    if pytest.item.materiaMelderClass == "":
        assert True

def test_materiaMelderLevel(parseItemData):
    if pytest.item.materiaMelderLevel == 00:
        assert True

def test_materiaAdvanced(parseItemData):
    if pytest.item.advancedMelding == False:
        assert True        

## Repair

def test_repairClass(parseItemData):
    if pytest.item.repairClass == "Alchemist":
        assert True

def test_repairClassLevel(parseItemData):
    if pytest.item.repairClassLevel == 60:
        assert True

def test_repairMaterial(parseItemData):
    if pytest.item.repairMaterial == 'Grade 7 Dark Matter':
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
    if pytest.item.desynth == 0.0:
        assert True

## Vendors

def test_sellsFor(parseItemData):
    if pytest.item.sellPrice == 0:
        assert True

def test_buyFor(parseItemData):
    if pytest.item.buyPrice == 0:
        assert True

def test_vendors(parseItemData):
    if len(pytest.item.buyFrom) == 0:
        assert True
    else: 
        assert False

def test_vendorsNames(parseItemData):
    if pytest.item.buyFrom.__len__() == 0:
        assert True
    else: 
        assert False

def test_vendorLocations(parseItemData):
    if pytest.item.buyFrom.__len__() == 0:
        assert True
    else:
        assert False

## Instances/Fights

def test_dropsFrom(parseItemData):
    if pytest.item.relatedDuties.__len__() == 0:
        assert True
    else:
        assert False

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
    if pytest.item.untradable == True and \
        pytest.item.unique == True:
        assert True