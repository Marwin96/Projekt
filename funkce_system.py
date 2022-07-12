#


class Systemove_funkce:
    """ 
    Třída systémové funkce, obsahující pomocné funkce - nejsou vázány k pojištěnci
    - volby, které může zvolit uživatel
    - výpis zprávy o založení uživatele
    - výpis zprávy o vypsání uživatelů
    - výpis zprávy o vyhledávání
    - výmaz obrazovky
    """

    def __init__(self):
        """
        konstruktor
        """
        pass

    def moznosti():
        """
        možnosti volby, kterou uživatel zvolí
        """
        print("----------------------------------------")
        print("Vítejte v aplikaci na správu pojištěných")
        print("----------------------------------------")
        print("Možnosti:")
        print("1 - Přidat nového pojistného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného na základě jména a příjmení")
        print("4 - Konec aplikace")

    def vypis_zpravu_o_zalozeni(self, zprava_zalozeni):
        """
        funkce vypisující zprávu o založení uživatele
        """
        self.zprava_zalozeni = zprava_zalozeni
        zprava_zalozeni = ("\nPojištěný byl uložen do systému. Pokračujte stiskem klávesy ENTER......")
        print(zprava_zalozeni)
        input()
    
    def vypis_zpravu_o_vypsani(self, zprava_vypsani):
        """
        funkce vypisující zprávu o vypsání uživatelů
        """
        self.zprava_vypsani = zprava_vypsani
        zprava_vypsani = ("\nDatabáze pojištěných byla vypsána, pokračujte stikem klávesy ENTER......")
        print(zprava_vypsani)
        input()
    
    def vypis_zpravu_vyhledavani(self, zprava_vyhledavani):
        """
        funkce vypisující zprávu o vyhledání uživatelů
        """
        self.zprava_vyhledavani = zprava_vyhledavani
        zprava_vyhledavani = ("\nVyhledávání bylo ukončeno. Pro pokračování stiskněte klávesu ENTER......")
        print(zprava_vyhledavani)
        input()

    def vycisti_obrazovku(self):
        """
        funkce, která maže hodnoty v obrazovce
        """
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith("win"):
            _subprocess.call(["cmd.exe", "/C", "cls"])
        else:
            _subprocess.call(["clear"])