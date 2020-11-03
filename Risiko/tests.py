from django.test import TestCase
from .Models import RiskTimer, Die, diceShaker
from threading import Timer
import time

# Run all the tests in the animals.tests module
# test animals.tests

# Run all the tests found within the 'animals' package
# ./manage.py test animals

# Run just one test case
# ./manage.py test animals.tests.AnimalTestCase

# Run just one test method
# ./manage.py test animals.tests.AnimalTestCase.test_animals_can_speak

#################### test function for RiskTimer #####################
class RiskTimerTests(TestCase):

   def helloWorld(self):
       print("hellWorld")


   def test_verify_remaining_time_and_singleton_instance(self):

       test_timer = RiskTimer.RiskTimer.getInstance()
       test_timer.setRemainingTime(10)
       test_timer.startTimer(self.helloWorld)
       print(test_timer.getRemainingTime())
       print(test_timer.getStartedAt())
       time.sleep(4)
       test_timer.pauseTimer()
       test_timer2 = RiskTimer.RiskTimer.getInstance()
       print(test_timer.getRemainingTime())
       print(test_timer2.getRemainingTime())
       test_timer.resumeTimer(self.helloWorld)


   def test_verify_stop_function(self):
        test_timer = RiskTimer.RiskTimer.getInstance()
        test_timer.setRemainingTime(10)
        test_timer.startTimer(self.helloWorld)
        test_timer.stopTimer()


######### Test function for Die #####################
class DieTests(TestCase):

    def test_roll_function(self):
        die1 = Die.Die()
        die2 = Die.Die()
        die1.rollDie()
        die2.rollDie()
        print(die1.getFaceValue())
        print(die2.getFaceValue())


############## Test function for diceShaker ########
class diceShakerTests(TestCase):

    def test_roll_dice_function(self):
        riskDiceShaker = diceShaker.diceShaker.getInstance()
        riskDiceShaker.rollDice(3)
        results = riskDiceShaker.getSortDiceResults()
        print(results)
