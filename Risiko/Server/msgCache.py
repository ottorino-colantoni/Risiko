import queue


class MsgCache:
    def __init__(self):
        self.msgQueue = queue.Queue(maxsize=0)

    def putMsg(self, msg, dest):
        self.msgQueue.put([msg, dest])

    def checkMsg(self, player):
        isMine = False
        if self.msgQueue[0][1] == player:
            isMine = True
        return isMine

    def getMsg(self):
        return self.msgQueue.get()[0]
