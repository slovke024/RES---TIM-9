from email import message
import string
import sqlite3
from datetime import datetime
import logging

codes = [("CODE_ANALOG","CODE_DIGITAL"),("CODE_CUSTOM","CODE_LIMITSET"),("CODE_SINGLENOE","CODE_MULTIPLENODE"),("CODE_CONSUMER","CODE_SOURCE")]




class CollectionDescription:
    
    id:int
    DataSet:int
    HistoricalCollection:list()
    def __init__(self,id,dataset,historical):
        self.id=id
        self.DataSet=dataset
        self.HistoricalCollection=historical

class RecieverProperty:
    code:string
    value:int
    def __init__(self,code,value):
        self.code=code
        self.value=value

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
        return True 
    def poslednjaVrednost(self,code):
        conn = sqlite3.connect('test_database.db')
        c = conn.cursor() 
        c.execute(F"SELECT vrednost FROM {self.dataSet} WHERE kod='{code}' AND dateTime=(SELECT MAX(dateTime) FROM {self.dataSet} WHERE kod='{code}')")
        conn.commit()
        latestValue=c.fetchall()
        broj=latestValue[0]
        print(F"Poslednja vrednost koda {code} je {broj[0]}") 
        return True
    def vremenskiInterval(self,code,interval1,interval2):
        conn = sqlite3.connect('test_database.db')
        c = conn.cursor() 
        c.execute(F"SELECT * from {self.dataSet} WHERE kod='{code}' AND (dateTime BETWEEN '{interval1}' AND '{interval2}')")
        conn.commit()
        latestValue=c.fetchall()
        for x in latestValue:
            print(F"[{x[0]}] {x[1]} {x[2]}")
        return True

        


class Logger:
    def upisiLog(self,msg):
        logging.basicConfig(filename='logovi.txt', encoding='utf-8', level=logging.DEBUG)
        logging.debug(msg)
        return True

class CodeValue:
  def __init__(self, code, value):
    self.code = code
    self.value = value