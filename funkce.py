""" #definice funkce
def greet_user():
  print("Ahoj!")
#volání funkce
greet_user()

def greet_user(name):
  print(f"Ahoj {name}!")
greet_user("Jirko") """

#Napiš funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek.
from random import randint


def mult(x,y):
    return x*y

print(mult(2,2))

#Napiš funkci total_price, která vypočte cenu noci v hotelu. Funkce bude mít dva parametry - persons a breakfast. Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč. Funkce vrátí výslednou cenu. Parametr breakfast je nepovinný a výchozí hodnota je False.

#Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. total_price(3), total_price(2, True).

def total_price(person: int, breakfast:bool=False):
    if breakfast == True:
        return (person*(850+125))
    else:
        return (person*850)

print(total_price(3))
print(total_price(3,True))

#Napiš funkci month_of_birth, která bude mít jeden parametr - rodné číslo. Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup. Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.

#Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5.

""" def month_of_birth(rodne_cislo):
    if rodne_cislo[2]=='0':
        return rodne_cislo[3]
    elif rodne_cislo[2]=='5':
        return rodne_cislo[3]
    elif rodne_cislo[2]=='6':
        return (str(int(rodne_cislo[2])-5))+rodne_cislo[3]
    else:
        return rodne_cislo[2]+rodne_cislo[3]

rodneCislo=input('Zadej své rodné číslo bez lomítka: ')
print(month_of_birth(str(rodneCislo))) """

#Vytvoř funkci roulette, která bude mít parametry číslo řady a výši sázky. Pomocí funkce randint z modulu random vygeneruj náhodné číslo v rozsahu od 0 (včetně) do 36. Vyhodnoť, do které řady číslo náleží. Nezapomeň, že 0 nepatří do žádné z řad a pokud padne, uživatel vždy prohrává.

def roulette(rada,sazka):
    if rada == 1:
        return 2*sazka
    elif rada == 2:
        return 2*sazka
    elif rada == 3:
        return 2*sazka

rada=input("zadej číslo řady:")
sazka=input("zadej výši sázky: ")
vitezneCislo=randint(0,9)
print(f"Vítězné číslo je: {vitezneCislo}")
prvni=[1,4,7]
druha=[2,5,8]
treti=[3,6,9]

for cislo in prvni:
    if vitezneCislo==prvni:
        print(roulette(1,sazka))
for cislo in druha:
    if vitezneCislo=="druha":
        print(roulette(1,sazka))
for cislo in treti:
    if vitezneCislo=="treti":
        print(roulette(1,sazka))


