import threading
import pickle
import asyncio


async def push_game_state(game, writer):
    try:
        while True:
            message = "PROVA"
            writer.write(message.encode())
            await writer.drain()
            await asyncio.sleep(1)

    except asyncio.CancelledError as error:
        print(error)
    '''
    finally:
        socket.close()
    '''

async def update_from_client(game, reader):

        while True:
            data = await reader.read(100)
            # EventListener.manageRequest(data)
            if data == "ciao":
                print(f'ricevuto {data} da ')
            await asyncio.sleep(1)



async def main(game, socket):

    reader, writer = await asyncio.open_connection(sock=socket)
    taskB = asyncio.create_task(push_game_state(game, writer))
    taskA = asyncio.create_task(update_from_client(game, reader))

    try:
        await asyncio.wait([taskB, taskA], return_when=asyncio.FIRST_COMPLETED)
    except:
        print("An error occurred")


class clientThread(threading.Thread):

    def __init__(self, socket, player=None, game=None, eventlistner=None):
        threading.Thread.__init__(self)
        self.socket = socket
        self.player = player
        self.eventListener = eventlistner
        self.game = game

    def run(self):
        # Register the open socket to wait for data.
        #reader, writer = asyncio.open_connection(sock=self.socket)
        asyncio.run(main(self.game, self.socket))










