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
                print(str(key) + " " + str(territory) + " " + str(self.__continetMap[key].getContinentTerritory()[territory].getOwner().getNickName())
                      + " " + str(self.__continetMap[key].getContinentTerritory()[territory].getArmiesNumber()))


    def getContinentMap(self):
        return self.__continetMap

    def setContinentMap(self, newMap):
        self.__continetMap = newMap

    def getMapId(self):
        return self.__mapId

    def setMapId(self, newId):
        self.__mapId = newId


    def getAttackingTerritories(self, playerID):
        # TODO: modify for fun

        playerTerritories = []

        for continent in self.__continetMap:
            continentTerritories = self.__continetMap[continent].getPlayerTerritories(playerID)
            if continentTerritories != None:
                playerTerritories += continentTerritories
        attackingTerritories = playerTerritories.copy()

        for atkTerritory in playerTerritories:
            remove = True
            if atkTerritory.getArmiesNumber() > 1:
                for neighbor in atkTerritory.getNeighbors():
                    if neighbor.getOwner != playerID:
                        remove = False
                        break
                if remove:
                    attackingTerritories.remove(atkTerritory)
            else:
                attackingTerritories.remove(atkTerritory)


        return attackingTerritories

    def getAttackableTerritories(self, territoryID):
        try:
            find = self.findTerritory(territoryID)
        except:
            raise Exception("Wrong Atk Territory")

        attackableTerritories = []
        for neighbor in find.getNeighbors():
            if find.getOwner() !=  neighbor.getOwner():
                attackableTerritories.append(neighbor)

        return attackableTerritories


    def findTerritory(self, territoryID):
        find = None
        for continent in self.__continetMap:
            find = self.__continetMap[continent].findTerritory(territoryID)
            if (find != None):
                break

        if(find == None):
            raise Exception("Territory not found")

        return find














