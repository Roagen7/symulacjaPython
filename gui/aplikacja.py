from tkinter import *
from tkinter import ttk
from gui.wizualizacja import Wizualizacja
from pomocnicze.wektor2d import Wektor2d
from symulacja.organizmy.rosliny.barszcz_sosnowskiego import BarszczSosnowskiego
from symulacja.organizmy.rosliny.guarana import Guarana
from symulacja.organizmy.rosliny.mlecz import Mlecz
from symulacja.organizmy.rosliny.trawa import Trawa
from symulacja.organizmy.rosliny.wilcze_jagody import WilczeJagody
from symulacja.organizmy.zwierzeta.antylopa import Antylopa
from symulacja.organizmy.zwierzeta.czlowiek import Czlowiek
from symulacja.organizmy.zwierzeta.lis import Lis
from symulacja.organizmy.zwierzeta.owca import Owca
from symulacja.organizmy.zwierzeta.wilk import Wilk
from symulacja.organizmy.zwierzeta.zolw import Zolw
from symulacja.swiat import Swiat


class Aplikacja(Tk):


    TYTUL = "Symulacja"
    DOMYSLNA_WYSOKOSC = 600
    DOMYSLNA_SZEROKOSC = 600


    def __init__(self, wysokosc: int, szerokosc: int):

        super().__init__()

        self._wizualizacja = Wizualizacja(self, int(Aplikacja.DOMYSLNA_WYSOKOSC * 9 / 10), self.__bazowySwiat())

        self.geometry(f"{szerokosc}x{wysokosc}")
        self.minsize(szerokosc, wysokosc)

        self.title(Aplikacja.TYTUL)

        self.__inicjujMenuGorne()

        self.__inicjujPanelGlowny()

        self._wizualizacja.paint()


    def __inicjujMenuGorne(self):

        menuBar = Menu(self)
        menuNowy = Menu(menuBar, tearoff=False)
        menuPlik = Menu(menuBar, tearoff=False)

        menuNowy.add_command(label="Bazowy", command=self.__bazowyCallback)

        menuPlik.add_command(label="Wczytaj", command=self.__wczytajCallback)
        menuPlik.add_command(label="Zapisz", command=self.__zapiszCallback)

        menuBar.add_cascade(label="Nowy", menu=menuNowy)
        menuBar.add_cascade(label="Plik", menu=menuPlik)

        self.config(menu=menuBar)


    def __inicjujPanelGlowny(self):

        self._wizualizacja.pack()

        panelGuziki = PanedWindow()


        turaButton = Button(panelGuziki, text="nastepna tura", command=self.__nastepnaTuraCallback)
        dziennikButton =  Button(panelGuziki, text="dziennik", command=self.__dziennikCallback)

        panelGuziki.add(turaButton)
        panelGuziki.add(dziennikButton)
        panelGuziki.pack()


    def __bazowyCallback(self):

        self._wizualizacja.setSwiat(self.__bazowySwiat())
        self._wizualizacja.paint()

    def __wczytajCallback(self):

        pass


    def __zapiszCallback(self):

        pass


    def __nastepnaTuraCallback(self):

        self._wizualizacja.nastepnaTura()
        self._wizualizacja.paint()

    def __dziennikCallback(self):

        dziennik = self._wizualizacja.getDziennik().wypisz()
        popup = Toplevel(self)
        popup.title("dziennik")
        Label(popup, text=dziennik).pack()

    def __bazowySwiat(self):
        return Swiat(20, 20, [

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
            Lis(Wektor2d(12, 12)),
            Czlowiek(Wektor2d(5,5))

        ])

