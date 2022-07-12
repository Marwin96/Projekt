#

class Pojistenec:
    """
    třída pojištěnec
    """

    def __init__(self, jmeno, prijmeni, vek, telefonni_cislo):
        """
        konstruktor pojištěnce obsahující:
        -jméno
        -příjmení
        -věk
        -telefonní číslo
        """
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefonni_cislo = telefonni_cislo

    def __str__(self):
        return ("{0}\t{1}\t{2}\t{3}").format(self.jmeno, self.prijmeni, self.vek, self.telefonni_cislo)