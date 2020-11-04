from .Timer import Timer

class combatPhase(object):
    def __init__(self, combatTime):
        self.timer = Timer.getInstance()
        self.timer.setRemainingTime(combatTime)
        self.timer.startTimer()
        self.attacks = []
    def makeAttack(self,attackingTerritory, defendingTerritory, attackingArmiesNumber):
        # TODO: implement here
        self.timer.pauseTimer()
    def fight(self, defendingArmiesNumber):
        # TODO: implement here
        self.timer.resumeTimer()
