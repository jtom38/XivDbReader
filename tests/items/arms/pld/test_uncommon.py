from XivDbReader.scrape import ParseItems
from XivDbReader.collections import *
import pytest

pytest.html = ''
pytest.url = 'https://na.finalfantasyxiv.com/lodestone/playguide/db/item/da663f852c1/'
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
    if pytest.item.name == 'Lakeland Longsword ':
        assert True

def test_glamourOptions(parseItemData):
    if pytest.item.companyCrest == False and \
        pytest.item.glamourChest == True and \
        pytest.item.armorie == False:
        assert True

def test_itemLevel(parseItemData):
    pi = ParseItems()
    res = pi.getDetails(html=pytest.html)
    if res.itemLevel == 390:
        assert True

def test_itemAttack(parseItemData):
    if pytest.item.physicalDamage == 107:
        assert True

def test_itemAutoAttack(parseItemData):
    if pytest.item.autoAttack == 79.89:
        assert True

def test_delay(parseItemData):
    if pytest.item.delay == 2.24:
        assert True

def test_itemJobs(parseItemData):
    if "PLD" in pytest.item.jobs:
        assert True

def test_jobLevel(parseItemData):
    if pytest.item.level == 71:
        assert True

def test_attributes(parseItemData):
    if pytest.item.strength == 272 and \
        pytest.item.tenacity == 168 and \
        pytest.item.vitality == 304 and \
        pytest.item.criticalHit == 241:
        assert True

def test_materiaSlots(parseItemData):
    if pytest.item.materiaSlots == 2:
        assert True

def test_repairClass(parseItemData):
    if pytest.item.repairClass == "Blacksmith":
        assert True

def test_repairClassLevel(parseItemData):
    if pytest.item.repairClassLevel == 61:
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
    if pytest.item.dyeable == False:
        assert True

def test_desynth(parseItemData):
    if pytest.item.desynth == 390.0:
        assert True

def test_sellsFor(parseItemData):
    if pytest.item.sellPrice == 708:
        assert True

def test_buyFor(parseItemData):
    if pytest.item.buyPrice == 0:
        assert True

def test_vendors(parseItemData):
    if len(pytest.item.buyFrom) == 0:
        assert True

def test_vendorsNames(parseItemData):
    if pytest.item.buyFrom.__len__() == 0:
        assert True

def test_vendorLocations(parseItemData):
    if pytest.item.buyFrom.__len__() == 0:
        assert True

def test_dropsFrom(parseItemData):
    if pytest.item.relatedDuties[0]['name'] == "Holminster Switch":
        assert True

def test_dropsFromLevel(parseItemData):
    if pytest.item.relatedDuties[0]['requiredLevel'] == 71:
        assert True
    
def test_dropsFromRequiredItemLevel(parseItemData):
    if pytest.item.relatedDuties[0]['averageItemLevel'] == 370:
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
        pytest.item.unique == True:
        assert True
