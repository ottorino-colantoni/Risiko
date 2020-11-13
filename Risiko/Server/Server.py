import socket
import threading
import pickle
import time
import sys
from Risiko.Server.Game import Game
from Risiko.Server.serverEventLisner import Eventlistner


class Server:

    def __init__(self, _serverIP: str, _serverPort: int, evenLis):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverIP = _serverIP
        self.serverPort = _serverPort
        self.game = Game.getInstance()
        self.eventLisner = evenLis

    def createRoom(self):
        self.game.startGame()


    def startServer(self, maxNumClient: int, evenLis):
        try:
            self.socket.bind((self.serverIP, self.serverPort))
            self.socket.listen(maxNumClient)
            print('Server started, waiting for connection...')
            while 1:
                (SocketClient, address) = self.socket.accept()
                newClientThread = clientThread(SocketClient, address, self.game.players[self.game.connectedPlayer].getNickName(), evenLis)
                self.game.playerAddress[self.game.players[self.game.connectedPlayer].getNickName()] = SocketClient
                self.game.connectedPlayer += 1
                newClientThread.start()



        except socket.error as error:
            print(error)

class clientThread(threading.Thread):

    def __init__(self, _clientSocket, _clientAddress, player, eventlistner):
        threading.Thread.__init__(self)
        self.clientAddress = _clientAddress
        self.clientSocket = _clientSocket
        self.player = player
        self.eventListener = eventlistner

    def run(self):

        self.clientSocket.send(str.encode("Welcome to Server" + "/0"))

        while True:

            data_from_client = self.clientSocket.recv(2048).decode()
            data_for_client = self.eventListener.splitString(data_from_client)
            self.clientSocket.send(str.encode(data_for_client))



if __name__ == '__main__':

    ev = Eventlistner()
    server = Server('127.0.0.1', 5555, ev)
    server.createRoom()
    ev.setGame(server.game)
    server.startServer(2, ev)
























"""

if not server.game.gameCanStart():
    replyMessage = "Waitning for more Player"
    self.clientSocket.send(pickle.dumps(str(replyMessage)))
    time.sleep(1)

elif self.player == server.game.round.getRoundPlayer().getNickName():
    # CombatPhase Strategy
    self.clientSocket.send(pickle.dumps(str("StartCPhase")))
    self.clientSocket.send(pickle.dumps(str("Enter 'Start' to begin the combat phase or 'Exit' to finish the turn")))
    playerChoice = pickle.loads(self.clientSocket.recv(4096))
    if playerChoice == "Start":

        # Loop per l'invio dei territorio da cui può attaccare
        returnTerritory = server.game.round.startCombatPhase()
        self.clientSocket.send(pickle.dumps(str("Puoi muovere un attacco dai seguenti territori: ")))
        for territory in returnTerritory:
            self.clientSocket.send(pickle.dumps(str(territory.getNameID() + "  " + str((territory.getArmiesNumber())))))
        # to close loop on client side
        self.clientSocket.send(pickle.dumps(str("finish")))
        # Selected AttackingTerritories
        selectedAttackingTerritories = pickle.loads(self.clientSocket.recv(4096))
        print(selectedAttackingTerritories)

        # Loop per inviare tutti i territori che si possono attaccare
        listAtkableTerr = server.game.round.enterAttackingTerritory(selectedAttackingTerritories)
        for territory in listAtkableTerr:
            self.clientSocket.send(pickle.dumps(str(territory.getNameID() + "  " + str((territory.getArmiesNumber())))))
        # to close loop on client side
        self.clientSocket.send(pickle.dumps(str("finish")))

        #recive the territory under attack
        dfnTerritory = pickle.loads(self.clientSocket.recv(2048))
        print(dfnTerritory)

        # Select the army number for begin the attack(attacker Armies)
        self.clientSocket.send(pickle.dumps("Seleziona il numero di armate con cui vuoi attaccare:"))
        armiesNumber = pickle.loads(self.clientSocket.recv(4096))
        dfnplayer = server.game.round.confirmAttack(selectedAttackingTerritories, dfnTerritory, int(armiesNumber))

        #contact defending player for ask armies number
        defsocket = server.game.playerAddress[dfnplayer]
        defsocket.send(pickle.dumps("Under Attack"))
        defsocket.send(pickle.dumps("Sei sotto attacco: " + str(dfnTerritory)))
        dfnArmiesNumber = pickle.loads(defsocket.recv(2048))

        # Final scheme for calculate results and send this to all player
        server.game.round.enterDefendingArmies(int(dfnArmiesNumber))
        for socket in server.game.playerAddress:
            server.game.playerAddress[socket].send(pickle.dumps("toALL"))
            server.game.playerAddress[socket].send(pickle.dumps(server.game.round.getCombatPhase().getAttacks()[-1].getResult().__repr__()))

    else:
        self.clientSocket.send(pickle.dumps("Questo è il turno di :" + str(server.game.round.getRoundPlayer().getNickName())))
        server.game.changeRoundlayer()

else:
    self.clientSocket.send(pickle.dumps("Questo è il turno di: " + str(server.game.round.getRoundPlayer().getNickName())))
"""