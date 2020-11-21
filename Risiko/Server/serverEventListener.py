import pickle
import time


class Eventlistener:

    # fase/attributo1/attributo2...

    def __init__(self):
        pass

    def manageRequest(self, string):
        if self.game.gameCanStart():
            data = string.split("/")
            if data[0] == "startCPhase":
                dts = self.startCPhase()
            elif data[0] == "enterAttackingTerritory":
                if len(data) == 2:
                    dts = self.enterAttackingTerritory(data[1])
            elif data[0] == "confirmAttack":
                if len(data) == 4:
                    dts = self.confirmAttack(data[1], data[2], data[3])

            return dts
        else:
            return "Waiting for more player\n"

    def setGame(self, game):
        self.game = game

    def startCPhase(self):
        data_to_send = ""
        playerTerritories = self.game.round.startCombatPhase()
        if len(playerTerritories) == 0:
            data_to_send = "Non ci sono territori da cui puoi attaccare"
        else:
            data_to_send += ("Puoi muovere un attacco dai seguenti territori: " + "\n")
            for territory in playerTerritories:
                data_to_send += (territory.getNameID() + "\n")

        return data_to_send

    def enterAttackingTerritory(self, territoryID):
        data_to_send = ""

        # raised whenever an attacking territory is missing
        try:
            attackableTerritories = self.game.round.enterAttackingTerritory(territoryID)

            if len(attackableTerritories) > 0:
                data_to_send += ("I territori attaccabili sono: " + "\n")
                for attackableTerritory in attackableTerritories:
                    data_to_send += (attackableTerritory.getNameID() + "\n")
            else:
                data_to_send = "Non puoi attaccare nessun territorio da qui\n"
        except Exception as err:
            data_to_send = type(err).__name__

        return data_to_send

    def confirmAttack(self, attackingTerritoryID, defendingTerritoryID, armies):
        data_to_send = ""
        try:
            self.game.round.confirmAttack(attackingTerritoryID, defendingTerritoryID, armies)

            self.__notifyDefPlayer(attackingTerritoryID, defendingTerritoryID, armies)

        except Exception as err:
            data_to_send = type(err).__name__
            return data_to_send

    def __notifyDefPlayer(self, attackingTerritoryID, defendingTerritoryID, armies):
        board = self.game.round.getBoard()
        defTerritory = board.findTerritory(defendingTerritoryID)
        defPlayer = defTerritory.getOwner()
        defPlayerSocket = self.game.playerSocket[defPlayer]

        atkPlayer = self.game.round.getRoundPlayer()
        data_to_send = f'Il giocatore {atkPlayer} ti sta attaccando da {attackingTerritoryID} a {defendingTerritoryID} con {armies}'
        defPlayerSocket.send(data_to_send)
