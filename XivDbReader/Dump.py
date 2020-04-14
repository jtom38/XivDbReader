
from XivDbReader.settings import Settings
from XivDbReader.scrape import ParseList, ParseItems
from XivDbReader.collections import *
import csv

class Dump():
    """

    """

    def __init__(self):
        self.settings = Settings()
        pass

    def getAllArmsLinks(self):
        url: str = self.settings.links.armsAllUrl
        loop: bool = True
        counter: int = 1

        links: List[str] = []
        items: List[Weapon] = []
        while(loop == True):
            url = f"{self.settings.links.armsAllUrl}&page={counter}"
            pl = ParseList(url)
            res = pl.FindLinks()
            
            counter = counter + 1
            
            for r in res:
                pi = ParseItems()
                details = pi.getDetails(href=r)
                self.writeWeaponCSV(details)
                items.append(details)
                print(f"Got details on '{details.name}''")

            print(f"Finished page {counter}")

    def writeWeaponCSV(self, w: Weapon):
        with open('weapons.csv', 'w', newline='') as csvfile:
            try:
                writecvs = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                header: str = ['key', 'itemLevel', 'jobs', 'level', 'stats.strength', 'stats.vitality', 'stats.dexterity', 'stats.intelligence']
                writecvs.writerow(header)
                writecvs.writerow([w.slot, w.itemLevel, w.jobs, w.level, w.stats.strength, w.stats.vitality, w.stats.dexterity, w.stats.intelligence])
            except Exception as e:
                print(e)
