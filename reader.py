import socket
import pickle
import sqlite3
from klase import DeltaCD, RecieverProperty,CollectionDescription

HEADERSIZE = 10                                             # Velicina headera u primljenoj poruci

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       # TCP Konekcija
s.connect((socket.gethostname(),1237))


conn = sqlite3.connect('test_database.db')                     # Pravljenje sqlite3 test baze
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS DataSet1
          (kod TEXT, vrednost INTEGER)
          ''')
                    
conn.commit()
c.execute('''
          CREATE TABLE IF NOT EXISTS DataSet2
          (kod TEXT, vrednost INTEGER)
          ''')
                    
conn.commit()
c.execute('''
          CREATE TABLE IF NOT EXISTS DataSet3
          (kod TEXT, vrednost INTEGER)
          ''')
                    
conn.commit()
c.execute('''
          CREATE TABLE IF NOT EXISTS DataSet4
          (kod TEXT, vrednost INTEGER)
          ''')
                    
conn.commit()


p1=DeltaCD
listAdd=list()
listUpdate=list()
rc=RecieverProperty
      
                                               # Petlja za primanje i ispis poruka
full_msg = b''
new_msg = True
while True:
    msg = s.recv(16)
        
    conn = sqlite3.connect('test_database.db')
    c = conn.cursor()
          
    p1 = pickle.load(msg)
    
    listAdd=p1[0]
    listUpdate=p1[1]
    print(listAdd)
    print(listUpdate)
            
            

    if p1[0]=="CODE_ANALOG" or p1[0]=="CODE_DIGITAL":
                c.execute("INSERT INTO DataSet1 (kod, vrednost) VALUES(?,?)",(p1[0],p1[1]))
                conn.commit()
    if p1[0]=="CODE_CUSTOM" or p1[0]=="CODE_LIMITSET":
                c.execute("INSERT INTO DataSet2 (kod, vrednost) VALUES(?,?)",(p1[0],p1[1]))
                conn.commit()
    if p1[0]=="CODE_SINGLENOE" or p1[0]=="CODE_MULTIPLENODE":
                c.execute("INSERT INTO DataSet3 (kod, vrednost) VALUES(?,?)",(p1[0],p1[1]))
                conn.commit()
    if p1[0]=="CODE_CONSUMER" or p1[0]=="CODE_SOURCE":
                c.execute("INSERT INTO DataSet4 (kod, vrednost) VALUES(?,?)",(p1[0],p1[1]))
                conn.commit()

    print("Kod uspesno smesten u bazu podataka")
    new_msg = True
    full_msg = b''


