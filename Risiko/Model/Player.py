
class Player:

    __nickName = None
    __color = None

    def __init__(self, username, gameColor):
        self.__color = gameColor
        self.__nickName = username

    def getNickName(self):
        return self.__nickName

    def getColor(self):
        return self.__color

