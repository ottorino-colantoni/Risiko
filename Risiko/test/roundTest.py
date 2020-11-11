from django.test import TestCase
from Risiko.Model import Player, classicBoardBuilder , Board, Round
import random


def selectAttackingTerritoryRoutine(listPossibleTerr):

    possibleAttackingTerritories = []
    for i in range(len(listPossibleTerr)):
        possibleAttackingTerritories.append(listPossibleTerr[i].getNameID())

    wrongTerritory = True
    while wrongTerritory:
        attackingTerritory = input("Seleziona il territorio d'attacco (digita EXIT se vuoi invece uscire)")
        if attackingTerritory in possibleAttackingTerritories:
            wrongTerritory = False
        else:
            print("Territorio d'attacco non valido")
    return attackingTerritory



def selectAttackedTerritoryRoutine(listatkTerr):
    idsAttackableTerritories = []
    for i in range(len(listatkTerr)):
        idsAttackableTerritories.append(listatkTerr[i].getNameID())

    wrongTerritory = True
    while wrongTerritory:
        attackedTerr = input("Seleziona il territorio da attaccare (digita EXIT se vuoi invece uscire)")
        if attackedTerr in idsAttackableTerritories:
            wrongTerritory = False
        else:
            print("Territorio da attaccare non valido")
    return attackedTerr

def insertAtkArmiesRoutine():
    wrongArmies = True
    while wrongArmies:
        armies = int(input("Seleziona il numero di armate con cui attaccare: "))
        if armies <= 3:
            wrongArmies = False
        else:
            print("Numero di armate non valido")
    return armies

def insertDefArmiesRoutine():
    wrongArmies = True
    while wrongArmies:
        armies = int(input("Seleziona il numero di armate con cui difenderti: "))
        if armies <= 3:
            wrongArmies = False
        else:
            print("Numero di armate non valido")
    return armies


def selectAttackArmiesNumber(listatkTerr):
    idsAttackableTerritories = []
    for i in range(len(listatkTerr)):
        idsAttackableTerritories.append(listatkTerr[i].getNameID())

    wrongTerritory = True
    while wrongTerritory:
        attackedTerr = input("Seleziona il territorio da attaccare - digita EXIT se vuoi invece uscire")
        if attackedTerr in idsAttackableTerritories:
            wrongTerritory = False
    return attackedTerr


def setUP():
    player1 = Player.Player("Livioski", "blu")
    #player2 = Player.Player("Carlatt", "orange")
    #player3 = Player.Player("bigFabbro", "yellow")
    player4 = Player.Player("Zar", "red")
    players =[player1, player4]
    classicBuilder1 = classicBoardBuilder.classicBoardBuilder()
    Board.Board.setBoardBuilder(classicBuilder1)
    board1 = Board.Board.getInstance()
    for continent in board1.getContinentMap():
        for territory in board1.getContinentMap()[continent].getContinentTerritory():
            board1.getContinentMap()[continent].getContinentTerritory()[territory].setArmiesNumber(5)
            board1.getContinentMap()[continent].getContinentTerritory()[territory].setOwner(random.choice(players))

    return board1


class TestRound(TestCase):

    def test_round(self):
        board = setUP()
        player4 = Player.Player("Zar", "red")
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
                print("Puoi muovere un attacco dai seguenti territori: ")
                for territory in returnTerritory:
                    print(f'[{territory.getNameID()}]')
                print("\n")

                atk_ter_id = selectAttackingTerritoryRoutine(returnTerritory)

                listAtkableTerr = turn.enterAttackingTerritory(atk_ter_id)

                if listAtkableTerr:
                    print(f'Da {atk_ter_id} puoi attaccare i seguenti: ')
                    for territory in listAtkableTerr:
                        print(f'[{territory.getNameID()}]')

                    attackedTerr = selectAttackedTerritoryRoutine(listAtkableTerr)

                    atkAN = insertAtkArmiesRoutine()

                    try:
                        turn.confirmAttack(atk_ter_id, attackedTerr, int(atkAN))
                    except:
                        print("Errore nelle armate in attacco")

                    dfnAN = insertDefArmiesRoutine()

                    turn.enterDefendingArmies(dfnAN)


                    print(turn.getCombatPhase().getAttacks()[-1].getResult().__repr__())
                else:
                    print("Non ci sono territori da attaccare")
            else:
                print(str(turn.getRoundPlayer().getNickName()) + " non ha territori, fase di combattimento finita")







