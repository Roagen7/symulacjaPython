from pomocnicze.wektor2d import Wektor2d
from symulacja.organizmy.organizm import Organizm
from symulacja.organizmy.roslina import Roslina


class WilczeJagody(Roslina):


    SILA = 0

    def __init__(self, polozenie: Wektor2d):
        super().__init__(polozenie, WilczeJagody.SILA)

    def dodajModyfikator(self, other : Organizm):

        other.zabij()



    def rysowanie(self) -> str:

        return "#31004C"


    def __str__(self):

        return "WILCZE_JAGODY"