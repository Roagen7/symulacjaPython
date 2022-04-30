class Swiat:


    def __init__(self, wysokosc: int, szerokosc: int):

        self.__wysokosc = wysokosc
        self.__szerokosc = szerokosc
        self.__organizmy = []


    def getWysokosc(self):

        return self.__wysokosc


    def getSzerokosc(self):

        return self.__szerokosc


    @staticmethod
    def Bazowy():

        swiat = Swiat(30,30)

        return swiat
