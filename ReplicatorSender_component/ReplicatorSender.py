import socket
import pickle

HEADERSIZE = 10
#TCP Konekcija
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1235))

#Petlja za prijem poruka od Writer komponente
while True:
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
            new_msg = True
            full_msg = b''