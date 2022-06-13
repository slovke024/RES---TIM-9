import string

codes = [("CODE_ANALOG","CODE_DIGITAL"),("CODE_CUSTOM","CODE_LIMITSET"),("CODE_SINGLENOE","CODE_MULTIPLENODE"),("CODE_CONSUMER","CODE_SOURCE")]
class RecieverProperty:
    code:string
    value:int
    def __init__(self,code,value):
        self.code=code
        self.value=value



class CollectionDescription:
    
    id:int
    DataSet:int
    HistoricalCollection:list()
    def __init__(self,id,dataset,historical):
        self.id=id
        self.DataSet=dataset
        self.HistoricalCollection=historical

class DeltaCD:
    add:list()
    update:list()
    