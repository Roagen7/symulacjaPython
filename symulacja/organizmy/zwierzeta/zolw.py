from random import random

from pomocnicze.wektor2d import Wektor2d
from symulacja.organizmy.organizm import Organizm
from symulacja.organizmy.zwierze import Zwierze


class Zolw(Zwierze):


    SILA = 2
    INICJATYWA = 1
    P_RUCHU = 0.25
    OBRONA = 5


    def __init__(self, polozenie: Wektor2d):
        super().__init__(polozenie, Zolw.SILA, Zolw.INICJATYWA)


    def akcja(self):

        if random() < Zolw.P_RUCHU:
            self._losowyRuch()


    def czyOdbilAtak(self,other : Organizm) -> bool:

        return other.getSila() < Zolw.OBRONA



    def rysowanie(self) -> str:

        return "#438C7E"


    def __str__(self):
        return "ZOLW"