from random import randint

from pomocnicze.wektor2d import Wektor2d
from symulacja.organizmy.organizm import Organizm
from symulacja.organizmy.roslina import Roslina
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

        for org in self.__organizmy:
            org.nowaTura()

        self.__nrTury+=1
        self.__ruchOrganizmow()

        self.__organizmy = [x for x in self.__organizmy if x.isZywy()] # pozbadz sie zwlok

    def addOrganizm(self, org: Organizm):
        org.setSwiat(self)
        self.__organizmy.append(org)

    def __ruchOrganizmow(self):


        self.__organizmy = sorted(self.__organizmy,reverse=True, key= lambda x: x.getWiek())
        self.__organizmy = sorted(self.__organizmy, reverse=True, key= lambda x: x.getInicjatywa())

        for org in self.__organizmy:

            if org.isZywy():

                org.akcja()
                org.kolizja()

            org.starzejSie()

    def getWolnePoleObok(self, p : Wektor2d, zasieg = 1):

        for dy in [-1 * zasieg, 0, zasieg]:

            for dx in [-1 * zasieg, 0, zasieg]:

                punkt =  Wektor2d(dy,dx) + p

                if punkt != p \
                        and self.getOrganizmNaPozycji(punkt) is None \
                        and not punkt.pozaGranicami(self.getWysokosc(),self.getSzerokosc()):
                    return punkt

        return p

    def getLosoweWolnePoleObok(self, p : Wektor2d, zasieg = 1):

        punkty = []

        for dy in [-1 * zasieg, 0, zasieg]:

            for dx in [-1 * zasieg, 0, zasieg]:

                punkt =  Wektor2d(dy,dx) + p

                if punkt != p \
                        and self.getOrganizmNaPozycji(punkt) is None \
                        and not punkt.pozaGranicami(self.getWysokosc(),self.getSzerokosc()):
                    punkty.append(punkt)

        if len(punkty):
            return punkty[randint(0,len(punkty) - 1)]

        return None



    def getKolidujacy(self, org):

        temp =  [x for x in self.__organizmy if x.getPolozenie() == org.getPolozenie() and x != org]

        if len(temp):
            return temp[0]

        return None


    @staticmethod
    def Bazowy():

        swiat = Swiat(15, 15, [

            Zwierze(Wektor2d(1,1),1,1),
            Zwierze(Wektor2d(2, 2), 2, 2),
            Roslina(Wektor2d(4,4),1),
            Roslina(Wektor2d(4, 2), 1),
            Roslina(Wektor2d(10, 10), 1),
        ])

        return swiat