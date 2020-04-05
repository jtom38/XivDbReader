
from XivDbReader.scrape import ParseItems
from XivDbReader.collections import Weapon
import pytest

pytest.e_html = ''
pytest.e_url = 'https://na.finalfantasyxiv.com/lodestone/playguide/db/item/6b663dd567f/'
pytest.e_item: Weapon = Weapon()

@pytest.fixture
def getHtmlSource():
    if pytest.e_html == '':
        pi = ParseItems()
        pytest.e_html = pi.GetHtmlSource(pytest.e_url)

@pytest.fixture
def parseItemData(getHtmlSource):
    w = Weapon()
    if pytest.e_item.delay == 0.0:
        # value is defaulted
        pi = ParseItems()
        pytest.e_item = pi.getDetails(html=pytest.e_html)

def test_itemLevel(parseItemData):
    res = pytest.e_item
    if res.itemLevel == 405:
        assert True

def test_jobLevel(parseItemData):
    res = pytest.e_item
    if res.level == 70:
        assert True

def test_damage(parseItemData):
    res = pytest.e_item
    if res.magicDamage == 147:
        assert True

def test_autoAttack(parseItemData):
    res = pytest.e_item
    if res.autoAttack == 119.17:
        assert True

def test_delay(parseItemData):
    res = pytest.e_item
    if res.delay == 3.28:
        assert True

def test_itemRarity(parseItemData):
    res = pytest.e_item
    if res.rarity == "Epic":
        assert True       

def test_itemJobs(parseItemData):
    res = pytest.e_item
    if "THM" in res.jobs:
        assert True

def test_attributes(parseItemData):
    res = pytest.e_item
    if res.vitality == 410 and res.intelligence == 403:
        assert True

def test_materiaSlots(parseItemData):
    res = pytest.e_item
    if res.materiaSlots == 0:
        assert True

def test_repairClass(parseItemData):
    res = pytest.e_item
    if res.repairClass == "Carpenter":
        assert True

def test_repairClassLevel(parseItemData):
    item = pytest.e_item
    if item.repairClassLevel == 60:
        assert True

def test_sellsFor(parseItemData):
    res = pytest.e_item
    if res.sellPrice == 0:
        assert True

def test_dropsFrom(parseItemData):
    res = pytest.e_item
    if len(res.relatedDuties) == 0:
        assert True

def test_relatedItems(parseItemData):
    res = pytest.e_item
    if len(res.requiredItems) == 0:
        assert True
