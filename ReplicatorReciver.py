import socket
import pickle
from klase import DeltaCD, RecieverProperty,CollectionDescription

     

cd1=CollectionDescription(1,0)
cd2=CollectionDescription(2,1)
cd3=CollectionDescription(3,2)
cd4=CollectionDescription(4,3)
hl1=list()
hl2=list()
hl3=list()
hl4=list()
bool1=True
bool2=True
bool3=True
bool4=True
listaAdd=list()
listaUpdate=list()
listaPomocna=list()
deltacd=DeltaCD


HEADERSIZE = 10
#TCP Konekcija sa ReplicatorSenderom
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1236))

#TCP Konekcija sa Readerom
s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.bind((socket.gethostname(),1237))
s1.listen()



full_msg = b''
new_msg = True

clientsocket, adress = s1.accept()
print(f"Connection from {adress} has been established")

def pakovanje(p1):
    if p1[0]=="CODE_ANALOG" or p1[0]=="CODE_DIGITAL":
                rc=RecieverProperty(p1[0],p1[1])
                hl1.append(rc)
                cd1.HistoricalCollection=hl1
                if bool1:
                    listaAdd.append(cd1)
                    deltacd.add=listaAdd
                else:
                    listaUpdate.append(cd1)
                    deltacd.update=listaUpdate
    if p1[0]=="CODE_CUSTOM" or p1[0]=="CODE_LIMITSET":
                rc=RecieverProperty(p1[0],p1[1])
                hl2.append(rc)
                cd2.HistoricalCollection=hl2
                if bool2:
                    listaAdd.append(cd2)
                    deltacd.add=listaAdd
                else:
                    listaUpdate.append(cd2)
                    deltacd.update=listaUpdate              
    if p1[0]=="CODE_SINGLENOE" or p1[0]=="CODE_MULTIPLENODE":
                rc=RecieverProperty(p1[0],p1[1])
                hl3.append(rc)
                cd3.HistoricalCollection=hl3
                if bool3:
                    listaAdd.append(cd3)
                    deltacd.add=listaAdd
                else:
                    listaUpdate.append(cd3)
                    deltacd.update=listaUpdate                
    if p1[0]=="CODE_CONSUMER" or p1[0]=="CODE_SOURCE":
                rc=RecieverProperty(p1[0],p1[1])
                hl4.append(rc)
                cd4.HistoricalCollection=hl4
                if bool4:
                    listaAdd.append(cd4)
                    deltacd.add=listaAdd
                else:
                    listaUpdate.append(cd4)
                    deltacd.update=listaUpdate                

while True:
        msg = s.recv(16)
        
        if new_msg:
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg) - HEADERSIZE == msglen:

            p1 = pickle.loads(full_msg[HEADERSIZE:])
            print(p1)
            pakovanje(p1)
            if len(listaAdd)+len(listaUpdate)==10:
                msg = pickle.dumps(deltacd)
                msg = bytes(f'{len(msg):<{HEADERSIZE}}',"utf-8") + msg
                clientsocket.send(msg)
                listaAdd.clear()
                listaUpdate.clear()

            new_msg = True
            full_msg = b''    
            