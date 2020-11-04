from .Territory import Territory
from .diceShaker import diceShaker
from .Result import Result

class Attack:

    defendingArmies = None


    def __init__(self, atkTerr: Territory, defTerr: Territory, atkArmies: int):
        self.attackingTerritory = atkTerr
        self.defendingTerritory = defTerr
        self.attackingArmies = atkArmies

    def setDefendingArmies(self, defArmies: int):
        self.defendingArmies = defArmies

    def rollDice(self, armiesNumber: int):
        diceShak = diceShaker.getInstance()
        diceShak.rollDice(armiesNumber)
        #ritorna i dadi tirati, ordinati in ordine crescente
        return (diceShak.getDiceResults()).sort(reverse=True)

    def calculateResult(self):
        atkLosses = 0
        defLosses = 0
        atkDices = self.rollDice(self.attackingArmies)
        defDices = self.rollDice(self.defendingArmies)
        for i in range(min(len(atkDices), len(defDices))):
            if atkDices[i] > defDices[i]:
                defLosses += 1
            else:
                atkLosses += 1
        res = Result()










