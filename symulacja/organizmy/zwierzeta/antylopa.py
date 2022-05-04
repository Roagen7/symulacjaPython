from random import random

from pomocnicze.wektor2d import Wektor2d
from symulacja.organizmy.zwierze import Zwierze


class Antylopa(Zwierze):


    SILA = 4
    INICJATYWA = 4
    ZASIEG = 2
    P_UCIECZKI = 0.5


    def __init__(self, polozenie: Wektor2d):
        super().__init__(polozenie, Antylopa.SILA, Antylopa.INICJATYWA)


    def akcja(self):

        self._losowyRuch(Antylopa.ZASIEG)

    def czyUciekl(self) -> bool:

        return random() < Antylopa.P_UCIECZKI


    def rysowanie(self) -> str:

        return "#964B00"


    def __str__(self):

        return "ANTYLOPA"