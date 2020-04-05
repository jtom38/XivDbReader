from XivDbReader.scrape import ParseItems
from XivDbReader.collections import *
import pytest

pytest.html = ''
pytest.url = 'https://na.finalfantasyxiv.com/lodestone/playguide/db/item/0cdf666234e/'
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
    if pytest.item.name == 'Ash Macuahuitl':
        assert True

def test_glamourOptions(parseItemData):
    if pytest.item.companyCrest == False and \
        pytest.item.glamourChest == True and \
        pytest.item.armorie == False:
        assert True

def test_itemLevel(parseItemData):
    pi = ParseItems()
    res = pi.getDetails(html=pytest.html)
    if res.itemLevel == 10:
        assert True

def test_itemAttack(parseItemData):
    if pytest.item.physicalDamage == 8:
        assert True

def test_itemAutoAttack(parseItemData):
    if pytest.item.autoAttack == 5.33:
        assert True

def test_delay(parseItemData):
    if pytest.item.delay == 2.00:
        assert True

def test_itemJobs(parseItemData):
    if "PLD" in pytest.item.jobs:
        assert True

def test_jobLevel(parseItemData):
    if pytest.item.level == 10:
        assert True

def test_attributes(parseItemData):
    if pytest.item.strength == 1 and \
        pytest.item.tenacity == 1 and \
        pytest.item.vitality == 1:
        assert True

def test_materiaSlots(parseItemData):
    if pytest.item.materiaSlots == 0:
        assert True

def test_repairClass(parseItemData):
    if pytest.item.repairClass == "Carpenter":
        assert True

def test_repairClassLevel(parseItemData):
    if pytest.item.repairClassLevel == 1:
        assert True

def test_repairMaterial(parseItemData):
    if pytest.item.repairMaterial == 'Grade 1 Dark Matter':
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
    if pytest.item.desynth == 10.0:
        assert True

def test_sellsFor(parseItemData):
    if pytest.item.sellPrice == 7:
        assert True

def test_buyFor(parseItemData):
    if pytest.item.buyPrice == 316:
        assert True

def test_vendors(parseItemData):
    if len(pytest.item.buyFrom) == 5:
        assert True

def test_vendorsNames(parseItemData):
    if pytest.item.buyFrom[0]['name'] == 'Faezghim' and \
        pytest.item.buyFrom[1]['name'] == "Geraint" and \
        pytest.item.buyFrom[2]['name'] == 'Gealous Guggernaunt' and \
        pytest.item.buyFrom[3]['name'] == 'Merchant & Mender' and \
        pytest.item.buyFrom[4]['name'] == 'Merchant & Mender':
        assert True

def test_vendorLocations(parseItemData):
    if pytest.item.buyFrom[0]['loc'] == 'Limsa Lominsa Lower Decks (X:6.5 Y:11.9)' and \
        pytest.item.buyFrom[1]['loc'] == 'Old Gridania (X:14.6 Y:9.7)' and \
        pytest.item.buyFrom[2]['loc'] == "Ul'dah - Steps of Thal (X:13.9 Y:11.0)" and \
        pytest.item.buyFrom[3]['loc'] == "Western Thanalan (X:22.3 Y:16.1)" and \
        pytest.item.buyFrom[4]['loc'] == "Western Thanalan (X:15.3 Y:18.5)":
        assert True
