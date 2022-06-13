import socket
import pickle
import sqlite3
from datetime import datetime
from klase import DeltaCD, RecieverProperty,CollectionDescription

HEADERSIZE = 10                                             # Velicina headera u primljenoj poruci

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       # TCP Konekcija
s.connect((socket.gethostname(),1237))


conn = sqlite3.connect('test_database.db')                     # Pravljenje sqlite3 test baze
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS DataSet1
          (kod TEXT, vrednost INTEGER, dateTime DATETIME)
          ''')
                    
conn.commit()
c.execute('''
          CREATE TABLE IF NOT EXISTS DataSet2
          (kod TEXT, vrednost INTEGER, dateTime DATETIME)
          ''')
                    
conn.commit()
c.execute('''
          CREATE TABLE IF NOT EXISTS DataSet3
          (kod TEXT, vrednost INTEGER, dateTime DATETIME)
          ''')
                    
conn.commit()
c.execute('''
          CREATE TABLE IF NOT EXISTS DataSet4
          (kod TEXT, vrednost INTEGER, dateTime DATETIME)
          ''')
                    
conn.commit()


def deadband(code,value):
    
    conn = sqlite3.connect('test_database.db')
    c = conn.cursor()
    dataset = "DataSet1"
    db_prosao = True

    if(code=="CODE_ANALOG"):
        dataset="DataSet1"

    if(code=="CODE_CUSTOM" or code=="CODE_LIMITSET"):
        dataset="DataSet2"

    if(code=="CODE_SINGLENOE" or code=="CODE_MULTIPLENODE"):
        dataset="DataSet3"

    if(code=="CODE_CONSUMER" or code=="CODE_SOURCE"):
        dataset="DataSet4" 
    
    
    try:
        c.execute(F"SELECT vrednost FROM {dataset} WHERE kod={code} AND dateTime=(SELECT MAX(dateTime) FROM {dataset} WHERE kod={code})")
        c.commit()
    except:
        print("##############################################################")
        return db_prosao
    else:
        latestValue=c.fetchall()
        limit = float(latestValue)*0.9

        if code !="CODE_DIGITAL":
            if value>=latestValue-limit or value<= latestValue+limit:
                db_prosao=False

        return db_prosao

#value = 100
#latest value = 100
#limit = 90
#100 >= 10  or   100 <= 190




listAdd=list()
listUpdate=list()
delta=DeltaCD()



rc=RecieverProperty
      
                                               # Petlja za primanje i ispis poruka
full_msg = b''
new_msg = True
while True:
    msg = s.recv(16)
    if new_msg:
        msglen = int(msg[:HEADERSIZE])
        new_msg = False

    full_msg += msg
    if len(full_msg) - HEADERSIZE == msglen:
        conn = sqlite3.connect('test_database.db')
        c = conn.cursor()
        counter=10
        lista =pickle.loads(full_msg[HEADERSIZE:])
        print("=======================================================")
        for x in lista:
            print(F"{x.HistoricalCollection[-counter].code} {x.HistoricalCollection[-counter].value}")

            if x.HistoricalCollection[-counter].code=="CODE_ANALOG" or x.HistoricalCollection[-counter].code=="CODE_DIGITAL":
                    prosao = deadband(x.HistoricalCollection[-counter].code,x.HistoricalCollection[-counter].value)
                    if prosao:
                        c.execute("INSERT INTO DataSet1 (kod, vrednost, dateTime) VALUES(?,?,?)",(x.HistoricalCollection[-counter].code,x.HistoricalCollection[-counter].value, datetime.now()))
                        conn.commit()
                        print("Kod uspesno upisan u bazu.")
                    else:
                        print("Kod ne ispunjava deadband uslov.")
            if x.HistoricalCollection[-counter].code=="CODE_CUSTOM" or x.HistoricalCollection[-counter].code=="CODE_LIMITSET":
                    prosao = deadband(x.HistoricalCollection[-counter].code,x.HistoricalCollection[-counter].value)
                    if prosao:
                        c.execute("INSERT INTO DataSet2 (kod, vrednost, dateTime) VALUES(?,?,?)",(x.HistoricalCollection[-counter].code,x.HistoricalCollection[-counter].value, datetime.now()))
                        conn.commit()
                        print("Kod uspesno upisan u bazu.")
                    else:
                        print("Kod ne ispunjava deadband uslov.")
            if x.HistoricalCollection[-counter].code=="CODE_SINGLENOE" or x.HistoricalCollection[-counter].code=="CODE_MULTIPLENODE":
                    prosao = deadband(x.HistoricalCollection[-counter].code,x.HistoricalCollection[-counter].value)
                    if prosao:
                        c.execute("INSERT INTO DataSet3 (kod, vrednost, dateTime) VALUES(?,?,?)",(x.HistoricalCollection[-counter].code,x.HistoricalCollection[-counter].value, datetime.now()))
                        conn.commit()
                        print("Kod uspesno upisan u bazu.")
                    else:
                        print("Kod ne ispunjava deadband uslov.")
            if x.HistoricalCollection[-counter].code=="CODE_CONSUMER" or x.HistoricalCollection[-counter].code=="CODE_SOURCE":
                    prosao = deadband(x.HistoricalCollection[-counter].code,x.HistoricalCollection[-counter].value)
                    if prosao:
                        c.execute("INSERT INTO DataSet4 (kod, vrednost, dateTime) VALUES(?,?,?)",(x.HistoricalCollection[-counter].code,x.HistoricalCollection[-counter].value, datetime.now()))
                        conn.commit()
                        print("Kod uspesno upisan u bazu.")
                    else:
                        print("Kod ne ispunjava deadband uslov.")

            
            counter-=1
        print("=======================================================")    

       
        new_msg = True
        full_msg = b''


