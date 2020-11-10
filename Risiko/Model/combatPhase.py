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

    def getCurrentAttack(self):
        return self.currentAttack


    def emptyTimerFunction(self):
        print("hellWorld")


    def makeAttack(self,attackingTerritory: Territory, defendingTerritory: Territory, attackingArmiesNumber: int):
        self.timer.pauseTimer()

        if attackingTerritory.getArmiesNumber()-attackingArmiesNumber < 1:
            raise Exception("Non rimarrebbe nessuna armata nel territorio d'attacco")
            return
        if attackingArmiesNumber > 3:
            raise Exception("Si sta attaccando con troppe armate")
            return

        self.currentAttack = Attack(attackingTerritory, defendingTerritory, attackingArmiesNumber)

    def fight(self, defendingArmiesNumber: int):
        print("Facciamo sto fight")
        if defendingArmiesNumber > 3:
            raise Exception("Non puoi difendere con piu di 3 armate)")

        numeroArmateNelTerrDiDifesa = self.getCurrentAttack().getDefendingTerritory().getArmiesNumber()
        if numeroArmateNelTerrDiDifesa < defendingArmiesNumber:
            raise Exception(f'Non si disponde di {defendingArmiesNumber} nel territorio in difesa')

        self.currentAttack.setDefendingArmies(defendingArmiesNumber)

        self.currentAttack.calculateResult()

        self.attacks.append(self.currentAttack)

        self.currentAttack = None

        self.timer.resumeTimer(self.emptyTimerFunction)
