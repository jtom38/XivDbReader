
from typing import List
from XivDbReader.collections import Weapon
from XivDbReader import Reader, ExportCsv


#r: Reader = Reader(job='pld')
#pldArms: List[Weapon] = r.getArms(recordLimit=1)


whmReader: Reader = Reader(job='whm')
whmArms: List[Weapon] = whmReader.getArms(recordLimit=10)

ec = ExportCsv(recordType='weapon', recordJob='whm')
ec.write(whmArms)