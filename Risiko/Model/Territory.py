from .Player import Player


class Territory:


    def __init__(self, name):
        self.__nameID = name
        self.__armiesNumber = 0
        self.__owner = None
        self.__neighbors = []

    # change the owner instance
    def setOwner(self, player : Player):
        self.__owner = player

    # return the owner instance
    def getOwner(self):
        return self.__owner

    # return the owner identifier
    def getOwnerID(self):
        ownerID = self.__owner.getNickName()
        return ownerID

    # return the territory name
    def getNameID(self):
        return self.__nameID

    # return the armies number
    def getArmiesNumber(self):
        return self.__armiesNumber

    # set the territory name
    def setNameID(self, name):
        self.__nameID = name

    # set the number of armies
    def setArmiesNumber(self, armies):
        self.__armiesNumber = armies

    # subtract lostArmies to the armiesNumber
    def modifyTerritoryArmies(self, lostArmies):
        self.__armiesNumber = self.__armiesNumber - lostArmies

    def getNeighbors(self):
        return self.__neighbors

    # This function add neighbors to the territory instance
    # Parameter:
    #   @neighbor = List[]
    def addNeighbors(self, neighbor : []):
        if neighbor == None:
            raise Exception(" Can not be Null value")
        for territory in neighbor:
            self.__neighbors.append(territory)

    def hasNeighbor(self, neighbor):
        find = False
        for ng in self.__neighbors:
            if neighbor.getNameID() == ng.getNameID():
                find = True
                break
        return find

    def printNeighbords(self):
        for ng in self.__neighbors:
            print(str(ng.getNameID()) + " " + str(ng.getArmiesNumber()) + " " + str(ng.getOwnerID()))





