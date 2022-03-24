""" Uvažuj, že navrhuješ software pro zásilkovou společnost.

Vytvoř třídu Balik, která bude mít tři atributy - adresa, hmotnost a doruceno. První dva atributy nastav pomocí parametrů funkce __init__. Parametr doruceno nastav na začátku jako False.
Připoj ke třídě funkci deliver, která změní hodnotu parametru doruceno na True.
Přidej metodu __str__, která vypíše adresu, hmotnost a informaci o tom, zda byl balík již doručen.
Zkus si vytvořit nějaké objekty ze třídy Balik a ověř, že vše funguje. """


class Balik:

    def __init__(self,adresa,hmotnost):
        self.adresa = adresa 
        self.hmotnost=hmotnost
        self.doruceno=False

    def deliver(self):
        self.doruceno=True

    def __str__(self):
        if self.doruceno==True:
            return f"Balík o hmotnosti {self.hmotnost} byl doručen na adresu {self.adresa}"
        else:
            return f"Balík nebyl doručen na adresu {self.adresa}!"

praha=Balik('Václavské náměstí, Praha','25kg')
print(praha)
praha.deliver()
print(praha)



""" Zkus pro našeho nakladatele vytvořit software s využitím tříd a objektů. Vytvoř tedy třídu Kniha, která reprezentuje knihu. Každá kniha bude mít atributy nazev, pocet_stran a cena. Hodnoty nastav ve funkci __init__.

Přidej knize funkci __str__, která vypíše informace o knize v nějakém pěkném formátu.
Občas se stane, že se kniha moc neprodává a knihkupec se snaží nalákat kupující slevou. Přidej metodu sleva(), která bude mít jeden parametr - velikost slevy v procentech. Funkce sníží cenu knihy o dané procento. """

class Kniha:
    def __init__(self,nazev,pocet_stran,cena):
        self.nazev=nazev
        self.pocet_stran=pocet_stran
        self.cena=cena

    def __str__(self):
        return f"Kniha {self.nazev} má {self.pocet_stran} počet stran a prodává se za {self.cena} Kč."

    def sleva(self,procenta):
        self.procenta=procenta
        self.cena = self.cena - (self.cena*(self.procenta/100))

harryPoter1=Kniha('Harry Poter', 250, 300)
print(harryPoter1)
harryPoter1.sleva(15)
print(harryPoter1)

""" U zaměstnanců budeme nově evidovat, jestli jsou ve zkušební době.

Rozšiř metodu __init__ třídy Zamestnanec o parametr zkusebni_doba, který bude typu bool. Tuto hodnotu ulož jako atribut třídy Zamestnanec.
Uprav metodu __str__. Pokud je zaměstnanec ve zkušební době, přidej k jeho/jejímu výpisu text Je ve zkušební době. """

class Zamestnanec:
    def __init__(self, jmeno, pozice):  # zavola se pokazde kdyz vytvarime novy objekt (constructor)
        self.jmeno = jmeno  # vlastnost, atribut
        self.pozice= pozice

        self.zkusebni_doba=True

    def po_zkusebni_dobe(self):
        self.zkusebni_doba=False

    def __str__(self):  # metoda tridy
        if self.zkusebni_doba==True:
            return f"Zamestnanec se jmenuje {self.jmeno} a pracuje na pozici {self.pozice} je ve zkušební době."
        else:
            return f"Zamestnanec se jmenuje {self.jmeno} a pracuje na pozici {self.pozice} neni ve zkušební době."

# vytvarime objekt
frantisek = Zamestnanec('Frantisek Novak', 'konstrukter')
print(frantisek)
frantisek.po_zkusebni_dobe()
print(frantisek)