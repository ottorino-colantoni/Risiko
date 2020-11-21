import threading
import pickle
import asyncio
from Risiko.Server.serverEventListener import Eventlistener


async def push_game_state(eventListener, writer):
    try:
        while True:
            message = "keep alive\n"
            writer.write(message.encode())
            await writer.drain()
            await asyncio.sleep(60)

    except asyncio.CancelledError as error:
        print(error)
    '''
    finally:
        socket.close()
    '''

async def update_from_client(eventListener, reader, writer):

        while True:
            data = await reader.read(200)
            data = data.decode("utf-8")
            data_to_send = eventListener.manageRequest(data)
            print(f'in risposta a {data} mando {data_to_send}')
            writer.write(data_to_send.encode())
            await writer.drain()
            await asyncio.sleep(1)



async def main(eventListener, socket):

    reader, writer = await asyncio.open_connection(sock=socket)
    taskB = asyncio.create_task(push_game_state(eventListener, writer))
    taskA = asyncio.create_task(update_from_client(eventListener, reader, writer))

    try:
        await asyncio.wait([taskB, taskA], return_when=asyncio.FIRST_COMPLETED)
    except:
        print("An error occurred")


class clientThread(threading.Thread):

    def __init__(self, socket, socketPlayer=None, game=None):
        threading.Thread.__init__(self)
        self.socket = socket
        self.eventListener = Eventlistener(game, socketPlayer)
        self.game = game

    def run(self):
        # Register the open socket to wait for data.
        asyncio.run(main(self.eventListener, self.socket))










