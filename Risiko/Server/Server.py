import socket
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
    server = Server("127.0.0.1", 6455)
    server.startServer(2)

