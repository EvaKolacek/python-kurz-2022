with open("posta.html", encoding='utf-8') as vstup:
    posta = vstup.read()

new_posta=posta.replace('\n'," ")
import re
posta_final=re.sub("\s+"," ",new_posta)

'''Najdi v datech všechna česká a slovenská města a jejich PSČ, která se nacházejí v ukázkových adresách. Mají format PSČ MĚSTO, kde PSČ se skládá ze tří číslic, mezery a dvou číslic, a MĚSTO se skládá z jednoho nebo více slov oddělených mezerou, za kterými může ještě následovat číslo pošty.460 15 LIBEREC 15, 512 11 VYSOKÉ NAD JIZEROU'''

reg_vyraz=re.compile("\d{3} \d{2} \w+ *\w+ *\w+")
psc_mesto=reg_vyraz.findall(str(posta_final))

for psc in psc_mesto:
    print(psc)

