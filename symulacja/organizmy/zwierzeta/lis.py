from pomocnicze.wektor2d import Wektor2d
from symulacja.organizmy.zwierze import Zwierze


class Lis(Zwierze):


    SILA = 3
    INICJATYWA = 7


    def __init__(self, polozenie: Wektor2d):
        super().__init__(polozenie, Lis.SILA, Lis.INICJATYWA)


    def czyMaDobryWech(self):

        return True


    def rysowanie(self) -> str:

        return "orange"


    def __str__(self):
        return "LIS"

