


class Settings():
    def __init__(self):
        self.sleepTimer: int = 5

        self.links = Links()



class Links():
    def __init__(self):
        self.rootUrl = "https://na.finalfantasyxiv.com"
        self.dbUrl = f"{self.rootUrl}/lodestone/playguide/db"
        
        self.armsAllUrl = f"{self.dbUrl}/item/?category2=1"
        self.armsUrl = f"{self.dbUrl}/item/?category2=1&category3="
        self.armsMnk = f"{self.armsUrl}1"
        self.armsPld = f"{self.armsUrl}2"
        self.armsWar = f"{self.armsUrl}3"
        
        self.toolsAllUrl = f"{self.dbUrl}/item/?category2=2"

        self.armorAllUrl = f"{self.dbUrl}/item/?category2=3"
        self.accessoriesAllUrl = f"{self.dbUrl}/item/?category2=4"
        self.medsAllUrl = f"{self.dbUrl}/item/?category2=5&category3=44"
        self.foodAllUrl = f"{self.dbUrl}/item/?category2=5&category3=46"
        self.materialsAllUrl = f"{self.dbUrl}/item/?category2=6"

    def getArmLink(self, job: str, page: int) -> str:
        """
        About:
            This will generate links to check based off values given.

        Params:

        """

        cat = -1
        if job == 'gld' or job == 'pld':
            cat = 2
        elif job == "mrd" or job == 'war':
            cat = 3
        elif job == 'drk':
            cat = 87
        elif job == 'gnb':
            cat = 106
        elif job == 'lnc' or job == 'drg':
            cat = 5
        elif job == 'pug' or job == 'mnk':
            cat = 1
        elif job == 'sam':
            cat = 96
        elif job == 'rog' or job == 'nin':
            cat = 84
        elif job == 'arc' or job == 'brd':
            cat = 4
        elif job == 'mch':
            cat = 88
        elif job == 'dnc':
            cat = 107
        elif job == 'thm':
            cat = 6
        else:
            cat = -1

        if cat == -1:
            return f"{self.armsAllUrl}&page={page}"
        else:
            return f"{self.armorAllUrl}&page={page}category3={cat}"

    def getArmorLink(self, slot: str, page: int) -> str:
        raise NotImplementedError()
        #slot = 
        #return f"{self.armorAllUrl}&page={page}"
