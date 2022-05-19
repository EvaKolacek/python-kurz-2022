import requests
import pandas

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_praha.csv")
open("zam_praha.csv", "wb").write(r.content)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_plzeň.csv")
open("zam_plzeň.csv", "wb").write(r.content)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_liberec.csv")
open("zam_liberec.csv", "wb").write(r.content)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/platy_2021_02.csv")
open("platy_2021_02.csv", "wb").write(r.content)

zam_praha=pandas.read_csv('zam_praha.csv')
zam_plzen=pandas.read_csv('zam_plzeň.csv')
zam_liberec=pandas.read_csv('zam_liberec.csv')
platy202102=pandas.read_csv('platy_2021_02.csv')

zam_praha ['město']= 'Praha'
zam_plzen ['město']= 'Plzeň'
zam_liberec ['město']= 'Liberec'

zamestnanci = pandas.concat([zam_praha,zam_plzen,zam_liberec], ignore_index=True)
#print(zamestnanci.shape)
zam202102= pandas.merge(zamestnanci, platy202102, on=['cislo_zamestnance'],how='left')
#print(zam202102.shape)

prumerPlat=zam202102.groupby('město')['plat'].mean()
jizNepracuji=zam202102[zam202102['plat'].isnull()]
jizNepracuji.to_csv('UkonceniZamestnanci.csv',index=False)
jizNepracujiPocet=jizNepracuji['cislo_zamestnance'].count()
print(jizNepracujiPocet)
