import socket
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
                sent = self.socket.send(msg[totalsent:].encode())
                if sent == 0:
                    raise RuntimeError
                totalsent += sent
        except socket.error as error:
            print(error)
            return False
        return True

    def receiveResponse(self):
        try:
            data = self.socket.recv(4096).decode()
            return data
        except socket.error as error:
            print(error)
            return None


if __name__ == '__main__':

    client = Client('127.0.0.1', 5555)
    if client.connectToServer():
        msg = ''
        while msg != 'bye':
                msg = input('Quale messaggio vuoi inviare?')
                if client.sendRequest(msg):
                    print(client.receiveResponse())





