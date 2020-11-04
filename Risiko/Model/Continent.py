from .Territory import Territory

class Continent:


    __continentTerritories =  {}
    __continentId = None
    __isConquered = False

    def __init__(self, name):
        self.__continentId = name
        self.__continent = {}
        self.__isConquered = False


    def addTerritory(self, territory : Territory):
        self.__continentTerritories[territory.getNameID()]= territory

    def getContinentId(self):
        return self.getContinentId

    def getContinentTerritory(self):
        return self.__continentTerritories

    def hasTerritory(self, territory : Territory):
        for key in self.__continentTerritories:
            if territory.getNameID() == self.__continentTerritories[key].getNameID():
                return True

    def isConquered(self):
        owner = None
        for key in self.__continentTerritories:
            if owner == None:
                owner = self.__continentTerritories[key].getOwnerID()
            elif owner != self.__continentTerritories[key].getOwnerID():
                self.__isConquered = False
                return self.__isConquered
        self.__isConquered = True
        return self.__isConquered



    def getPlayerTerritory(self, playerId):
        playerTerritory = []
        for key in self.__continentTerritories:
            if playerId == self.__continentTerritories[key].getOwnerID():
                playerTerritory.add(self.__continentTerritories[key])

        if not playerTerritory:
            return (str(playerId)+ " has not territory in " + str(self.getContinentId()))
        else:
            return playerTerritory



