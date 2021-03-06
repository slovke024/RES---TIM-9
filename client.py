from klase import Reader
import os


codes = ["CODE_ANALOG","CODE_DIGITAL","CODE_CUSTOM","CODE_LIMITSET","CODE_SINGLENOE","CODE_MULTIPLENODE","CODE_CONSUMER","CODE_SOURCE"]


def provera_koda(x):
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

def poslednja_vrednost():
        kod=""
        lista=list()
        while kod!="x":
            print("Unosite kodove, unesite x za prekid unosa")
            kod=input()
            while kod not in codes:
                if kod=="x":
                    break
                print("UNESITE VALIDNU VREDNOST KODA")
                kod=input()
                
            if kod!="x":
                lista.append(kod)
            
        for x in lista:
            provera_koda(x)

           
        return True

def vremenski_interval():
        print("Unesite kod")
        vrednost=input()
        while vrednost not in codes:
            print("UNESITE VALIDNU VREDNOST KODA")
            vrednost=input()
        print("Unesite prvi vremenski interval u formatu YYYY-MM-DD HH:MM:SS")
        vremenski_interval1=input()
        print("Unesite drugi vremenski interval u formatu HH:MM:SS")
        vremenski_interval2=input()
        if vrednost=="CODE_ANALOG" or vrednost=="CODE_DIGITAL":
            reader1=Reader("DataSet1")
            reader1.vremenskiInterval(vrednost,vremenski_interval1,vremenski_interval2)
        if vrednost=="CODE_CUSTOM" or vrednost=="CODE_LIMITSET":
            reader2=Reader("DataSet2")
            reader2.vremenskiInterval(vrednost,vremenski_interval1,vremenski_interval2)
        if vrednost=="CODE_SINGLENOE" or vrednost=="CODE_MULTIPLENODE":
            reader3=Reader("DataSet3")
            reader3.vremenskiInterval(vrednost,vremenski_interval1,vremenski_interval2)
        if vrednost=="CODE_CONSUMER" or vrednost=="CODE_SOURCE":
            reader4=Reader("DataSet4")
            reader4.vremenskiInterval(vrednost,vremenski_interval1,vremenski_interval2)
        return True


def main():
    print("UNESITE BROJ KOJI ZELITE DA POZOVETE")
    print("1.Unesite kod za koji zelite da iscitate poslednju vrednost iz baze podataka")
    print("2.Unesite kod i vremenski interval za koji zelite da iscitate kodove iz baze podataka")
    while True:
        broj=input()
        while broj!='1' and broj!='2':
            print("POGRESAN UNOS, POKUSAJTE PONOVO")
            broj=input()

        if broj=='1':
            poslednja_vrednost()
        
        if broj=="2":
            vremenski_interval()
        
        print("Sledeci upis")

if __name__ == '__main__':
    main()