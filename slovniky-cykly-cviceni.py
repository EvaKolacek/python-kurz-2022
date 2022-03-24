""" #Napiš program, který spočte průměrnou známku ze všech předmětů.
#Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.

school_report = {
  "Český jazyk": 1,
  "Anglický jazyk": 1,
  "Matematika": 1,
  "Přírodopis": 2,
  "Dějepis": 1,
  "Fyzika": 2,
  "Hudební výchova": 4,
  "Výtvarná výchova": 2,
  "Tělesná výchova": 3,
  "Chemie": 4,
}

index = 0
pocet_predmetu = len(school_report)

for predmet,znamka in school_report.items():
    if znamka==1:
        print(predmet)

for znamka in school_report:
    index+=school_report[znamka]
print (f'Průměr všech známek je: {index/pocet_predmetu}') """

#Napiš program, který spočte celkový počet stran, které Gustav přečetl.
#Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.
books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

index = 0

for book in books:
    index+=book['pages']
print (index)

i=0
for book in books:
    if book['rating']>=8:
        i+=1
print(i)

#V následujícím slovníků je evidence automobilů. Klíčem jsou státní poznávací značky (SPZ) a hodnotou je jméno majitele vozu. Napiš program, který vypíše všechny majitele, jejichž vozidlo je registrováno v Plzeňském kraji, tj. na druhém místě (index 1!) řetězce v klíči je písmeno P.

plates = {"4A2 3000": "František Novák",
  "6P5 4747": "Jana Pilná",
  "3B7 3652": "Jaroslav Sečkár",
  "1P5 5269": "Marta Nováková",
  "37E 1252": "Martina Matušková",
  "2A5 2241": "Jan Král"}

for spz, jmeno in plates.items():
    if spz[1]=='P':
        print (jmeno)

# maturita
vysledky = [
  {"Jméno": "Mirek Dušín", "Český jazyk": 1, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 1, "Zeměpis": 1},
  {"Jméno": "Jarka Metelka", "Český jazyk": 3, "Anglický jazyk": 1, "Matematika": 3, "Dějepis": 2, "Ekonomika": 5},
  {"Jméno": "Jindra Hojer", "Český jazyk": 2, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 3, "Chemie": 3},
  {"Jméno": "Červenáček", "Český jazyk": 1, "Anglický jazyk": 1, "Matematika": 1, "Fyzika": 2, "Informatika": 4},
  {"Jméno": "Rychlonožka", "Český jazyk": 4, "Anglický jazyk": 3, "Matematika": 2, "Chemie": 1, "Biologie": 4},
]


for student in vysledky:
    jmeno=student.pop('Jméno') #zbavíme se jména a uložíme ho
    znamky=student.values()
    prumer=sum(znamky)/len(znamky)
    print(f'{jmeno} má průměr známek z maturity {prumer}')
