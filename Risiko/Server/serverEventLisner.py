import pickle
import time

class Eventlistner:

    # fase/attributo1/attributo2...

    def __init__(self):
        pass

    def manageRequest(self,string):
        if self.game.gameCanStart():
            data = string.split("/")
            if data[0] == "startCPhase":
                dts = self.startCPhase()
                return dts
            elif data[0] == "enterAttackingTerritory":
                if len(data) > 1:
                    dts = self.enterAttackingTerritory(data[1])
        else:
            return "Waiting for more player\n"

    def setGame(self, game):
        self.game = game


    def startCPhase(self):
        data_to_send = ""
        playerTerritories = self.game.round.startCombatPhase()
        data_to_send += ("Puoi muovere un attacco dai seguenti territori: " + "\n")
        for territory in playerTerritories:
            data_to_send += (territory.getNameID() + "\n")
        return data_to_send

    def enterAttackingTerritory(self, territoryID):
        data_to_send = ""
        attackableTerritories = self.game.round.enterAttackingTerritory(territoryID);
        if (len(attackableTerritories) > 0):
            data_to_send += ("I territori attaccabili sono: " + "\n")







