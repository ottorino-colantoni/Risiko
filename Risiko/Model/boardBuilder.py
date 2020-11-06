from abc import ABC, abstractmethod


class boardBuilder(ABC):

    @abstractmethod
    def buildTerritories(self):
        pass

    @abstractmethod
    def buildContinents(self):
        pass

   #TODO:  il problema è che questa funzione crea una nuova istanza di Board ma non possiamo perhè Board è Singleton
   # @abstractmethod
   #def buildBoard(self):
   #    pass

    @abstractmethod
    def getBoard(self):
        pass

    @abstractmethod
    def getMapId(self):
        pass
