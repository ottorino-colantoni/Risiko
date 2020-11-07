from django.test import TestCase
from Risiko.Model import Player, classicBoardBuilder , Board, Round
import random

def setUP():
    player1 = Player.Player("Livioski", "blu")
    player2 = Player.Player("Carlatt", "orange")
    player3 = Player.Player("bigFabbro", "yellow")
    player4 = Player.Player("zar", "red")
    players =[player1, player2, player3, player4]
    classicBuilder1 = classicBoardBuilder.classicBoardBuilder()
    Board.Board.setBoardBuilder(classicBuilder1)
    board1 = Board.Board.getInstance()
    for continent in board1.getContinentMap():
        for territory in board1.getContinentMap()[continent].getContinentTerritory():
            board1.getContinentMap()[continent].getContinentTerritory()[territory].setArmiesNumber(random.randrange(1, 8))
            board1.getContinentMap()[continent].getContinentTerritory()[territory].setOwner(random.choice(players))

    return board1


class TestRound(TestCase):

    def test_round(self):
        board = setUP()
        player4 = Player.Player("zar", "red")
        player1 = Player.Player("Livioski", "blu")
        player2 = Player.Player("Carlatt", "orange")
        player3 = Player.Player("bigFabbro", "yellow")
        players = [player1, player2, player3, player4]
        board.printBoard()
        print("\n")

        while True:
            turn = Round.Round(random.choice(players))
            print("Il giocatore di turno è: " + str(turn.getRoundPlayer().getNickName()))
            if turn.startCombatPhase():
                returnTerritory = turn.startCombatPhase()
                for territory in returnTerritory:
                    print(territory.getNameID(), end=" ")
                print("\n")
                atk_ter_id = input("Seleziona il territorio dal quale iniziare l'attacco: ")
                listatkTerr = turn.enterAttackingTerritory(atk_ter_id)
                if listatkTerr:
                    for territory in listatkTerr:
                        print(territory.getNameID(), end=" ")
                    print("\n")
                    attackedTerr =input("Seleziona il territorio da attaccare: ")
                    atkAN =input("Seleziona il numero di armate con cui attaccare: ")
                    turn.confirmAttack(atk_ter_id, attackedTerr, int(atkAN))
                    dfnAN = input("Inserisci il numero di armate con cui vuoi difenderti: ")
                    turn.enterDefendingArmies(int(dfnAN))
                    print(turn.getCombatPhase().getAttacks()[-1].getResult().__repr__())
                else:
                    print("Non ci sono territori da attaccare")
            else:
                print(str(turn.getRoundPlayer().getNickName()) + " non ha territori")







