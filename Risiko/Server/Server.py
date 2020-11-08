import socket
import threading
import sys

class Server:

    def __init__(self, _serverIP: str, _serverPort: int):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverIP = _serverIP
        self.serverPort = _serverPort

    def startServer(self, maxNumClient: int):
        try:
            self.socket.bind((self.serverIP, self.serverPort))
            self.socket.listen(maxNumClient)
            print('Server started, waiting for connection...')
            while 1:
                (SocketClient, address) = self.socket.accept()
                newClientThread = clientThread(SocketClient, address)
                newClientThread.start()

        except socket.error as error:
            print(error)



class clientThread(threading.Thread):

    def __init__(self, _clientSocket, _clientAddress):
        threading.Thread.__init__(self)
        self.clientAddress = _clientAddress
        self.clientSocket = _clientSocket
        msg = ''

    def run(self):
        print('New client is arrived!')
        while True:
            data = self.clientSocket.recv(2048)
            msg = data.decode()
            if msg == 'bye':
                break
            print(msg)
            replyMessage = 'Message received'
            self.clientSocket.send(replyMessage.encode())
        print("Client at ", self.clientAddress, " disconnected...")



if __name__ == '__main__':

    server = Server('127.0.0.1', 5555)
    server.startServer(3)