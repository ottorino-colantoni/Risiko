import pickle
import time

class Eventlistner:

    def __init__(self):
        pass

    def splitString(self,string):
        if self.game.gameCanStart():
            data = string.split("/")
            if data[0] == "startCPhase":
                dts = self.startCPhase()
                return dts
        else:
            return "Waiting for more player/0"

    def setGame(self, game):
        self.game = game


    def startCPhase(self):
        data_to_send = ""
        returnTerritory = self.game.round.startCombatPhase()
        data_to_send += ("Puoi muovere un attacco dai seguenti territori: " + "/0")
        for territory in returnTerritory:
            data_to_send += (territory.getNameID() + "/0")
        return data_to_send


