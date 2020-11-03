from threading import Timer
import time


class RiskTimer:

    __instance = None
    __timeRemaining = None
    __startedAt = None
    __phaseTimer = None

    @staticmethod
    def getInstance():
        if RiskTimer.__instance == None:
            RiskTimer()
        return RiskTimer.__instance

    def __init__(self):
        if RiskTimer.__instance != None:
            raise Exception("This class is a Singleton")
        else:
            self.__timeRemaining = None
            self.__startedAt = None
            self.__phaseTimer = None
            RiskTimer.__instance = self

    def startTimer(self, method):

        self.__startedAt = time.time()
        self.__phaseTimer = Timer(self.__timeRemaining, method)
        self.__phaseTimer.start()

    def pauseTimer(self):
        self.__timeRemaining = self.__timeRemaining - (time.time() - self.__startedAt)
        self.__phaseTimer.cancel()

    def resumeTimer(self, method):
        self.__phaseTimer = Timer(self.__timeRemaining, method)
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








