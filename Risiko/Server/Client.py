import socket
import asyncio
from pynput import keyboard

unlock_input = False

def show_commands():
    print("Se sei di turno puoi scegliere tra i seguenti comandi: \n")
    print("[startCPhase]-[enterAttackingTerritory/<territorioInAttacco>]-[confirmAttack/<territorioInAttacco>/<territorioDifensore>/<armateInAttacco>]")

async def update_from_server(reader):

    while True:
        data = await reader.read(200)
        data = data.decode("utf-8")
        print(data)
        await asyncio.sleep(0.1)

async def send_message(writer):
    global unlock_input
    try:
        while True:
            if unlock_input:
                mess = input("inserisci comando")
                if mess == "help":
                    show_commands()
                elif mess == "annulla":
                    pass
                else:
                    writer.write(mess.encode())
                    await writer.drain()
                unlock_input = False
            await asyncio.sleep(0.1)

    except asyncio.CancelledError as error:
        print(error)

async def main(serverIP, serverPort_P):

    reader, writer = await asyncio.open_connection(serverIP, serverPort_P)
    taskB = asyncio.create_task(send_message(writer))
    taskA = asyncio.create_task(update_from_server(reader))

    try:
        await asyncio.wait([taskB, taskA], return_when=asyncio.FIRST_COMPLETED)
    except:
        print("An error occurred")


def on_press(key):
    global unlock_input
    try:
        if key.char == "e":
            unlock_input = True
    except:
        pass

class Client:

    def __init__(self, _serverIP: str, _serverPort: int ):
        self.serverIP = _serverIP
        self.serverPort_P = _serverPort

    def run(self):
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        asyncio.run(main(self.serverIP, self.serverPort_P))


if __name__ == '__main__':

    client = Client('127.0.0.1', 6455)
    client.run()






