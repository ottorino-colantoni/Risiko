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
            self.attackingTerritory.setArmiesNumber(self.attackingTerritory-movedArmies)
            self.defendingTerritory.setArmiesNumber(movedArmies)

        else:
            self.attackingTerritory.setArmiesNumber(self.attackingTerritory-atkLosses)
            self.defendingTerritory.setArmiesNumber(self.defendingArmies-defLosses)


        res = Result(atkLosses, defLosses, conquered)










