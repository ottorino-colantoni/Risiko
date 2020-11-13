import socket
import pickle
import threading
from pynput.keyboard import Key, Listener

import time

import sys


def on_press(key):
    try:
        if key.char == 'e':
           client.message_for_server = True
    except:
        pass

def Commands():
    print("Puoi utilizzare i seguenti comandi: \n")
    print("# startCPhase =  per iniziare la fase di combattimento N.B: devi essere il giocatore di turno ")

class Client:

    def __init__(self, _serverIP: str, _serverPort: int):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverIP = _serverIP
        self.serverPort = _serverPort
        self.connected = False
        self.message_for_server = False
        self.message_from_server = False

    def connectToServer(self):
        try:
            self.socket.connect((self.serverIP, self.serverPort))
            self.connected = True
        except socket.error as error:
            print(error)
            return False
        return True

    def sendRequest(self, msg: str):
        try:
            totalsent = 0
            while totalsent < len(msg):
                sent = self.socket.send(str.encode(msg[totalsent:]))
                if sent == 0:
                    raise RuntimeError
                totalsent += sent
        except socket.error as error:
            print(error)
            return False
        return True


    def wait_for_message(self):
        while self.connected:
            global data_retrieved
            try:
                data_from_server = self.socket.recv(2048).decode()
                data_retrieved += data_from_server
                if "/0" in data_retrieved:
                    data_retrieved = data_retrieved.replace("/0", "\n")
                    data_from_server = ""
                    self.message_from_server = True


            except socket.error as error:
                print(error)



if __name__ == '__main__':

    client = Client('127.0.0.1', 5555)
    data_retrieved = ""
    data_to_send = None
    listner = Listener(on_press=on_press)
    listner.start()
    if client.connectToServer():
        output = threading.Thread(target=client.wait_for_message)
        output.start()

        run = True
        while run:

            if client.message_from_server:
                print(data_retrieved)
                data_retrieved = ""
                client.message_from_server = False

            if client.message_for_server:
                data = input("Iserisci l'operazione")
                if data == "Commands":
                    Commands()
                    client.message_for_server = False
                elif data == "annulla":
                    client.message_for_server = False
                else:
                    client.socket.send(str.encode(data))
                    client.message_for_server = False






'''
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
               elif message_from_server == "toALL":
                   message_from_server = client.receiveResponse()
                   print(message_from_server)


               # Routine if you are not the round_player
               else:
                   message_from_server = client.receiveResponse()
                   print(message_from_server)
'''