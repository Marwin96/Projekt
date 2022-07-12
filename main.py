#


from funkce_pojistenci import Funkce_pojistenci, seznam_pojistenych
from pojistenec import Pojistenec
from funkce_system import Systemove_funkce
funkce_pojistenci = Funkce_pojistenci 
systemove_funkce = Systemove_funkce


while True:
    systemove_funkce.moznosti()
    print()
    try:
       volba = int(input("Zvolte volbu: "))
       if volba <= 0 or volba >= 5:
        print("\nNeplatná volba. Lze zadat pouze volbu v rozmezí 1-4.\n")
    except:
        print("\nNeplatná volba. Lze zadat pouze volbu v rozmezí 1-4.\n")
        continue
    if volba == 1:
        funkce_pojistenci.vytvoreni_pojisteneho(Pojistenec)
        systemove_funkce.vypis_zpravu_o_zalozeni(Systemove_funkce, zprava_zalozeni="")
        systemove_funkce.vycisti_obrazovku(Systemove_funkce)
    elif volba == 2:
        funkce_pojistenci.vypsani_pojistenych(Pojistenec)
        systemove_funkce.vypis_zpravu_o_vypsani(Systemove_funkce, zprava_vypsani="")
        systemove_funkce.vycisti_obrazovku(Systemove_funkce)
    elif volba == 3:
        funkce_pojistenci.vyhledani_pojisteneho(Pojistenec)
        systemove_funkce.vypis_zpravu_vyhledavani(Systemove_funkce, zprava_vyhledavani="")
        systemove_funkce.vycisti_obrazovku(Systemove_funkce)
    elif volba == 4:
        print("Děkuji za využití.")
        break