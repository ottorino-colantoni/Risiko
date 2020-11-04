from django.test import TestCase
from Risiko.Model import Player, Territory, Attack

class attackTest(TestCase):

    def createTerritories(self):
        player1 = Player.Player("John", "blu")
        player2 = Player.Player("Jade", "yellow")
        territory1 = Territory.Territory("Italia", 10)
        territory2 = Territory.Territory("Germania", 1)
        territory1.addNeighbords(territory2)
        territory2.addNeighbords(territory1)
        territory1.setOwner(player1)
        territory2.setOwner(player2)
        #print(str(territory2.getNameID()) + " " + str(territory1.getOwnerID()) + " " + str(territory1.getArmiesNumber()))
        #territory1.modifyTerritoryArmies(8)
        #print(str(territory1.getNameID()) + " " + str(territory1.getOwnerID()) + " " + str(territory1.getArmiesNumber()))
        #print(territory1.hasNeighbord(territory2))
        #territory1.printNeighbords()
        #territory2.printNeighbords()
        return territory1, territory2

    def testTheAttack(self):
        ter1, ter2 = self.createTerritories()
        atk = Attack.Attack(ter1, ter2, 1)
        defArmies = 1
        atk.setDefendingArmies(defArmies)
        print(f'Nel territorio attaccante "{ter1.getNameID()}" prima dell\'attacco ci sono {ter1.getArmiesNumber()} armate')
        print(f'Nel territorio difensore "{ter2.getNameID()}" prima dell\'attacco ci sono {ter2.getArmiesNumber()} armate')

        res = atk.calculateResult()
        print(res)
        print(f'In "{ter1.getNameID()}" dopo l\'attacco ci sono {ter1.getArmiesNumber()} armate')
        print(f'In "{ter2.getNameID()}" dopo l\'attacco ci sono {ter2.getArmiesNumber()} armate')
