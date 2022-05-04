from symulacja.organizmy.zwierzeta.czlowiek import Czlowiek
from symulacja.swiat import Swiat


class MenedzerPlikow:

    def zapisz(self, swiat : Swiat , name : str):

        with open(name, "w") as out:

            for org in swiat.getOrganizmy():

                out.write(f"{str(org)} {org.getWiek()} {org.getPolozenie().getY()} {org.getPolozenie().getX()}")

                if isinstance(org,Czlowiek):
                    out.write(f" {org.getTurySpecjalne()}")

                out.write("\n")


    def wczytaj(self, name):

        try:

            with open(name, "r") as out:
                pass

            return Swiat(20,20)


        except:

            return None





