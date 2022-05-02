from datetime import datetime
datum_prijezdu= input("Zadej datum příjezdu ve formátu dd.mm.rrrr: ")
pocet_osob=input("Zadej počet osob: ")
prijezd=datetime.strptime(datum_prijezdu,"%d.%m.%Y")

if prijezd>=datetime(2021,7,1) and prijezd<=datetime(2021,8,10):
    print (f"Cena vstupenek za {pocet_osob} osob dne {datum_prijezdu} je : {int(pocet_osob)*250}")
elif prijezd>=datetime(2021,8,11) and prijezd<=datetime(2021,8,31):
    print (f"Cena vstupenek za {pocet_osob} osob dne {datum_prijezdu} je : {int(pocet_osob)*180}")
else:
    print("Příjezd je mimo pracovní dobu")
