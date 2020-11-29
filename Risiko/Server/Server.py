import socket
from Risiko.Model.Player import Player
from Risiko.Model.Game import Game
from Risiko.Server.clientThread import clientThread
from Risiko.Server.msgCache import MsgCache

class Server:

    def __init__(self, server_ip, server_port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverIP = server_ip
        self.serverPort = server_port

    def startServer(self, maxNumClient: int, game):

            print('Server started, waiting for connection...')
            self.socket.bind((self.serverIP, self.serverPort))
            self.socket.listen(maxNumClient)

            count_player = 0
            while True:
                conn, addr = self.socket.accept()
                game.set_player_socket(players[count_player], conn)
                client_thread = clientThread(conn, msgCache, players[count_player].getNickName(), game)
                client_thread.start()
                #la partita non inizierà se non ci sono tanti sockets quanti i players
                game.gameStart()
                count_player += 1


if __name__ == '__main__':

    #TODO : only for test model
    player1 = Player("Zar", "red")
    player2 = Player("Livioski", "blu")
    #player3 = Player("Carlatt", "orange")
    #player4 = Player("bigFabbro", "yellow")
    msgCache = MsgCache()
    players = [player1, player2]
    game = Game(players)


    #TODO : to be modified
    server = Server("127.0.0.1", 6455)
    server.startServer(2, game)

