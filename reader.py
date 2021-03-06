import socket
import pickle
import sqlite3
from datetime import datetime
from klase import Reader,Logger



listaKodova=list()

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
    
    
    if code in listaKodova:
        c.execute(F"SELECT vrednost FROM {dataset} WHERE kod='{code}' AND dateTime=(SELECT MAX(dateTime) FROM {dataset} WHERE kod='{code}')")
    else:
        return True
    
    latestValue=c.fetchall()
    broj=latestValue[0]
    limit = float(broj[0])*0.02

    if code !="CODE_DIGITAL":
        if value>=broj[0]-limit and value<= broj[0]+limit:
            db_prosao=False

    return db_prosao


def Main():
    loger=Logger()
    
    HEADERSIZE = 10                                             # Velicina headera u primljenoj poruci

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       # TCP Konekcija
    s.connect((socket.gethostname(),1237))
    loger.upisiLog("Reader:Uspostavljena konekcija sa ReplicatorReciver komponentom.")

    #sClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)      # Konekcija sa Client
    #sClient.connect((socket.gethostname(),1239))



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
    loger.upisiLog("Reader:Uspesno kreirane tabele baze podataka.")

    reader1=Reader("DataSet1")
    reader2=Reader("DataSet2")
    reader3=Reader("DataSet3")
    reader4=Reader("DataSet4")

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
            loger.upisiLog("Reader:Uspesno prihvacen DeltaCD od ReplicatorReciver komponente.")
            print("=======================================================")
            for x in lista:
                print(F"{x.historical_collection[-counter].code} {x.historical_collection[-counter].value}")

                if x.historical_collection[-counter].code=="CODE_ANALOG" or x.historical_collection[-counter].code=="CODE_DIGITAL":
                        loger.upisiLog("Reader1:Provera Deadbanda.")
                        prosao = deadband(x.historical_collection[-counter].code,x.historical_collection[-counter].value)
                        if prosao:
                            reader1.upisiUBazu(x.historical_collection[-counter].code,x.historical_collection[-counter].value)
                            if x.historical_collection[-counter].code not in listaKodova:
                                listaKodova.append(x.historical_collection[-counter].code)
                            loger.upisiLog("Reader1:Kod uspesno upisan u bazu.")
                        else:
                            loger.upisiLog("Reader1:Kod nije upisan u bazu zbog Deadbanda.")
                if x.historical_collection[-counter].code=="CODE_CUSTOM" or x.historical_collection[-counter].code=="CODE_LIMITSET":
                        loger.upisiLog("Reader2:Provera Deadbanda.")
                        prosao = deadband(x.historical_collection[-counter].code,x.historical_collection[-counter].value)
                        if prosao:
                            reader2.upisiUBazu(x.historical_collection[-counter].code,x.historical_collection[-counter].value)
                            if x.historical_collection[-counter].code not in listaKodova:
                                listaKodova.append(x.historical_collection[-counter].code)
                            loger.upisiLog("Reader2:Kod uspesno upisan u bazu.")
                        else:
                            loger.upisiLog("Reader2:Kod nije upisan u bazu zbog Deadbanda.")
                if x.historical_collection[-counter].code=="CODE_SINGLENOE" or x.historical_collection[-counter].code=="CODE_MULTIPLENODE":
                        loger.upisiLog("Reader3:Provera Deadbanda.")
                        prosao = deadband(x.historical_collection[-counter].code,x.historical_collection[-counter].value)
                        if prosao:
                            reader3.upisiUBazu(x.historical_collection[-counter].code,x.historical_collection[-counter].value)
                            if x.historical_collection[-counter].code not in listaKodova:
                                listaKodova.append(x.historical_collection[-counter].code)
                            loger.upisiLog("Reader3:Kod uspesno upisan u bazu.")
                        else:
                            loger.upisiLog("Reader3:Kod nije upisan u bazu zbog Deadbanda.")
                if x.historical_collection[-counter].code=="CODE_CONSUMER" or x.historical_collection[-counter].code=="CODE_SOURCE":
                        loger.upisiLog("Reader4:Provera Deadbanda.")
                        prosao = deadband(x.historical_collection[-counter].code,x.historical_collection[-counter].value)
                        if prosao:
                            reader4.upisiUBazu(x.historical_collection[-counter].code,x.historical_collection[-counter].value)
                            if x.historical_collection[-counter].code not in listaKodova:
                                listaKodova.append(x.historical_collection[-counter].code)
                            loger.upisiLog("Reader4:Kod uspesno upisan u bazu.")
                        else:
                            loger.upisiLog("Reader4:Kod nije upisan u bazu zbog Deadbanda.")

                
                counter-=1
            print("=======================================================")    

        
            new_msg = True
            full_msg = b''

if __name__ == '__main__':
    Main()
