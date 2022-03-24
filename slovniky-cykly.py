


""" books = [
  {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
  {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
  {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]# seznam

books[0]# slovník
books[0]['sold'] # číslo

rok =2019
pocet_prodanych_knih =0

for book in books:
    if book['year']== rok:
       pocet_prodanych_knih= pocet_prodanych_knih + (book["sold"])# počet prodaných knížek
       pocet_prodanych_knih+=(book['sold'])# zkrácený zápis
print(f'Za rok {rok} jsme prodali {pocet_prodanych_knih} knih') """

""" sales = {
    "Zkus mě chytit":4165,
    "Vrah zavolá v deset":5681,
    "Zločinný steh":2565
}

for book, value in sales.items():
    if len(book)>15:
        print(book)
        print(value)
        print(book, value)
        print(f'Titulu {book} se prodalo {value} ks') """

""" print(sales.keys())
print(sales.values())
for book in sales:
    if len(book)>15:
        print(book)
        print(sales[book])
        print(f'Titulu {book} se prodalo {sales[book]} ks') """

""" nazvy = ['Zkus mě chytit','Vrah zavola v deset', 'Zločinný steh']

for nazev in nazvy:
    print(nazev)

jmeno="Eva"

for pismeno in jmeno:
    print(pismeno) """