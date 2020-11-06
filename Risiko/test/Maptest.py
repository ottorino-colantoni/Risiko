from django.test import TestCase
from Risiko.Model import Territory, Continent, Player, boardBuilder, classicBoardBuilder, Board

class TestContinent(TestCase):

    def test_map_territory(self):
        territory1 = Territory.Territory("Italy")
        territory2 = Territory.Territory("Germania")
        territory3 = Territory.Territory("Francia")
        continent1 = Continent.Continent("Europa")
        territory1.setArmiesNumber(15)
        territory1.setArmiesNumber(16)
        territory1.setArmiesNumber(17)
        player1 = Player.Player("Jade", "blue")
        player2 = Player.Player("Jane", "red")
        territory1.setOwner(player1)
        territory2.setOwner(player1)
        territory3.setOwner(player1)
        continent1.addTerritory([territory1])
        continent1.addTerritory([territory2])
        continent1.addTerritory([territory3])
        territory4 = continent1.findTerritory("Polonia")
        print(territory4)
        print(continent1.isConquered());
        player1Territory = continent1.getPlayerTerritory("Jane")
        print(player1Territory)


class TestMap(TestCase):

    def test_buildMap(self):
        classicBoarBuilder1 = classicBoardBuilder.classicBoardBuilder()
        Board.Board.setBoardBuilder(classicBoarBuilder1)
        board1 = Board.Board.getInstance()
        board1.printBoard()
