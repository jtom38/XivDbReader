 
from XivDbReader.Reader import Reader


def test_armsPld():
    r = Reader()
    res = r.getArms('Pld',1)
    if res.__len__() == 1:
        assert True

def test_armsPld10():
    r = Reader()
    res = r.getArms('pld', 10)
    if len(res) == 10:
        assert True
    else: assert False

def test_linksArms():
    r = Reader()
    res = r.getItemLinks
