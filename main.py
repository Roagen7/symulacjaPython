import symulacja.organizmy.organizm
from gui.aplikacja import Aplikacja
from pomocnicze.dziennik import Dziennik

if __name__ == '__main__':

    app = Aplikacja(Aplikacja.DOMYSLNA_WYSOKOSC, Aplikacja.DOMYSLNA_SZEROKOSC)
    app.mainloop()