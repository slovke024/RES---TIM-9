import string
import sqlite3
from datetime import datetime

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

class Reader:
    dataSet:string
    def __init__(self,dataset):
        self.dataSet=dataset

    def upisiUBazu(self,code,value):
        conn = sqlite3.connect('test_database.db')
        c = conn.cursor() 
        c.execute(F"INSERT INTO {self.dataSet} (kod,vrednost,dateTime) VALUES('{code}',{value},'{datetime.now()}')")
        conn.commit()   

   