
from XivDbReader.scrape import ParseItems
from XivDbReader.collections import *
import pytest

pytest.html = ''
pytest.url = 'https://na.finalfantasyxiv.com/lodestone/playguide/db/item/29f2f5b7711/'
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
    if pytest.item.name == 'Misos':
        assert True

def test_glamourOptions(parseItemData):
    if pytest.item.companyCrest == False and \
        pytest.item.glamourChest == True and \
        pytest.item.armorie == False:
        assert True

def test_itemLevel(parseItemData):
    if pytest.item.itemLevel == 465:
        assert True

def test_itemAttack(parseItemData):
    if pytest.item.physicalDamage == 120:
        assert True

def test_itemAutoAttack(parseItemData):
    if pytest.item.autoAttack == 89.60:
        assert True

def test_delay(parseItemData):
    if pytest.item.delay == 2.24:
        assert True

def test_itemJobs(parseItemData):
    if "PLD" in pytest.item.jobs:
        assert True

def test_jobLevel(parseItemData):
    if pytest.item.level == 80:
        assert True

def test_attributes(parseItemData):
    if pytest.item.strength == 369 and \
        pytest.item.tenacity == 228 and \
        pytest.item.vitality == 391 and \
        pytest.item.determination == 325:
        assert True

def test_materiaSlots(parseItemData):
    if pytest.item.materiaSlots == 2:
        assert True

def test_repairClass(parseItemData):
    if pytest.item.repairClass == "Blacksmith":
        assert True

def test_repairClassLevel(parseItemData):
    if pytest.item.repairClassLevel == 70:
        assert True

def test_repairMaterial(parseItemData):
    if pytest.item.repairMaterial == 'Grade 7 Dark Matter':
        assert True

##TODO materia melding

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
    if pytest.item.desynth == 465.0:
        assert True

def test_sellsFor(parseItemData):
    if pytest.item.sellPrice == 1182:
        assert True

def test_buyFor(parseItemData):
    if pytest.item.buyPrice == 0:
        assert True

def test_vendors(parseItemData):
    if len(pytest.item.buyFrom) == 0:
        assert True

def test_dropsFrom(parseItemData):
    if pytest.item.relatedDuties[0]['name'] == "The Minstrel's Ballad: Hades's Elegy":
        assert True

def test_RequiredItemName(parseItemData):
    if "Hades Totem" in pytest.item.requiredItems[0]['item']:
        assert True

def test_RequiredItemCount(parseItemData):
    if pytest.item.requiredItems[0]['itemAmount'] == 7:
        assert True 

def test_RequiredItemNpc(parseItemData):
    if "Fathard" in pytest.item.requiredItems[0]['npc']:
        assert True 

def test_RequiredItemNpcLocation(parseItemData):
    if "Eulmore" in pytest.item.requiredItems[0]['location']:
        assert True 

