""" Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
Tvůj program bude obsahovat dvě funkce:

První funkce ověří délku telefonního čísla. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili. Pokud je číslo platné, funkce vrátí hodnotu True, jinak vrátí hodnotu False.
Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli. """

cislo=input('Zadej své telefonní číslo: ')


def delkaCisla(cislo:int):
    if len(cislo)==9:
        return True
    elif len(cislo)==13:
        return True
    else:
        return False

if delkaCisla(cislo)==True:
    zprava=input('Jakou zprávu chcete zaslat?')
    delkaZpravy=len(zprava)
else:
    print('Neplatné číslo!')

def cenaZpravy(delkaZpravy,cena=3):
    if delkaZpravy//180>1:
        return((delkaZpravy//180)*cena)
    else:
        return(cena)

print(f"Cena za zaslanou zprávu je: {cenaZpravy(delkaZpravy)}")
