from .Attack import Attack
from .Territory import Territory
from .Timer import Timer


class combatPhase(object):
    def __init__(self, combatTimeSeconds: int):
        self.__timer = Timer.getInstance()
        self.__attacks = []
        self.__currentAttack = None
        self.__end = False
        # timer initialization
        self.__timer.setRemainingTime(combatTimeSeconds)
        self.__timer.startTimer(self.__endPhase)

    def __endPhase(self):
        self.__end = True

    def isFinished(self):
        return self.__end

    def getAttacks(self):
        return self.__attacks

    def getLastAttack(self):
        return self.__attacks[-1]

    def getCurrentAttack(self):
        return self.__currentAttack

    def makeAttack(self, attackingTerritory: Territory, defendingTerritory: Territory, attackingArmiesNumber: int):
        self.__timer.pauseTimer()

        if attackingTerritory.getArmiesNumber() - attackingArmiesNumber < 1:
            raise Exception("Non rimarrebbe nessuna armata nel territorio d'attacco")

        if attackingArmiesNumber > 3:
            raise Exception("Si sta attaccando con troppe armate")


        self.__currentAttack = Attack(attackingTerritory, defendingTerritory, attackingArmiesNumber)

    def fight(self, defendingArmiesNumber: int):

        print("Facciamo sto fight")
        if defendingArmiesNumber > 3:
            raise Exception("Non puoi difendere con piu di 3 armate)")

        numeroArmateNelTerrDiDifesa = self.getCurrentAttack().getDefendingTerritory().getArmiesNumber()
        if numeroArmateNelTerrDiDifesa < defendingArmiesNumber:
            raise Exception(f'Non si disponde di {defendingArmiesNumber} nel territorio in difesa')

        self.__currentAttack.setDefendingArmies(defendingArmiesNumber)

        self.__currentAttack.calculateResult()

        self.__attacks.append(self.__currentAttack)

        self.__currentAttack = None

        self.__timer.resumeTimer(self.__endPhase)

    def endCombatPhase(self):
        self.__timer.stopTimer()
