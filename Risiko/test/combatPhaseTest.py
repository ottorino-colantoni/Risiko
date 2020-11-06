from django.test import TestCase

from Risiko.Model.Territory import Territory
from Risiko.Model.combatPhase import combatPhase
import time


class combatPhaseTest(TestCase):
    def test_one_attack(self):
        Italia = Territory("Italia")
        Italia.setArmiesNumber(5)
        Francia = Territory("Francia")
        Francia.setArmiesNumber(5)

        Italia.addNeighbors([Francia])
        Francia.addNeighbors([Italia])

        combatPh = combatPhase(5)
        time.sleep(2)
        combatPh.makeAttack(Italia, Francia, 3)
        time.sleep(2)
        combatPh.fight(2)
