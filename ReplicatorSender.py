import socket
import pickle

HEADERSIZE = 10
#TCP Konekcija sa Writerom
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1235))

#TCP Konekcija sa ReplicatorReciverom
s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.bind((socket.gethostname(),1236))
s1.listen()


#Petlja za prijem poruka od Writer komponente

full_msg = b''
new_msg = True

clientsocket, adress = s1.accept()
print(f"Connection from {adress} has been established")

lista = list()
brojac=-1

while True:
        msg = s.recv(16)
        if new_msg:
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg) - HEADERSIZE == msglen:

            p1 = pickle.loads(full_msg[HEADERSIZE:])
            print(p1)
            lista.append(p1)
            brojac+=1
            
            
            #Slanje poruke ReplicatorReciveru
            msg = pickle.dumps(lista[brojac])
            msg = bytes(f'{len(msg):<{HEADERSIZE}}',"utf-8") + msg
            clientsocket.send(msg)
            lista.pop(brojac)
            brojac-=1
            new_msg = True
            full_msg = b''
            

