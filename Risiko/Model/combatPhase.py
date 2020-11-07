from .Attack import Attack
from .Territory import Territory
from .Timer import Timer

# timer method, this will be necessary in the future to implement



class combatPhase(object):
    def __init__(self, combatTimeSeconds: int):
        self.timer = Timer.getInstance()
        self.attacks = []
        self.currentAttack = None

        self.timer.setRemainingTime(combatTimeSeconds)
        self.timer.startTimer(self.emptyTimerFunction)

    # timer method, this will be necessary in the future to implement

    def getAttacks(self):
        return self.attacks


    def emptyTimerFunction(self):
        print("hellWorld")


    def makeAttack(self,attackingTerritory: Territory, defendingTerritory: Territory, attackingArmiesNumber: int):
        self.timer.pauseTimer()
        self.currentAttack = Attack(attackingTerritory, defendingTerritory, attackingArmiesNumber)

    def fight(self, defendingArmiesNumber: int):
        self.currentAttack.setDefendingArmies(defendingArmiesNumber)
        self.currentAttack.calculateResult()

        self.attacks.append(self.currentAttack)
        self.currentAttack = None

        self.timer.resumeTimer(self.emptyTimerFunction)
