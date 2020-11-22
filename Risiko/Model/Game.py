from random import choice, random
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
        self.started = False

        #dizionario chiave = giocatore, valore = socketAssociata
        self.playerSocket = {}

    def set_player_socket(self,player,socket):

        self.playerSocket[f'{player.getNickName()}'] = socket

    def get_player_socket(self):
        return self.playerSocket

    #TODO: to be modified
    def build_board(self):
        classicBuilder1 = classicBoardBuilder()
        Board.setBoardBuilder(classicBuilder1)
        board1 = Board.getInstance()
        for continent in board1.getContinentMap():
            for territory in board1.getContinentMap()[continent].getContinentTerritory():
                board1.getContinentMap()[continent].getContinentTerritory()[territory].setArmiesNumber(5)
                board1.getContinentMap()[continent].getContinentTerritory()[territory].setOwner(choice(self.players))

    def makeTurn(self):
        if self.rounds == []:
            new_round = Round(self.players[0])
            self.rounds.append(new_round)
        else:
            #TODO: Fare in modo che cicli su tutti i giocatori uno per uno
            last_round_player = self.rounds[-1].getRoundPlayer()
            new_round_player = self.players[(self.players.index(last_round_player) + 1) % len(self.players)]
            new_round = Round(new_round_player)
            self.rounds.append(new_round)

    #TODO : to be modified?
    def gameStart(self):
        if len(self.playerSocket) == len(self.players):
            self.build_board()
            self.makeTurn()
            self.started = True
        else:
            return False

    def gameStarted(self):
        return self.started

    def getCurrentRound(self):
        return self.rounds[-1]

    #TODO : it is necessary to understand what to send
    def toJason(self):
        pass

    #TODO : what parameters are usefull to create the checksum
    def __hash__(self):
        pass









