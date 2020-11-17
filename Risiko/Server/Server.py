import socket
from Risiko.Model.Player import Player
from Risiko.Model.Game import Game
from Risiko.Server.clientThread import clientThread


class Server:

    def __init__(self, server_ip, server_port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverIP = server_ip
        self.serverPort = server_port

    def startServer(self, maxNumClient: int):

            print('Server started, waiting for connection...')
            self.socket.bind((self.serverIP, self.serverPort))
            self.socket.listen(maxNumClient)

            while True:
                conn, addr = self.socket.accept()
                client_thread = clientThread(conn)
                client_thread.start()



if __name__ == '__main__':

    #TODO : only for test model

    player4 = Player("Zar", "red")
    player1 = Player("Livioski", "blu")
    player2 = Player("Carlatt", "orange")
    player3 = Player("bigFabbro", "yellow")
    players = [player1, player2, player3, player4]
    game = Game(players)



    #TODO : to be modified

    server = Server("127.0.0.1", 6455)
    server.startServer(2)

