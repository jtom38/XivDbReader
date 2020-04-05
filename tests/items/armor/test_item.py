
from XivDbReader.collections import Item
from XivDbReader.scrape import ParseItems

import pytest

class TestArmorRare():

    pytest.global_html = ""
    pytest.global_url = "https://na.finalfantasyxiv.com/lodestone/playguide/db/item/30cbc1cab18/"

    @pytest.fixture
    def getHtmlSource(self):
        if pytest.global_html == '':
            pi = ParseItems()
            pytest.global_html = pi.GetHtmlSource(pytest.global_url)


    def test_DataPull(self, getHtmlSource):
        pi = ParseItems()
        res: Item = pi.getDetails(html=pytest.global_html)
        if res.materiaSlots == None:
           assert True

class TestArmorUncommon():
    pytest.global_html = ""
    pytest.global_url = "https://na.finalfantasyxiv.com/lodestone/playguide/db/item/fd2b0428875/"

    @pytest.fixture
    def getHtmlSource(self):
        if pytest.global_html == '':
            pi = ParseItems()
            pytest.global_html = pi.GetHtmlSource(pytest.global_url)
 
    def test_DataPull(self, getHtmlSource):
        pi = ParseItems()
        res: Item = pi.getDetails(html=pytest.global_html)
        if res.materiaSlots == None:
           assert True

class TestArmorCommon():
    pytest.global_html = ""
    pytest.global_url = "https://na.finalfantasyxiv.com/lodestone/playguide/db/item/e0809678a9b/"

    @pytest.fixture
    def getHtmlSource(self):
        if pytest.global_html == '':
            pi = ParseItems()
            pytest.global_html = pi.GetHtmlSource(pytest.global_url)
 
    def test_DataPull(self, getHtmlSource):
        pi = ParseItems()
        res: Item = pi.getDetails(html=pytest.global_html)
        if res.materiaSlots == None:
           assert True
