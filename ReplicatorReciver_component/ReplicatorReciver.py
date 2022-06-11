import socket
import pickle

HEADERSIZE = 10
#TCP Konekcija sa ReplicatorSenderom
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1236))
#TCP Konekcija sa Readerom
s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.bind((socket.gethostname(),1237))
s1.listen(4)

while True:
    full_msg = b''
    new_msg = True

    clientsocket, adress = s1.accept()
    print(f"Connection from {adress} has been established")

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