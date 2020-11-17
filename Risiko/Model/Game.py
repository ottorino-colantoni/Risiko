from random import random
import hashlib
from Risiko.Model.Board import Board
from Risiko.Model.Round import Round
from Risiko.Model.classicBoardBuilder import classicBoardBuilder


class Game:

    def __init__(self, players: []):
        self.id = random()
        self.players = players
        self.rounds = []
        self.checksum = None

        #TODO : only for test
        self.playerSocket = {}


    #TODO: to be modified
    def build_board(self):
        classicBuilder1 = classicBoardBuilder()
        Board.setBoardBuilder(classicBuilder1)
        board1 = Board.getInstance()
        for continent in board1.getContinentMap():
            for territory in board1.getContinentMap()[continent].getContinentTerritory():
                board1.getContinentMap()[continent].getContinentTerritory()[territory].setArmiesNumber(5)
                board1.getContinentMap()[continent].getContinentTerritory()[territory].setOwner(random.choice(self.players))


    def makeTurn(self):
        if self.rounds == []:
            new_round = Round(random.choice(self.players))
            self.rounds.append(new_round)
        else:
            new_round = Round(self.players[self.rounds.index(self.rounds[-1].getRoundPlayer() + 1)])
            self.rounds.append(new_round)

    #TODO : to be modified?
    def game_can_start(self):
        if len(self.playerSocket) == len(self.players):
            return True
        else:
            return False


    #TODO : it is necessary to understand what to send
    def toJason(self):
        pass

    #TODO : what parameters are usefull to create the checksum
    def __hash__(self):
        pass









