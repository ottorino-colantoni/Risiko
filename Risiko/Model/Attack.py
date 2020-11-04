from .Territory import Territory
from .diceShaker import diceShaker
from .Result import Result

class Attack:

    defendingArmies = None

    def __init__(self, atkTerr: Territory, defTerr: Territory, atkArmies: int):
        self.attackingTerritory = atkTerr
        self.defendingTerritory = defTerr
        self.attackingArmies = atkArmies
        self.result = None

    def setDefendingArmies(self, defArmies: int):
        self.defendingArmies = defArmies

    def rollDice(self, armiesNumber: int):
        diceShak = diceShaker.getInstance()
        diceShak.rollDice(armiesNumber)
        diceResult = diceShak.getDiceResults()
        diceResult.sort(reverse = True)
        return diceResult

    def calculateResult(self):
        conquered = False
        atkLosses = 0
        defLosses = 0
        atkDices = self.rollDice(self.attackingArmies)
        defDices = self.rollDice(self.defendingArmies)

        for i in range(min(len(atkDices), len(defDices))):
            if atkDices[i] > defDices[i]:
                defLosses += 1
            else:
                atkLosses += 1

        if defLosses == self.defendingTerritory.getArmiesNumber():
            conquered = True

        if conquered:
            self.defendingTerritory.setOwner(self.attackingTerritory.getOwner())
            #ASK TO THE ATTACKING PLAYER HOW MANY ARMIES HE WANTS TO MOVE TO THE CONQUERED TERRITORY
            #AT THE MOMENT HE MOVES ALL THE REMAINING ATK ARMIES FROM THE FIGHT
            movedArmies = self.attackingArmies-atkLosses
            self.attackingTerritory.modifyTerritoryArmies(movedArmies)
            self.defendingTerritory.setArmiesNumber(movedArmies)

        else:
            self.attackingTerritory.modifyTerritoryArmies(atkLosses)
            self.defendingTerritory.modifyTerritoryArmies(defLosses)


        self.result = Result(atkLosses, defLosses, conquered)

        return self.result










