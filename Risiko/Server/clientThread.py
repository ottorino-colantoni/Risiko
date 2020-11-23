import threading
import pickle
import asyncio
from Risiko.Server.requestHandler import RequestHandler


async def push_game_state(msgCache, playerID, writer):
    try:
        while True:
            if msgCache.checkMsg(playerID):
                msgToSend = msgCache.getMsg()
                writer.write(msgToSend.encode())
                await writer.drain()
            await asyncio.sleep(0.2)

    except asyncio.CancelledError as error:
        print(error)

async def update_from_client(requestHandler, reader, writer):

        while True:
            data = await reader.read(200)
            data = data.decode("utf-8")
            requestHandler.manageRequest(data)
            await writer.drain()
            await asyncio.sleep(1)

async def main(requestHandler, socket, playerID, msgCache):

    reader, writer = await asyncio.open_connection(sock=socket)
    taskB = asyncio.create_task(push_game_state(msgCache, playerID,  writer))
    taskA = asyncio.create_task(update_from_client(requestHandler, reader, writer))

    try:
        await asyncio.wait([taskB, taskA], return_when=asyncio.FIRST_COMPLETED)
    except:
        print("An error occurred")

class clientThread(threading.Thread):

    def __init__(self, socket, msgCache, playerID, game):
        threading.Thread.__init__(self)
        self.socket = socket
        self.playerID = playerID
        self.requestHandler = RequestHandler(game, playerID, msgCache)
        self.game = game
        self.msgCache = msgCache

    def run(self):
        # Register the open socket to wait for data.
        asyncio.run(main(self.requestHandler, self.socket, self.playerID, self.msgCache))