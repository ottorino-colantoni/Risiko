from .Territory import Territory
from .Continent import Continent
from .boardBuilder import  boardBuilder


class Board:

    __instance = None
    __boardBuilder = None

    @staticmethod
    def setBoardBuilder(builder : boardBuilder):
        Board.__boardBuilder = builder

    @staticmethod
    def getInstance():
        if Board.__instance == None:
            Board()
        return Board.__instance

    def __init__(self):
        if Board.__instance != None:
            raise Exception("This class is a Singleton")
        else:
            self.__boardBuilder.buildContinents()
            self.__boardBuilder.buildTerritories()
            self.__continetMap = self.__boardBuilder.getBoard()
            self.__mapId = self.__boardBuilder.getMapId()
            Board.__instance = self


    def printBoard(self):
        for key in self.__continetMap:
            print(key)
            for territory in self.__continetMap[key].getContinentTerritory():
                print(str(key) + " " + str(territory))


    def getContinentMap(self):
        return self.__continetMap

    def setContinentMap(self, newMap):
        self.__continetMap = newMap

    def getMapId(self):
        return self.__mapId

    def setMapId(self, newId):
        self.__mapId = newId









