from random import randint

from pomocnicze.wektor2d import Wektor2d
from symulacja.organizmy.organizm import Organizm


class Zwierze(Organizm):


    def __init__(self, polozenie: Wektor2d, sila: int, inicjatywa: int):

        super().__init__(polozenie, sila, inicjatywa)


    def akcja(self):

        self._losowyRuch()


    def kolizja(self):
        pass


    def nowaTura(self):
        pass


    def rysowanie(self) -> str:

        return "red"


    def _losowyRuch(self, zasieg = 1):

        koordynaty = [-1 * zasieg, 0,zasieg]

        przemieszczenie = Wektor2d(0,0)
        wczesniejsze = Wektor2d(self._polozenie.getY(), self._polozenie.getX())

        while True:

            randX = koordynaty[randint(0,2)]
            randY = koordynaty[randint(0,2)]

            przemieszczenie = Wektor2d(randY,randX)

            self._zmienPolozenie(przemieszczenie)

            if not (wczesniejsze == self._polozenie):
                break

    def _zmienPolozenie(self, przemieszczenie: Wektor2d):

        if not (self.getPolozenie() + przemieszczenie) \
            .pozaGranicami(self._swiat.getWysokosc(), self._swiat.getSzerokosc()):

            self._wczesniejszePolozenie = Wektor2d(self._polozenie.getY(), self._polozenie.getX())
            self._polozenie += przemieszczenie
