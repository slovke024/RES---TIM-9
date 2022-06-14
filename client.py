from csv import reader
import socket
import time
import pickle
from klase import Reader




print("UNESITE BROJ KOJI ZELITE DA POZOVETE")
print("1.Unesite kod za koji zelite da iscitate poslednju vrednost iz baze podataka")
print("2.Unesite kod i vremenski interval za koji zelite da iscitate kodove iz baze podataka")
while True:
    broj=input()
    if broj=='1':
        kod=""
        lista=list()
        while(kod!="x"):
            print("Unosite kodove, unesite x za prekid unosa")
            kod=input()
            if(kod!="x"):
                lista.append(kod)
            
        for x in lista:
            if (x=="CODE_ANALOG" or x=="CODE_DIGITAL"):
                reader1=Reader("DataSet1")
                reader1.poslednjaVrednost(x)
            if (x=="CODE_CUSTOM" or x=="CODE_LIMITSET"):
                reader2=Reader("DataSet2")
                reader2.poslednjaVrednost(x)
            if (x=="CODE_SINGLENOE" or x=="CODE_MULTIPLENODE"):
                reader3=Reader("DataSet3")
                reader3.poslednjaVrednost(x)
            if (x=="CODE_CONSUMER" or x=="CODE_SOURCE"):
                reader4=Reader("DataSet4")
                reader4.poslednjaVrednost(x)
    
    if broj=="2":
        print("Unesite kod")
        vrednost=input()
        print("Unesite prvi vremenski interval u formatu YYYY-MM-DD HH:MM:SS")
        vremenskiInterval1=input()
        print("Unesite drugi vremenski interval u formatu HH:MM:SS")
        vremenskiInterval2=input()
        if vrednost=="CODE_ANALOG" or vrednost=="CODE_DIGITAL":
            reader1=Reader("DataSet1")
            reader1.vremenskiInterval(vrednost,vremenskiInterval1,vremenskiInterval2)
        if vrednost=="CODE_CUSTOM" or vrednost=="CODE_LIMITSET":
            reader2=Reader("DataSet2")
            reader2.vremenskiInterval(vrednost,vremenskiInterval1,vremenskiInterval2)
        if vrednost=="CODE_SINGLENOE" or vrednost=="CODE_MULTIPLENODE":
            reader3=Reader("DataSet3")
            reader3.vremenskiInterval(vrednost,vremenskiInterval1,vremenskiInterval2)
        if vrednost=="CODE_CONSUMER" or vrednost=="CODE_SOURCE":
            reader4=Reader("DataSet4")
            reader4.vremenskiInterval(vrednost,vremenskiInterval1,vremenskiInterval2)
    
    print("Sledeci upis")