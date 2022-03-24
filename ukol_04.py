class Auto:
    def __init__(self,rz,znacka_typ,najete_km):
        self.rz=rz
        self.znacka_typ=znacka_typ
        self.najete_km=najete_km
        self.auto_volne=True

    def pujc_auto(self):
        if self.auto_volne==True:
            self.auto_volne=False
            return "Potvrzuji zapůjčení vozidla!"
        else:
            return "Vozidlo není k dispozici"
    def get_info(self):
        
        if self.auto_volne==True:
            return f"Vozidlo {self.znacka_typ} s registrační značkou {self.rz} má najeto {self.najete_km} km."
        else:
            return f"Vozidlo {self.znacka_typ} s registrační značkou {self.rz} má najeto {self.najete_km} km."

peugeot=Auto('4A2 3020','Peugeot 403 Cabrio',47534)
skoda=Auto('1P3 4747','Škoda Octavia',	41253)

vyber_auto=input('Zadej si auto, které chceš půjčit Peugeot nebo Škoda: ')

if vyber_auto=='Peugeot':
    print(peugeot.get_info())
    print(peugeot.pujc_auto())
elif vyber_auto=='Škoda':
    print(skoda.get_info())
    print(skoda.pujc_auto())
else:
    print('Toto auto nemáme v nabídce!')

vyber_auto=input('Zadej si auto, které chceš půjčit Peugeot nebo Škoda: ')

if vyber_auto=='Peugeot':
    print(peugeot.get_info())
    print(peugeot.pujc_auto())
elif vyber_auto=='Škoda':
    print(skoda.get_info())
    print(skoda.pujc_auto())
else:
    print('Toto auto nemáme v nabídce!')