from .Player import Player

class Territory:

    __nameID = None
    __armiesNumber = None
    __owner = None

    def __init__(self, name, armies):
        self.__nameID = name
        self.__armiesNumber = armies
        self.__owner = None

    #change the owner instance
    def setOwner(self, player : Player):
        self.__owner = player

    # return the owner instance
    def getOwner(self):
        return self.__owner

    #return the owner identifier
    def getOwnerID(self):
        ownerID = self.__owner.getNickName()
        return ownerID

    #return the territory name
    def getNameID(self):
        return self.__nameID

    #return the armies number
    def getArmiesnumber(self):
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


