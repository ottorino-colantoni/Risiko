from .Territory import Territory
from .Timer import Timer

class combatPhase(object):
    def __init__(self, combatTime):
        self.timer = Timer.getInstance()
        self.timer.setRemainingTime(combatTime)
        self.timer.startTimer()
        self.attacks = []
    def makeAttack(self,attackingTerritory: Territory, defendingTerritory: Territory, attackingArmiesNumber: int):
        # TODO: implement here
        self.timer.pauseTimer()
    def fight(self, defendingArmiesNumber: int):
        # TODO: implement here
        self.timer.resumeTimer()
