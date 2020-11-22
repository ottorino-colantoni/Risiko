from .Player import Player
from .Board import Board
from .combatPhase import combatPhase


class Round:

    def __init__(self, player: Player):
        self.__board = Board.getInstance()
        self.__roundPlayer = player

    def getBoard(self):
        return self.__board

    def getRoundPlayer(self):
        return self.__roundPlayer

    def getCombatPhase(self):
        return self.cPhase

    def enterAttackingTerritory(self, territoryID):

        if self.cPhase.isFinished():
            raise Exception("il timer è scaduto")

        try:
            return self.__board.getAttackableTerritories(territoryID)
        except Exception as err:
            raise err

    def confirmAttack(self, attackingTerritoryID, defendingTerritoryID, attackingArmiesNumber):

        try:
            atkTerritory = self.__board.findTerritory(attackingTerritoryID)
        except:
            raise Exception("Il territorio d'attacco non è corretto")

        try:
            dfnTerritory = self.__board.findTerritory(defendingTerritoryID)
        except:
            raise Exception("Il territorio di difesa non è corretto")

        try:
            self.cPhase.makeAttack(atkTerritory, dfnTerritory, attackingArmiesNumber)
        except:
            raise Exception("Errore nelle armate in attacco")

        # TODO: Notify defender player

    def enterDefendingArmies(self, defendingArmiesNumber):
        try:
            self.cPhase.fight(defendingArmiesNumber)
        except Exception as err:
            raise Exception(err)

    def startCombatPhase(self):

        # TODO: time remaining Timer !!!!
        self.cPhase = combatPhase(3000)
        return self.__board.getAttackingTerritories(self.__roundPlayer.getNickName())

    def endCombatPhase(self):
        self.cPhase.endCombatPhase()
