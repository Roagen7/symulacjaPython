from pomocnicze.wektor2d import Wektor2d
from symulacja.organizmy.organizm import Organizm


class Zwierze(Organizm):


    def __init__(self, polozenie: Wektor2d, sila: int, inicjatywa: int):

        super().__init__(polozenie, sila, inicjatywa)


    def akcja(self):
        pass


    def kolizja(self):
        pass

