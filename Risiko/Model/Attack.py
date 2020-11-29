from .Territory import Territory
from .diceShaker import diceShaker
from .Result import Result

class Attack:


    def __init__(self, atkTerr: Territory, defTerr: Territory, atkArmies: int):
        self.attackingTerritory = atkTerr
        self.defendingTerritory = defTerr
        self.attackingArmies = atkArmies
        self.result = None

    def getResult(self):
        return self.result

    def getDefendingTerritory(self):
        return self.defendingTerritory

    def setDefendingArmies(self, defArmies: int):
        self.defendingArmies = defArmies

    def rollDice(self, armiesNumber: int):
        diceShak = diceShaker.getInstance()
        diceShak.rollDice(armiesNumber)
        diceResult = diceShak.getDiceResults()
        diceResult.sort(reverse=True)
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
            self.attackingTerritory.modifyTerritoryArmies(atkLosses)
            self.defendingTerritory.setArmiesNumber(0)

        else:
            self.attackingTerritory.modifyTerritoryArmies(atkLosses)
            self.defendingTerritory.modifyTerritoryArmies(defLosses)


        self.result = Result(atkLosses, defLosses, conquered)

        return self.result


    def conquerMovement(self, armiesNumber):

        atkArmiesLost  = self.result.atkLosses
        atkTerritoryArmies = self.attackingTerritory.getArmiesNumber()

        if(armiesNumber >= (self.attackingArmies-atkArmiesLost) & armiesNumber < atkTerritoryArmies):
            self.attackingTerritory.modifyTerritoryArmies(armiesNumber)
            self.defendingTerritory.setArmiesNumber(armiesNumber)
            return True
        else:
            if(armiesNumber < (self.attackingArmies-atkArmiesLost)):
                raise Exception(f'Devi spostare almeno {self.attackingArmies-atkArmiesLost}')
            else:
                raise Exception(f'Puoi spostare al massimo {atkTerritoryArmies-1}')










