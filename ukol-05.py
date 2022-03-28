""" Uvažuj, že vyvíjíš software pro službu, která nabízí streamování videa. Služba nabízí dva typy pořadů - filmy a seriály. Firma chce evidovat, které filmy a seriály nabízí a jejich žánry. Dále chce u filmů evidovat délku a u seriálů počet episod a délku jedné episody.

Vytvoř program, který bude obsahovat tři třídy - Polozka, Film a Serial.
Třída Polozka bude sloužit jako základ pro další třídy. Bude mít atributy určující název a žánr. Oba atributy nastav ve funkci __init__, žánr získej jako parametr funkce.
Třída Film bude potomkem třídy Polozka. Film má kromě názvu a žánru atribut délka.
Třída Serial bude potomkem třídy Polozka. Má kromě názvu a žánru atributy počet epizod a délka epizody.
Všem třídám přidej funkci get_info, která vypíše informace o položce, resp. o filmu a seriálu. Funkce u třídy Polozka vypíše název a žánr. Následně tuto funkci využij ve funkcích u tříd Film a Serial a přidej k ní informaci o délce, resp. počtu episod.
Po naprogramování si vytvoř alespoň jeden objekt reprezentující film a seriál a ověř, že vše funguje. """

class Polozka:
    def __init__(self,nazev,zanr):
        self.nazev=nazev
        self.zanr=zanr
    def __str__(self):
        return f"Název: {self.nazev}, Žánr: {self.zanr}"

class Film(Polozka):
    def __init__(self, nazev, zanr,delka):
        super().__init__(nazev, zanr)
        self.delka=delka
    def __str__(self):
        return "Film: " + super().__str__() + f", délka filmu: {self.delka} min"

class Serial(Polozka):
    def __init__(self, nazev, zanr,pocet_epizod,delka_epizody):
        super().__init__(nazev, zanr)
        self.pocet_epizod=pocet_epizod
        self.delka_epizody=delka_epizody
    def __str__(self):
        return "Seriál" + super().__str__() + f", počet epizod: {self.pocet_epizod}, délka epizody: {self.delka_epizody} min"

babovky=Film("Bábovky","Romantický / Drama / Komedie",97)
print(babovky)
koruna=Serial("Koruna","Drama / Historický",10,"47–62")
print(koruna)