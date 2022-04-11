nazev_souboru= input("Zadej celý název souboru:")
with open (nazev_souboru) as vstup:
    auta=vstup.readlines()

auto_km= [float(auto.split()[1].replace(",","."))for auto in auta]
print (f"Součet všech ujetých km je: {sum(auto_km)} tisíc.")