from threading import Timer as thredingTimer
import time


class Timer:

    __instance = None

    @staticmethod
    def getInstance():
        if Timer.__instance == None:
            Timer()
        return Timer.__instance

    def __init__(self):
        if Timer.__instance != None:
            raise Exception("This class is a Singleton")
        else:
            self.__timeRemaining = None
            self.__startedAt = None
            self.__phaseTimer = None
            Timer.__instance = self

    def startTimer(self, method):

        self.__startedAt = time.time()
        self.__phaseTimer = thredingTimer(self.__timeRemaining, method)
        self.__phaseTimer.start()

    def pauseTimer(self):
        self.__timeRemaining = self.__timeRemaining - (time.time() - self.__startedAt)
        self.__phaseTimer.cancel()

    def resumeTimer(self, method):
        self.__phaseTimer = thredingTimer(self.__timeRemaining, method)
        self.__phaseTimer.start()
        self.__startedAt = time.time()

    def stopTimer(self):
        self.__timeRemaining = None
        self.__startedAt = None
        self.__phaseTimer.cancel()

    def setRemainingTime(self, duration):
        self.__timeRemaining = duration

    def getRemainingTime(self):
        return self.__timeRemaining

    def getStartedAt(self):
        return self.__startedAt

    def getphaseTimer(self):
        return self.__phaseTimer








