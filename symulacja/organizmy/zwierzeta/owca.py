from pomocnicze.wektor2d import Wektor2d
from symulacja.organizmy.zwierze import Zwierze


class Owca(Zwierze):


    SILA = 4
    INICJATYWA = 4


    def __init__(self, polozenie: Wektor2d):
        super().__init__(polozenie, Owca.SILA, Owca.INICJATYWA)


    def rysowanie(self) -> str:

        return "gray"


    def __str__(self):
        return "OWCA"