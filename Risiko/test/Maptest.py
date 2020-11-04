from django.test import TestCase
from Risiko.Model import Territory, Continent, Player

class TestContinent(TestCase):

    def test_map_territory(self):
        territory1 = Territory.Territory("Italy", 21)
        territory2 = Territory.Territory("Germania", 15)
        territory3 = Territory.Territory("Francia", 34)
        continent1 = Continent.Continent("Europa")
        continent1.addTerritory(territory1)
        continent1.addTerritory(territory2)
        continent1.addTerritory(territory3)
        territory4 = continent1.findTerritory("Polonia")
        print(territory4)

