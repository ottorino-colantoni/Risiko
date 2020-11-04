from django.test import TestCase
from Risiko.Model import Player, Territory, Attack

class attackTest(TestCase):

    def createTerritories(self):
        player1 = Player.Player("John", "blu")
        player2 = Player.Player("Jade", "yellow")
        territory1 = Territory.Territory("Italy", 19)
        territory2 = Territory.Territory("Germania", 32)
        territory1.addNeighbords(territory2)
        territory2.addNeighbords(territory1)
        territory1.setOwner(player1)
        territory2.setOwner(player2)
        #print(str(territory2.getNameID()) + " " + str(territory1.getOwnerID()) + " " + str(territory1.getArmiesNumber()))
        territory1.modifyTerritoryArmies(8)
        #print(str(territory1.getNameID()) + " " + str(territory1.getOwnerID()) + " " + str(territory1.getArmiesNumber()))
        #print(territory1.hasNeighbord(territory2))
        territory1.printNeighbords()
        territory2.printNeighbords()
        return territory1, territory2

    def testTheAttack(self):
        ter1, ter2 = self.createTerritories()
        atk = Attack.Attack(ter1, ter2, 3)
        defArmies = 2
        atk.setDefendingArmies(defArmies)
        res = atk.calculateResult()
        print(res)