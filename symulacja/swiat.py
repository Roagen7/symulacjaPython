from pomocnicze.wektor2d import Wektor2d
from symulacja.organizmy.organizm import Organizm
from symulacja.organizmy.zwierze import Zwierze


class Swiat:

    def __init__(self, wysokosc: int, szerokosc: int, organizmy=None):

        if organizmy is None:
            organizmy = []
        else:
            for organizm in organizmy:
                organizm.setSwiat(self)

        self.__wysokosc = wysokosc
        self.__szerokosc = szerokosc
        self.__organizmy = organizmy
        self.__nrTury = 0

    def getWysokosc(self):
        return self.__wysokosc

    def getSzerokosc(self):
        return self.__szerokosc

    def getOrganizmNaPozycji(self, pozycja: Wektor2d) -> Organizm:

        szukany = None

        for organizm in self.__organizmy:

            if organizm.getPolozenie() == pozycja and organizm.isZywy():

                if szukany is None or szukany.getSila() < organizm.getSila():

                    szukany = organizm

        return szukany

    def wykonajTure(self):

        self.__nrTury+=1
        self.__ruchOrganizmow()
        self.__pozbadzSieZwlok()


    @staticmethod
    def Bazowy():

        swiat = Swiat(30, 30, [
            Zwierze(Wektor2d(1,1),1,1),
            Zwierze(Wektor2d(2, 2), 1, 1)

        ])

        return swiat

    def __ruchOrganizmow(self):

        # self.__organizmy.sort()
        for org in self.__organizmy:

            if org.isZywy():

                org.akcja()
                org.kolizja()

            org.starzejSie()


    def __pozbadzSieZwlok(self):
        pass
