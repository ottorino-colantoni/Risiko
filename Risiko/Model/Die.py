import random

class Die:

    __faceValue = None

    def __init__(self):
        self.__faceValue = None

    def rollDie(self):
        self.__faceValue = random.randrange(1, 6)

    def getFaceValue(self):
        return self.__faceValue

