from asyncio.log import logger
import socket
import pickle
from klase import DeltaCD, RecieverProperty,CollectionDescription,Logger


LoggerPoruka="ReplicatorReciver:Formatiranje poruke za slanje Reader komponenti."
historicalCollection=[]
listAdd=[]
listUpdate=[]
loger=Logger()
bool1=True
bool2=True
bool3=True
bool4=True

def pakovanje(p1):
    global bool1
    global bool2
    global bool3
    global bool4

    if p1[0]=="CODE_ANALOG" or p1[0]=="CODE_DIGITAL":
                loger.upisiLog(LoggerPoruka)
                rc=RecieverProperty(p1[0],p1[1])
                historicalCollection.append(rc)
                cd=CollectionDescription(1,0,historicalCollection)
                if bool1:
                    listAdd.append(cd)
                    bool1=not(bool1)
                else:
                    listUpdate.append(cd)
           
    if p1[0]=="CODE_CUSTOM" or p1[0]=="CODE_LIMITSET":
                loger.upisiLog(LoggerPoruka)
                rc=RecieverProperty(p1[0],p1[1])
                historicalCollection.append(rc)
                cd=CollectionDescription(2,1,historicalCollection)
                if bool2:
                    listAdd.append(cd)
                    bool2=not(bool2)
                else:
                    listUpdate.append(cd)
                                            
    if p1[0]=="CODE_SINGLENOE" or p1[0]=="CODE_MULTIPLENODE":
                loger.upisiLog(LoggerPoruka)
                rc=RecieverProperty(p1[0],p1[1])
                historicalCollection.append(rc)
                cd=CollectionDescription(3,2,historicalCollection)
                if bool3:
                    listAdd.append(cd)
                    bool3=not(bool3)
                else:
                    listUpdate.append(cd)
              
    if p1[0]=="CODE_CONSUMER" or p1[0]=="CODE_SOURCE":
                loger.upisiLog(LoggerPoruka)
                rc=RecieverProperty(p1[0],p1[1])
                historicalCollection.append(rc)
                cd=CollectionDescription(4,3,historicalCollection)
                if bool4:
                    listAdd.append(cd)
                    bool4=not(bool4)
                else:
                    listUpdate.append(cd)
    
    return True

def main():
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
    loger.upisiLog("ReplicatorReciver:Konekcija uspostavljena sa Reader komponentom.")


                    
                        
                            

    while True:
            msg = s.recv(16)
            
            if new_msg:
                msglen = int(msg[:HEADERSIZE])
                new_msg = False

            full_msg += msg

            if len(full_msg) - HEADERSIZE == msglen:

                p1 = pickle.loads(full_msg[HEADERSIZE:])
                loger.upisiLog("ReplicatorReciver:Primljena poruka od ReplicatorSender komponente.")
                print(p1)
                pakovanje(p1)
                
                if len(listAdd)+len(listUpdate)==10:
                    deltacd=DeltaCD()
                    deltacd.add=listAdd
                    deltacd.update=listUpdate
                    lista=deltacd.update+deltacd.add
                    
                    msg = pickle.dumps(lista)
                    msg = bytes(f'{len(msg):<{HEADERSIZE}}',"utf-8") + msg
                    clientsocket.send(msg)
                    loger.upisiLog("ReplicatorReciver:Poslat DeltaCD Reader komponenti.")
                    listAdd.clear()
                    listUpdate.clear()

                new_msg = True
                full_msg = b''    

if __name__ == '__main__':
    main()
                