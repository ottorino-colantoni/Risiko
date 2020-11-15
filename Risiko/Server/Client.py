import socket
import pickle
#import zmq
#import json


class Client:

    def __init__(self, _serverIP: str, _serverPort: int ):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverIP = _serverIP
        self.serverPort_P = _serverPort


    def connectToServer(self):
        try:
            self.socket.connect((self.serverIP, self.serverPort_P))
        except socket.error as error:
            print(error)
            return False
        return True

if __name__ == '__main__':

    client = Client('127.0.0.1', 6455)
    if client.connectToServer():

     while True:
        try:
            data = client.socket.recv(2048).decode()
            print(data)
            message = input("inserisci il messaggio: ")

        except:
            pass






