import threading
import pickle
import asyncio


async def retrieve_data(socket):
    try:
        data = socket.recv(2048).decode()
        return data
    except asyncio.CancelledError as error:
     print(error)


async def send_data(socket):
    socket.send(str.encode("fuck off"))
    return True



async def push_game_state(game, socket):
    try:
        while True:
            await send_data(socket)
            await asyncio.sleep(1)

    except asyncio.CancelledError as error:
        print(error)

    finally:
        socket.close()


async def update_from_client(game, socket):

        while True:
            message = await retrieve_data(socket)
            await asyncio.sleep(1)
            print(message)


async def main(game, socket):

    taskB = asyncio.create_task(push_game_state(game, socket))
    taskA = asyncio.create_task(update_from_client(game, socket))

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
        asyncio.run(main(self.game, self.socket))










