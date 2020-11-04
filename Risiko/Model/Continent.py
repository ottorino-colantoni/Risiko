from .Territory import Territory

class Continent:

    __continentTerritories = {}
    __continentId = None
    __isConquered = False

    def __init__(self, name):
        self.__continentId = name
        self.__continent = {}
        self.__isConquered = False

    def addTerritory(self, territory : Territory):
        self.__continentTerritories[territory.getNameID()]= territory

    def getContinentId(self):
        return self.__continentId

    def getContinentTerritory(self):
        return self.__continentTerritories

    def hasTerritory(self, territory : Territory):
        for key in self.__continentTerritories:
            if territory.getNameID() == self.__continentTerritories[key].getNameID():
                return True

    # The function use only the playerId and not the full instance !!!! TODO : what return??
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

    # The function use only the playerId and not the full instance !!!! TODO : what return??
    def getPlayerTerritory(self, playerId):
        playerTerritory = []
        for key in self.__continentTerritories:
            if playerId == self.__continentTerritories[key].getOwnerID():
                playerTerritory.append(self.__continentTerritories[key])

        if not playerTerritory:
            return str(playerId) + " has not territory in " + str(self.getContinentId())
        else:
            return playerTerritory

    # The function use only the playerId and not the full instance !!! TODO : what return??
    def findTerritory(self, territoryID):
        if territoryID in self.__continentTerritories:
            return self.__continentTerritories[territoryID]
        else:
            return str(territoryID) + " is not in " + str(self.getContinentId())



