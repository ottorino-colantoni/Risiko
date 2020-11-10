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
        try:
            return self.__board.getAttackableTerritories(territoryID)
        except:
            print("TERRITORIO D'ATTACCO NON CORRETTO!!!!")


    def confirmAttack(self, attackingTerritoryID, defendingTerritoryID, attackingArmiesNumber):

        try:
            atkTerritory = self.__board.findTerritory(attackingTerritoryID)
        except:
            print("Il territorio d'attacco non è corretto")
            return
        try:
            dfnTerritory = self.__board.findTerritory(defendingTerritoryID)
        except:
            print("Il territorio di difesa non è corretto")
            return
        try:
            self.cPhase.makeAttack(atkTerritory, dfnTerritory, attackingArmiesNumber)
        except:
            raise Exception("Errore nelle armate in attacco")

        #TODO: Notify defender player


    def enterDefendingArmies(self, defendingArmiesNumber):


        self.cPhase.fight(defendingArmiesNumber)

    def startCombatPhase(self):

        #TODO: time remaining Timer !!!!
        self.cPhase = combatPhase(500000)
        return self.__board.getAttackingTerritories(self.__roundPlayer.getNickName())


    def endCombatPhase(self):
        pass


