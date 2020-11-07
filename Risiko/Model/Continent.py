from .Territory import Territory

class Continent:

    def __init__(self, name):
        self.__continentId = name
        self.__continent = {}
        self.__isConquered = False

    # This function add a List of territories to the dictionary variable @self.__continentterritories
    # Parameter
    #   territories : List[]
    def addTerritory(self, territories: []):
        for ter in territories:
            self.__continent[ter.getNameID()] = ter

    def getContinentId(self):
        return self.__continentId

    def getContinentTerritory(self):
        return self.__continent

    def hasTerritory(self, territory : Territory):
        for key in self.__continent:
            if territory.getNameID() == self.__continent[key].getNameID():
                return True

    # The function use only the playerId and not the full instance !!!! TODO : what return??
    def isConquered(self):
        owner = None
        for key in self.__continent:
            if owner == None:
                owner = self.__continent[key].getOwnerID()
            elif owner != self.__continent[key].getOwnerID():
                self.__isConquered = False
                return self.__isConquered
        self.__isConquered = True
        return self.__isConquered

    # The function use only the playerId and not the full instance !!!! TODO : what return??
    def getPlayerTerritories(self, playerId):
        playerTerritories = []
        for key in self.__continent:
            if playerId == self.__continent[key].getOwnerID():
                playerTerritories.append(self.__continent[key])

        if not playerTerritories:
            return None
        else:
            return playerTerritories

    # The function use only the playerId and not the full instance !!! TODO : what return??
    def findTerritory(self, territoryID):
        if territoryID in self.__continent:
            return self.__continent[territoryID]
        else:
            return None



