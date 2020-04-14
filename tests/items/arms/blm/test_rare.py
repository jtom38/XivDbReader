
from XivDbReader.scrape import ParseItems
from XivDbReader.collections import *
import pytest

pytest.html = ''
pytest.url = 'https://na.finalfantasyxiv.com/lodestone/playguide/db/item/20c4ee34148/'
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

def test_itemLevel(parseItemData):
    res = pytest.item
    if res.itemLevel == 405:
        assert True
    else: assert False

def test_jobLevel(parseItemData):
    res = pytest.item
    if res.level == 70:
        assert True
    else: assert False

def test_damage(parseItemData):
    if pytest.item.magicDamage == 147:
        assert True
    else: assert False

def test_delay(parseItemData):
    if pytest.item.delay == 3.28:
        assert True
    else: assert False

def test_itemJobs(parseItemData):
    if "BLM" in pytest.item.jobs:
        assert True
    else: assert False

def test_attributes(parseItemData):
    if pytest.item.stats.vitality == 410 and \
        pytest.item.stats.intelligence == 403 and \
        pytest.item.stats.criticalHit == 249 and \
        pytest.item.stats.spellSpeed == 356:
        assert True
    else: assert False

def test_materiaSlots(parseItemData):
    if pytest.item.materia.slots == 2:
        assert True
    else: assert False

def test_repairClass(getHtmlSource):
    if pytest.item.repair.job == "Goldsmith":
        assert True
    else: assert False

def test_repairClassLevel(parseItemData):
    if pytest.item.repair.level == 60:
        assert True
    else: assert False

def test_sellsFor(parseItemData):
    if pytest.item.vendors.sell == 2752:
        assert True
    else: assert False

def test_dropsFrom(parseItemData):
    if pytest.item.relatedDuties[0].name == 'Alphascape V4.0 (Savage)':
        assert True
    else: assert False

def test_RequiredItemName(parseItemData):
    if "Alphascape Datalog v4.0" in pytest.item.requiredItems[0].items[0].name:
        assert True
    else: assert False

def test_RequiredItemCount(parseItemData):
    if pytest.item.requiredItems[0].items[0].amount == 8:
        assert True 
    else: assert False

def test_RequiredItemNpc(parseItemData):
    if "Gelfradus" in pytest.item.requiredItems[0].npc:
        assert True 
    else: assert False

def test_RequiredItemNpcLocation(parseItemData):
    if "Rhalgr's Reach" in pytest.item.requiredItems[0].location:
        assert True 
    else: assert False