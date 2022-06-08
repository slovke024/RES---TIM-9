import socket
import pickle
import sqlite3



HEADERSIZE = 10                                             # Velicina headera u primljenoj poruci

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       # TCP Konekcija
s.connect((socket.gethostname(),1235))

conn = sqlite3.connect('test_database')                     # Pravljenje sqlite3 test baze
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS kodovi
          (kod TEXT, vrednost INTEGER)
          ''')
                    
conn.commit()



while True:                                                 # Petlja za primanje i ispis poruka
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg) - HEADERSIZE == msglen:

            p1 = pickle.loads(full_msg[HEADERSIZE:])
            print(p1)
            
            c.execute("INSERT INTO kodovi (kod, vrednost) VALUES(?,?)",(p1[0],p1[1]))
            
            conn.commit

            c.execute('''
            SELECT
            kod,
            vrednost
            FROM kodovi
            ''')

            
            print (c.fetchall())
            
            print("Kod uspesno smesten u bazu podataka")
            new_msg = True
            full_msg = b''