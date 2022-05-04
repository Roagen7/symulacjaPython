from pomocnicze.wektor2d import Wektor2d
from symulacja.organizmy.roslina import Roslina


class Trawa(Roslina):


    SILA = 0

    def __init__(self, polozenie: Wektor2d):
        super().__init__(polozenie, Trawa.SILA)


    def rysowanie(self) -> str:

        return "green"


    def __str__(self):

        return "TRAWA"