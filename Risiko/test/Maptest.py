from django.test import TestCase
from Risiko.Model import Territory, Continent, Player

class TestContinent(TestCase):

    def test_map_territory(self):
        territory1 = Territory.Territory("Italy", 21)
        territory2 = Territory.Territory("Germania", 15)
        territory3 = Territory.Territory("Francia", 34)
        continent1 = Continent.Continent("Europa")
        player1 = Player.Player("Jade", "blue")
        player2 = Player.Player("Jane", "red")
        territory1.setOwner(player1)
        territory2.setOwner(player1)
        territory3.setOwner(player1)
        continent1.addTerritory(territory1)
        continent1.addTerritory(territory2)
        continent1.addTerritory(territory3)
        territory4 = continent1.findTerritory("Polonia")
        print(territory4)
        print(continent1.isConquered());
        player1Territory = continent1.getPlayerTerritory("Jane")
        print(player1Territory)

