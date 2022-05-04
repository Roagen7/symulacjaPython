from pomocnicze.wektor2d import Wektor2d
from symulacja.organizmy.organizm import Organizm
from symulacja.organizmy.roslina import Roslina


class Guarana(Roslina):


    SILA = 0
    ZWIEKSZENIE_SILY = 3

    def __init__(self, polozenie: Wektor2d):
        super().__init__(polozenie, Guarana.SILA)

    def dodajModyfikator(self, other : Organizm):

        other.setSila(other.getSila() + Guarana.ZWIEKSZENIE_SILY)

    def rysowanie(self) -> str:

        return "magenta"


    def __str__(self):

        return "GUARANA"
