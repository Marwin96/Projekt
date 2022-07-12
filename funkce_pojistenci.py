#

from pojistenec import Pojistenec

seznam_pojistenych = []

class Funkce_pojistenci:
    """
    třída obsahující funkce vázáné k pojištěnci
    -vytvoření pojištěného
    -vyhledávání pojištěného
    -vypsání všech pojištěných
    """

    def __init__(self, pojistenec):
        """
        konsturktor
        """
        self.pojistenec = pojistenec

    def vytvoreni_pojisteneho(self):
        """
        funkce vytvoření pojištěného
        -vyplnění hodnot jména,příjmení,věku a telefonního čísla
        -kontrola správného typu parametru (věk a tel.číslo)
        -uložení pojištěného do seznamu
        """
        print()
        jmeno = input("Jméno: ")
        prijmeni = input("Příjmení: ")
        kontrola_vek = True
        while kontrola_vek:
            try:
                vek = int(input("Věk: "))
            except:
                print("Lze zadat pouze číselnou hodnotu!")
                continue
            kontrola_vek = False
        kontrola_telefonni_cislo = True
        while kontrola_telefonni_cislo:
            try:
                telefonni_cislo = int(input("Telefon: "))
            except:
                print("Lze zadat pouze číselnou hodnotu!")
                continue
            if len(str(telefonni_cislo)) == 9:
                kontrola_telefonni_cislo = False
            else:
                print("Telefonní číslo musí mít 9 znaků!")
                kontrola_telefonni_cislo = True
        pojistenec = Pojistenec(jmeno, prijmeni, vek, telefonni_cislo)
        seznam_pojistenych.append(pojistenec)
        

    def vyhledani_pojisteneho(self):
        """
        funkce pro vyhledávání pojištěného
        - vyplnění hodnoty pro vyhledávání - jméno a příjmení
        - vyhledání v seznamu - pokud je shodné jméno a příjmení je vypsán
        """
        print()
        zadani_jmeno = input("Zadej hledané jméno: ")
        zadani_prijmeni = input("Zadej hledané příjmení: ")
        kontrola = [pojistenec for pojistenec in seznam_pojistenych if pojistenec.jmeno == zadani_jmeno and pojistenec.prijmeni == zadani_prijmeni]
        print()
        print("Jméno/Příjmení/Věk/Telefonní číslo\n")
        for pojistenec in kontrola:
            print(pojistenec)
    
    def vypsani_pojistenych(self):
        """
        funkce pro vypsání všech pojištěných
        """
        print()
        print("Jméno/Příjmení/Věk/Telefonní číslo\n")
        for osoba in seznam_pojistenych:
            print(osoba)