from pomocnicze.wektor2d import Wektor2d
from symulacja.organizmy.organizm import Organizm
from symulacja.organizmy.roslina import Roslina
from symulacja.organizmy.zwierze import Zwierze


class BarszczSosnowskiego(Roslina):


    SILA = 0

    def __init__(self, polozenie: Wektor2d):
        super().__init__(polozenie, BarszczSosnowskiego.SILA)


    def akcja(self):

        for y in range(-1,2):

            for x in range(-1, 2):

                org = self._swiat.getOrganizmNaPozycji(self.getPolozenie() + Wektor2d(y,x))

                if isinstance(org,Zwierze) and not org.isOdpornyNaToksyny():
                    org.zabij()


        super().akcja()


    def dodajModyfikator(self, other : Organizm):

        if other.isOdpornyNaToksyny():
            return

        other.zabij()


    def rysowanie(self) -> str:

        return "white"


    def __str__(self):

        return "BARSZCZ_SOSNOWSKIEGO"