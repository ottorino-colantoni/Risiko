import socket
import pickle
import time

import sys


class Client:

    def __init__(self, _serverIP: str, _serverPort: int):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverIP = _serverIP
        self.serverPort = _serverPort

    def connectToServer(self):
        try:
            self.socket.connect((self.serverIP, self.serverPort))
        except socket.error as error:
            print(error)
            return False
        return True

    def sendRequest(self, msg: str):
        try:
            totalsent = 0
            while totalsent < len(msg):
                sent = self.socket.send(pickle.dumps(msg[totalsent:]))
                if sent == 0:
                    raise RuntimeError
                totalsent += sent
        except socket.error as error:
            print(error)
            return False
        return True

    def receiveResponse(self):
        try:
            data = pickle.loads(self.socket.recv(4096))
            return data
        except socket.error as error:
            print(error)
            return None


if __name__ == '__main__':

    client = Client('127.0.0.1', 5555)
    if client.connectToServer():
        run = True
        while run:
            try:
                message_from_server = client.receiveResponse()
                # Start Combat Phase Routine
                if message_from_server == "StartCPhase":
                    # Receive the message "Enter 'Start' to ......"
                    message_from_server = client.receiveResponse()
                    print(message_from_server)
                    #Send message Start or Exit"
                    message_to_server = input("Seleziona l'operazione: ")
                    client.sendRequest(message_to_server)
                    message_from_server = client.receiveResponse()
                    print(message_from_server)
                    # Loop for print all the possible territory to attack
                    message_from_server = client.receiveResponse()
                    while message_from_server != "finish":
                        print(message_from_server)
                        message_from_server = client.receiveResponse()


                    #Select un territorio da cui attaccare
                    message_to_server = input("Inserisci un territorio da cui attaccare : ")
                    client.sendRequest(message_to_server)

                    # Loop for print all the possible attackable territories
                    message_from_server = client.receiveResponse()
                    while message_from_server != "finish":
                        print(message_from_server)
                        message_from_server = client.receiveResponse()

                    # Seleziona un territorio da attaccare
                    atk_territory = input("Inserisci un territorio da attaccare: ")
                    client.sendRequest(atk_territory)


                    # Selection armies Number
                    message_from_server = client.receiveResponse()
                    print(message_from_server)
                    message_to_server = input("Inserisci il numero Armate: ")
                    client.sendRequest(message_to_server)

                #routine if you are under attack
                elif message_from_server == "Under Attack":
                    message_from_server = client.receiveResponse()
                    print(message_from_server)
                    CdfnArmy = input("Inserisci il numero di armate con cui vuoi difenderti: ")
                    client.sendRequest(CdfnArmy)

                # routine if the message is to all
                elif message_from_server == "toALL" :
                    message_from_server = client.receiveResponse()
                    print(message_from_server)


                # Routine if you are not the round_player
                else:
                    message_from_server = client.receiveResponse()
                    print(message_from_server)

            except:
                pass

