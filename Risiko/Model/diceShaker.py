from .Die import Die


class diceShaker:

    __instance = None
    __diceResults = []

    @staticmethod
    def getInstance():
        if diceShaker.__instance == None:
            diceShaker()
        else:
            diceShaker.__diceResults = []
            return diceShaker.__instance

    def __init__(self):
        if diceShaker.__instance != None:
            raise Exception("diceShaker is a Singleton")
        else:
            diceShaker.__instance = self

    def rollDice(self, diceNumber):
        riskDie = Die()
        for i in range(diceNumber):
            riskDie.rollDie()
            self.__diceResults.append(riskDie.getFaceValue())

    def getDiceResults(self):
        return self.__diceResults

    def getSortDiceResults(self):
        self.__diceResults.sort(reverse= True)
        return self.__diceResults