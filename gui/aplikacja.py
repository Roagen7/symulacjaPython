from tkinter import *
from tkinter import ttk
from gui.wizualizacja import Wizualizacja
from symulacja.swiat import Swiat


class Aplikacja(Tk):


    TYTUL = "Symulacja"
    DOMYSLNA_WYSOKOSC = 600
    DOMYSLNA_SZEROKOSC = 600


    def __init__(self, wysokosc: int, szerokosc: int):

        super().__init__()

        self._wizualizacja = Wizualizacja(self, int(Aplikacja.DOMYSLNA_WYSOKOSC * 9 / 10), Swiat.Bazowy())

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

        pass


    def __wczytajCallback(self):

        pass


    def __zapiszCallback(self):

        pass


    def __nastepnaTuraCallback(self):

        self._wizualizacja.paint()

    def __dziennikCallback(self):

        pass