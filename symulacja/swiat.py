from random import randint

from pomocnicze.dziennik import Dziennik
from pomocnicze.wektor2d import Wektor2d
from symulacja.organizmy.organizm import Organizm
from symulacja.organizmy.roslina import Roslina
from symulacja.organizmy.rosliny.barszcz_sosnowskiego import BarszczSosnowskiego
from symulacja.organizmy.rosliny.guarana import Guarana
from symulacja.organizmy.rosliny.mlecz import Mlecz
from symulacja.organizmy.rosliny.trawa import Trawa
from symulacja.organizmy.rosliny.wilcze_jagody import WilczeJagody
from symulacja.organizmy.zwierze import Zwierze
from symulacja.organizmy.zwierzeta.antylopa import Antylopa
from symulacja.organizmy.zwierzeta.lis import Lis
from symulacja.organizmy.zwierzeta.owca import Owca
from symulacja.organizmy.zwierzeta.wilk import Wilk
from symulacja.organizmy.zwierzeta.zolw import Zolw


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
        self.__dziennik = Dziennik()

    def getWysokosc(self):
        return self.__wysokosc

    def getSzerokosc(self):
        return self.__szerokosc

    def getDziennik(self):
        return self.__dziennik

    def getOrganizmNaPozycji(self, pozycja: Wektor2d) -> Organizm:

        szukany = None

        for organizm in self.__organizmy:

            if organizm.getPolozenie() == pozycja and organizm.isZywy():

                if szukany is None or szukany.getSila() < organizm.getSila():

                    szukany = organizm

        return szukany

    def wykonajTure(self):

        self.__dziennik.czysc()

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

        swiat = Swiat(20, 20, [

            Wilk(Wektor2d(1,1)),
            Wilk(Wektor2d(2, 2)),
            Trawa(Wektor2d(4,4)),
            Trawa(Wektor2d(4, 2)),
            Trawa(Wektor2d(10, 10)),
            Owca(Wektor2d(14,14)),
            Owca(Wektor2d(13, 14)),
            Mlecz(Wektor2d(9,4)),
            WilczeJagody(Wektor2d(12,14)),
            Zolw(Wektor2d(14,15)),
            Zolw(Wektor2d(15,16)),
            Guarana(Wektor2d(17,17)),
            BarszczSosnowskiego(Wektor2d(17, 5)),
            Antylopa(Wektor2d(13,4)),
            Lis(Wektor2d(12, 12))

        ])

        return swiat