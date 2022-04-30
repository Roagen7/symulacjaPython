from tkinter import *
from tkinter import ttk

from pomocnicze.wektor2d import Wektor2d
from symulacja.swiat import Swiat

from random import randint


class Wizualizacja(Canvas):


    __KOLOR_TLA = "black"

    def __init__(self,master, wysokoscOkienka: int, swiat: Swiat):

        self.__wysokoscOkienka = wysokoscOkienka
        self.__wysokosc = swiat.getWysokosc()
        self.__szerokosc = swiat.getSzerokosc()

        self.__swiat = swiat

        self.__rozmiarZwierzecia = int(self.__wysokoscOkienka / self.__wysokosc)


        super().__init__(master, height=wysokoscOkienka,width=self.__rozmiarZwierzecia * self.__szerokosc)


        self.__eventy()

        self.focus_set()


    def paint(self):


        self.create_rectangle(0,0,self.__rozmiarZwierzecia *self.__szerokosc, self.__rozmiarZwierzecia * self.__wysokosc, fill=Wizualizacja.__KOLOR_TLA)

        for y in range(self.__wysokosc):
            for x in range(self.__szerokosc):

                org = self.__swiat.getOrganizmNaPozycji(Wektor2d(y,x))

                if not org is None:

                    self.create_rectangle(x * self.__rozmiarZwierzecia,
                                      y * self.__rozmiarZwierzecia,
                                      x * self.__rozmiarZwierzecia + self.__rozmiarZwierzecia,
                                      y * self.__rozmiarZwierzecia + self.__rozmiarZwierzecia,
                                      fill=org.rysowanie())


    def __eventy(self):

        def klik(event):
            print(event.x,event.y)


        def klawisz(event):
            print(event.char)

        self.bind("<Button-1>",klik)
        self.bind("<Key>",klawisz)


    def nastepnaTura(self):
        self.__swiat.wykonajTure()


    def getDziennik(self):
        return self.__swiat.getDziennik()

    def setSwiat(self, swiat: Swiat):
        self.__swiat = swiat

