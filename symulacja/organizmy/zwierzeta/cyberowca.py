from pomocnicze.wektor2d import Wektor2d
from symulacja.organizmy.rosliny.barszcz_sosnowskiego import BarszczSosnowskiego
from symulacja.organizmy.zwierze import Zwierze


class Cyberowca(Zwierze):


    SILA = 11
    INICJATYWA = 4

    def __init__(self, polozenie: Wektor2d):
        super().__init__(polozenie, Cyberowca.SILA, Cyberowca.INICJATYWA)
        self._rozmnozylSie = True

    def akcja(self):

        min_polozenie = self.getPolozenie()

        for org in self._swiat.getOrganizmy():
            if isinstance(org,BarszczSosnowskiego):

                poz = org.getPolozenie()
                if min_polozenie == self.getPolozenie() or \
                    min_polozenie - self.getPolozenie() > poz - self.getPolozenie():

                    min_polozenie = poz

        if min_polozenie == self.getPolozenie():
            super().akcja()
            return

        zm = min_polozenie-self.getPolozenie()
        zm = zm.znormalizowany()

        self._zmienPolozenie(zm)



    def nowaTura(self):
        pass

    def zabij(self):
        pass


    def rysowanie(self) -> str:

        return "#555652"

    def __str__(self):

        return "OWCA"