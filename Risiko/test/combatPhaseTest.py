from django.test import TestCase

from Risiko.Model.Territory import Territory
from Risiko.Model.combatPhase import combatPhase


class combatPhaseTest(TestCase):
    def test_one_attack(self):
        Italia = Territory("Italia", 5)
        Francia = Territory("Francia", 3)

        Italia.addNeighbords(Francia)
        Francia.addNeighbords(Italia)

        combatPh = combatPhase(60)
        combatPh.makeAttack(Italia, Francia, 3)
        combatPh.fight(2)
