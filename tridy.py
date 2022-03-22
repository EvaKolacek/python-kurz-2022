zamestnanci = {
    '1': {'pozice': 'konstrukter', 'jmeno': 'Frantisek Novak'},
    '2': {'pozice': 'vedouci', 'jmeno': 'Klara Nova'},
}

cislo_zamestnance = '1'
zamestnanec = zamestnanci[cislo_zamestnance]

print(f"Zamestnanec {zamestnanec['jmeno']} pracuje na pozici {zamestnanec['pozice']}.")

# trida
class Zamestnanec:
    def vypis_jmeno(self):  # metoda tridy
        return f"Zamestnanec se jmenuje {self.jmeno}."


# vytvarime objekt
frantisek = Zamestnanec()
frantisek.jmeno = 'Frantisek Novak'  # vlastnost, atribut
print(frantisek.vypis_jmeno())


class Zamestnanec:
    def __init__(self, jmeno, pozice=None):  # zavola se pokazde kdyz vytvarime novy objekt (constructor)
        self.jmeno = jmeno  # vlastnost, atribut
        if pozice is None:
            self.pozice = "uklizecka"
        else:
            self.pozice = pozice

    def vypis_jmeno(self):  # metoda tridy
        return f"Zamestnanec se jmenuje {self.jmeno} a pracuje na pozici {self.pozice}."


# vytvarime objekt
frantisek = Zamestnanec('Frantisek Novak', 'konstrukter')  # zavola se metoda __init__()
print(frantisek.vypis_jmeno())

class Zamestnanec:
    def __init__(self, jmeno, pozice=None):  # zavola se pokazde kdyz vytvarime novy objekt (constructor)
        self.jmeno = jmeno  # vlastnost, atribut
        if pozice is None:
            self.pozice = "uklizecka"
        else:
            self.pozice = pozice
        self.pocet_dni_dovolene = 30

    def vypis_jmeno(self):  # metoda tridy
        return f"Zamestnanec se jmenuje {self.jmeno} a pracuje na pozici {self.pozice}."

    def cerpej_dovolenou(self, pocet_dni):
        if self.pocet_dni_dovolene >= pocet_dni:  # mam narok na dost dovolene
            self.pocet_dni_dovolene -= pocet_dni
            # self.pocet_dni_dovolene = self.pocet_dni_dovolene - pocet_dni
            print(f"Prejeme peknou dovolenou. Zbyva vam {self.pocet_dni_dovolene} dni dovolene")
        else:
            print(f"Nemate dost dovolene, maximalne muzete cerpat {self.pocet_dni_dovolene} dni dovolene.")

# vytvarime objekt
frantisek = Zamestnanec('Frantisek Novak', 'konstrukter')  # zavola se metoda __init__()
frantisek.cerpej_dovolenou(10)
frantisek.cerpej_dovolenou(30)
frantisek.cerpej_dovolenou(20)

class Zamestnanec:
    def __init__(self, jmeno, pozice=None):  # zavola se pokazde kdyz vytvarime novy objekt (constructor)
        self.jmeno = jmeno  # vlastnost, atribut
        if pozice is None:
            self.pozice = "uklizecka"
        else:
            self.pozice = pozice
        self.pocet_dni_dovolene = 30

    def __str__(self):
        return f"Zamestnanec se jmenuje {self.jmeno} a pracuje na pozici {self.pozice}."

