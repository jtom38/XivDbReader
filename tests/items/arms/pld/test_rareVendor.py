
from XivDbReader.scrape import ParseItems
from XivDbReader.collections import *
import pytest

pytest.html = ''
pytest.url = 'https://na.finalfantasyxiv.com/lodestone/playguide/db/item/c4e26dc27d0/'
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
    if pytest.item.name == 'Ironworks Magitek Sword':
        assert True

def test_glamourOptions(parseItemData):
    if pytest.item.companyCrest == False and \
        pytest.item.glamourChest == True and \
        pytest.item.armorie == False:
        assert True

def test_itemLevel(parseItemData):
    if pytest.item.itemLevel == 120:
        assert True

def test_itemAttack(parseItemData):
    if pytest.item.physicalDamage == 54:
        assert True

def test_itemAutoAttack(parseItemData):
    if pytest.item.autoAttack == 36.00:
        assert True

def test_delay(parseItemData):
    if pytest.item.delay == 2.00:
        assert True

def test_itemJobs(parseItemData):
    if "PLD" in pytest.item.jobs:
        assert True

def test_jobLevel(parseItemData):
    if pytest.item.level == 50:
        assert True

def test_attributes(parseItemData):
    if pytest.item.stats.strength == 34 and \
        pytest.item.stats.directHitRate == 24 and \
        pytest.item.stats.vitality == 40 and \
        pytest.item.stats.determination == 24:
        assert True

def test_materiaSlots(parseItemData):
    if pytest.item.materia.slots == 0:
        assert True

def test_repairClass(parseItemData):
    if pytest.item.repair.job == "Blacksmith":
        assert True

def test_repairClassLevel(parseItemData):
    if pytest.item.repair.level == 40:
        assert True

def test_repairMaterial(parseItemData):
    if pytest.item.repair.material == 'Grade 5 Dark Matter':
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
    if pytest.item.desynth == 120.0:
        assert True

def test_sellsFor(parseItemData):
    if pytest.item.vendors.sell == 756:
        assert True

def test_buyFor(parseItemData):
    if pytest.item.vendors.buy == 0:
        assert True

def test_vendors(parseItemData):
    if len(pytest.item.vendors.buyFrom) == 0:
        assert True

def test_dropsFrom(parseItemData):
    if pytest.item.relatedDuties.__len__() == 0:
        assert True
    else: assert False

def test_requiredItemTrades(parseItemData):
    if pytest.item.requiredItems.__len__() == 4:
        assert True
    else: assert False

def test_RequiredItemName(parseItemData):
    if pytest.item.requiredItems[0].items[0].name == "Rowena's Token (Poetics)" and \
        pytest.item.requiredItems[0].items[1].name == "Encrypted Tomestone" and \
        pytest.item.requiredItems[1].items[0].name == "Silver Chocobo Feather" and \
        pytest.item.requiredItems[2].items[0].name == "Silver Chocobo Feather" and \
        pytest.item.requiredItems[3].items[0].name == "Silver Chocobo Feather":
        assert True
    else: assert False

def test_RequiredItemCount(parseItemData):
    if pytest.item.requiredItems[0].items[0].amount == 7 and \
        pytest.item.requiredItems[0].items[1].amount == 1 and \
        pytest.item.requiredItems[1].items[0].amount == 5 and \
        pytest.item.requiredItems[1].items[0].amount == 5 and \
        pytest.item.requiredItems[1].items[0].amount == 5:    
        assert True 
    else: assert False

def test_RequiredItemNpc(parseItemData):
    if "Aelina" in pytest.item.requiredItems[0].npc and \
        "Calamity Salvager" in pytest.item.requiredItems[1].npc and \
        "Calamity Salvager" in pytest.item.requiredItems[2].npc and \
        "Calamity Salvager" in pytest.item.requiredItems[3].npc:
        assert True
    else: assert False

def test_RequiredItemNpcLocation(parseItemData):
    if "Eulmore" in pytest.item.requiredItems[0].location:
        assert True 

