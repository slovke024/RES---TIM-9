import socket
import time
import pickle
import random
from klase import Logger


loger=Logger()

class CodeValue:
  def __init__(self, code, value):
    self.code = code
    self.value = value

codes = ["CODE_ANALOG","CODE_DIGITAL","CODE_CUSTOM","CODE_LIMITSET","CODE_SINGLENOE","CODE_MULTIPLENODE","CODE_CONSUMER","CODE_SOURCE"]

HEADERSIZE = 10

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1235))
s.listen()



clientsocket, adress = s.accept()
print(f"Connection from {adress} has been established")
loger.upisiLog("Writer:Konekcija uspostavljena sa ReplicatorSender komponentom.")


while True:
        time.sleep(1)
        p1 = CodeValue(codes[random.randint(0,7)],random.randint(0,100))
        msg1 = [p1.code,p1.value]
        msg = pickle.dumps(msg1)

        msg = bytes(f'{len(msg):<{HEADERSIZE}}',"utf-8") + msg

        clientsocket.send(msg)
        loger.upisiLog("Writer:Poruka prosledjena ReplicatorSender komponenti.")
