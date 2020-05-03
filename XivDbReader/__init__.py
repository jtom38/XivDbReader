
from .settings import *
from .collections import *
from XivDbReader.scrape import ParseList, ParseItems
from typing import List
import os
import csv

class ExportCsv():
    def __init__(self, fileName: str):
        self.fileName: str = f"{fileName}.csv"

        self.weaponHeader: List[str] = [
            'key','url','pictureUrl','name'
            ,'rarity','untradeable','unique','slot'
            ,'itemLevel','jobs','level','companyCrest'
            ,'armorie','glamourChest','dyeable','extractable'
            ,'projectable','desynth' ]
        self.statsHeader: List[str] =[
            'key','str','vit','dex'
            ,'intelligence','mnd','det','skl'
            ,'spl','crt','dhr','ten','pie']
        self.repairHeader: List[str] = ['key','job','level','material']
        self.materiaHeader: List[str] = ['key','slots','melderLevel','advancedMelding']
        pass

    def __writeHeaders__(self, fileName: str, ):
        if os.path.isfile(f'{fileName}.csv') == False:
            with open('weapons.csv', 'w', newline='') as csvfile:
                try:
                    writecvs = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    if 'weapon' in fileName:
                        writecvs.writerow(self.weaponHeader)
                    if 'stats' in fileName:
                        writecvs.writerow(self.statsHeader)
                    if 'repair' in fileName:
                        writecvs.writerow(self.repairHeader)
                    if 'materia' in fileName:
                        writecvs.writerow(self.materiaHeader)
                except Exception as e:
                    print(f"ERROR - {e}") 

    def __removeExistingFile__(self, fileName: str) -> None:
        if os.path.isfile(f'{fileName}.csv') == True:
            try:
                os.remove(f"{fileName}.csv")
            except Exception as e:
                print(f"ERROR - {e}")
    

class Reader():
    def __init__(self, job: str):
        self.job = job
        pass

    def getArms(self, recordLimit: int = -1) -> List[Weapon]:
        self.recordLimit = recordLimit
        weapons: List[Weapon] = []
        s = Settings()
        link = s.links.getArmLink(job=self.job)
        
        page: int = 0
        loopKeeper: bool = False
        # Get the items from the list

        while loopKeeper == False:
            res = self.__extractInfo__(f"{link}&page={page}")
            if res.__len__() == 0:
                loopKeeper = True
                break
            else:
                weapons.append(res)
                page = page + 1
                if weapons.__len__() == self.recordLimit:
                    break

        self.recordLimit = -1
        return weapons

    def getArmor(self, slot: str, recordLimit: int = -1) -> List[Armor]:
        self.recordLimit = recordLimit
        armors: List[Armor] = []
        s = Settings()
        link = s.links.getArmorLink(slot)
        page:int = 0
        loopKeeper: bool = False
        while loopKeeper == False:
            res = self.__extractInfo__(f"{link}&page={page}")
            if res.__len__() == 0:
                loopKeeper = True
                break
            else:
                armors.append(res)
                page = page + 1
                if armors.__len__() == self.recordLimit:
                    break

        self.recordLimit = -1
        return armors

    def __extractInfo__(self, link: str) -> List[Item]:
        itemsList: List[Item] = []
        pl = ParseList(link)
        items: List[str] = pl.FindLinks()

        for item in items:
            pi = ParseItems()
            details: Item = pi.getDetails(href=item)
            itemsList.append(details)
            print(f"INFO - Got info on '{details.name}'")
            if itemsList.__len__() == self.recordLimit:
                break
        
        return itemsList

