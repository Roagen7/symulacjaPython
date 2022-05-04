import copy
from random import randint

from pomocnicze.wektor2d import Wektor2d
from symulacja.organizmy.organizm import Organizm


class Zwierze(Organizm):


    def __init__(self, polozenie: Wektor2d, sila: int, inicjatywa: int):

        super().__init__(polozenie, sila, inicjatywa)
        self.__rozmnozylSie = False


    def akcja(self):

        self._losowyRuch()


    def kolizja(self):

        drugi = self._swiat.getKolidujacy(self)

        if drugi is None:
            return

        if str(drugi) == str(self):

            self._rozmnozSie(drugi)
            return

        self._walcz(drugi)


    def nowaTura(self):

        self.__rozmnozylSie = False



    def _losowyRuch(self, zasieg = 1):


        if self.czyMaDobryWech() and self.wszyscySasiedziSilniejsi():
            return

        koordynaty = [-1 * zasieg, 0,zasieg]
        wczesniejsze = Wektor2d(self._polozenie.getY(), self._polozenie.getX())

        while True:

            randX = koordynaty[randint(0,2)]
            randY = koordynaty[randint(0,2)]

            przemieszczenie = Wektor2d(randY,randX)

            self._zmienPolozenie(przemieszczenie)

            if not (wczesniejsze == self._polozenie or
                    (self.czyMaDobryWech() and
                     self._swiat.getKolidujacy(self) is not None and
                     self._swiat.getKolidujacy(self).getSila() > self.getSila())):
                break

    def _zmienPolozenie(self, przemieszczenie: Wektor2d):

        if not (self.getPolozenie() + przemieszczenie) \
            .pozaGranicami(self._swiat.getWysokosc(), self._swiat.getSzerokosc()):

            self._wczesniejszePolozenie = Wektor2d(self._polozenie.getY(), self._polozenie.getX())
            self._polozenie += przemieszczenie

    def _rozmnozSie(self, drugi):

        if drugi.getWiek() == 0:
            return

        org = copy.deepcopy(self)
        self.__cofnijSie()

        miejsceNarodzin = self._swiat.getWolnePoleObok(drugi.getPolozenie())

        if miejsceNarodzin == drugi.getPolozenie() or drugi.__rozmnozylSie or self.__rozmnozylSie:
            return


        org.setPolozenie(miejsceNarodzin)
        org.setWiek(-1)

        self._swiat.addOrganizm(org)


        self.__rozmnozylSie = True
        drugi.__rozmnozylSie = True



    def __cofnijSie(self):

        self.setPolozenie(self._wczesniejszePolozenie)

    def _walcz(self, drugi : Organizm):

        if self.ucieczka() or drugi.ucieczka():
            return

        if self.getSila() < drugi.getSila():

            if self.czyOdbilAtak(drugi):

                self.__cofnijSie()
                return

            self._swiat.getDziennik().wpisz(f"{str(drugi)} zjada {str(self)}")
            self.zabij()
            self.dodajModyfikator(drugi)

            return

        if drugi.czyOdbilAtak(self):

            self.__cofnijSie()
            return

        self._swiat.getDziennik().wpisz(f"{str(self)} zjada {str(drugi)}")
        drugi.zabij()
        drugi.dodajModyfikator(self)

    def wszyscySasiedziSilniejsi(self) -> bool:

        for y in range(-1,2):
            for x in range(-1,2):

                pol = Wektor2d(y,x)

                org = self._swiat.getOrganizmNaPozycji(self.getPolozenie() + pol)

                if org != self and (org is None or org.getSila() <= self.getSila()):

                    return False


        return True

