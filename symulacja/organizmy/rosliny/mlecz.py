from pomocnicze.wektor2d import Wektor2d
from symulacja.organizmy.roslina import Roslina


class Mlecz(Roslina):


    SILA = 0
    PROBY = 3

    def __init__(self, polozenie: Wektor2d):
        super().__init__(polozenie, Mlecz.SILA)


    def akcja(self):

        for i in range(Mlecz.PROBY):

            self.rozsiej()






    def rysowanie(self) -> str:

        return "yellow"


    def __str__(self):

        return "MLECZ"