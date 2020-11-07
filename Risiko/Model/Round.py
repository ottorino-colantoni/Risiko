from .Player import Player
from .Board import Board
from .combatPhase import combatPhase


class Round:

    def __init__(self, player: Player):
        self.__board = Board.getInstance()
        self.__roundPlayer = player


    def enterAttackingTerritory(self, territoryID):

         return self.__board.getAttackableTerritories(territoryID)


    def confirmAttack(self, attackingTerritoryID, defendingTerritoryID, attackingArmiesNumber):

        atkTerritory = self.__board.findTerritory(attackingTerritoryID)
        dfnTerritory = self.__board.findTerritory(defendingTerritoryID)
        self.cPhase.makeAttack(atkTerritory, dfnTerritory, attackingArmiesNumber)

        #TODO: Notify defender player


    def enterDefendingArmies(self, defendingArmiesNumber):

        self.cPhase.fight(defendingArmiesNumber)

    def startCombatPhase(self):

        #TODO: time remaining Timer !!!!
        self.cPhase = combatPhase(30)
        return self.__board.getAttackingTerritories(self.__roundPlayer.getNickName())


    def endCombatPhase(self):
        pass


