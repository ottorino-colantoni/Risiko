from Risiko.test import roundTest
from Risiko.Model import Player, classicBoardBuilder , Board, Round
import random

class Game:

    __instance = None

    @staticmethod
    def getInstance():
        if Game.__instance == None:
            Game()
        return Game.__instance
    def __init__(self):
        self.connectedPlayer = 0
        self.players = [Player.Player("Zar", "red"), Player.Player("Livioski", "blu")]
        self.playerAddress = {}
        self.board = None
        self.round = None
        Game.__instance = self

    def gameCanStart(self):
        if self.connectedPlayer != 2:
            return False
        else:
            return True

    def startGame(self):
        self.board = roundTest.setUP()
        self.round = Round.Round(random.choice(self.players))

    def changeRoundlayer(self):
        self.round = Round.Round(random.choice(self.players))

