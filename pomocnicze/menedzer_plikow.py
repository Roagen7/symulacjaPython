import copy

from pomocnicze.wektor2d import Wektor2d
from symulacja.organizmy.organizm import Organizm
from symulacja.organizmy.rosliny.barszcz_sosnowskiego import BarszczSosnowskiego
from symulacja.organizmy.rosliny.guarana import Guarana
from symulacja.organizmy.rosliny.mlecz import Mlecz
from symulacja.organizmy.rosliny.trawa import Trawa
from symulacja.organizmy.rosliny.wilcze_jagody import WilczeJagody
from symulacja.organizmy.zwierzeta.antylopa import Antylopa
from symulacja.organizmy.zwierzeta.cyberowca import Cyberowca
from symulacja.organizmy.zwierzeta.czlowiek import Czlowiek
from symulacja.organizmy.zwierzeta.lis import Lis
from symulacja.organizmy.zwierzeta.owca import Owca
from symulacja.organizmy.zwierzeta.wilk import Wilk
from symulacja.organizmy.zwierzeta.zolw import Zolw
from symulacja.swiat import Swiat


class MenedzerPlikow:

    def zapisz(self, swiat: Swiat, name: str):

        with open(name, "w") as out:

            out.write(f"{swiat.getNrTury()} {swiat.getWysokosc()} {swiat.getSzerokosc()} {'KART' if swiat.getTyp() == Swiat.Typ.KARTEZJANSKI else 'HEX'}\n")

            for org in swiat.getOrganizmy():

                out.write(f"{str(org)} {org.getWiek()} {org.getPolozenie().getY()} {org.getPolozenie().getX()}")

                if isinstance(org, Czlowiek):
                    out.write(f" {org.getTurySpecjalne()}")

                out.write("\n")

    def wczytaj(self, name):

        try:

            with open(name, "r") as input:

                r = input.read().split("\n")

                r = [el for el in r if el != ""]

                t, h, w, typ = [el for el in r[0].split(" ")]

                sw = Swiat(int(h), int(w), None, Swiat.Typ.HEX if typ == "HEX" else Swiat.Typ.KARTEZJANSKI)
                sw.setNrTury(int(t))


                for i in range(1, len(r)):
                    org = self.__wczytajOrganizm(r[i])

                    sw.addOrganizm(org)

                return sw


        except:

            return None

    def __wczytajOrganizm(self, line: str) -> Organizm:

        args = line.split(" ")

        org = self.__alokujPoNazwie(args[0])

        if org is None:
            raise Exception

        org.setWiek(int(args[1]))
        org.setPolozenie(Wektor2d(int(args[2]),int(args[3])))

        if isinstance(org, Czlowiek):
            org.setTurySpecjalne(int(args[4]))

        return org

    def __alokujPoNazwie(self, nazwa: str):

        p0 = Wektor2d(0, 0)

        organizmy = [
            Czlowiek(p0),
            Wilk(p0),
            Owca(p0),
            Lis(p0),
            Zolw(p0),
            Antylopa(p0),
            Trawa(p0),
            Mlecz(p0),
            Guarana(p0),
            WilczeJagody(p0),
            BarszczSosnowskiego(p0),
            Cyberowca(p0)

        ]

        for org in organizmy:

            if str(org) == nazwa:

                return copy.deepcopy(org)


        return None
