from .Territory import Territory
from .boardBuilder import boardBuilder
from .Continent import Continent

class classicBoardBuilder(boardBuilder):

    def __init__(self):
        self.__board = {}
        self.__mapId = "Terra"

    def buildContinents(self):
        continent1 = Continent("Europa")
        # continent2 = Continent("Nord America")
        # continent3 = Continent("Sud America")
        # continent4 = Continent("Africa")
        # continent5 = Continent("Asia")
        # continent6 = Continent("Oceania")

        self.__board = {

            continent1.getContinentId(): continent1,
            # continent2.getContinentId(): continent2,
            # continent3.getContinentId(): continent3,
            # continent4.getContinentId(): continent4,
            # continent5.getContinentId(): continent5,
            # continent6.getContinentId(): continent6,
        }

    # TODO: Complete Map creation if it is correct
    def buildTerritories(self):
        # Europe territories
        territoryE1 = Territory("Gran Bretagna")
        territoryE2 = Territory("Islanda")
        territoryE3 = Territory("Europa Settentrionale")
        territoryE4 = Territory("Scandinavia")
        territoryE5 = Territory("Europa Meridionale")
        territoryE6 = Territory("Ucraina")
        territoryE7 = Territory("Europa Occidentale")

        ''' TODO
        # Nord America territories
        territoryNA1 = Territory("Alaska")
        territoryNA2 = Territory("Alberta")
        territoryNA3 = Territory("America Centrale")
        territoryNA4 = Territory("Stati Uniti Orientali")
        territoryNA5 = Territory("Groenlandia")
        territoryNA6 = Territory("Territori del Nord Ovest")
        territoryNA7 = Territory("Ontario")
        territoryNA8 = Territory("Quebec")
        territoryNA9 = Territory("Stati Uniti Occidentali")

        # Sud America territories
        territorySA1 = Territory("Argentina")
        territorySA2 = Territory("Brasile")
        territorySA3 = Territory("Perù")
        territorySA4 = Territory("Venezuela")

        # Africa territories
        territoryAF1 = Territory("Congo")
        territoryAF2 = Territory("Africa Orientale")
        territoryAF3 = Territory("Egitto")
        territoryAF4 = Territory("Madagascar")
        territoryAF5 = Territory("Africa del Nord")
        territoryAF6 = Territory("Africa del Sud")

        # Asia Territories
        territoryAS1 = Territory("Afghanistan")
        territoryAS2 = Territory("Cina")
        territoryAS3 = Territory("India")
        territoryAS4 = Territory("Cita")
        territoryAS5 = Territory("Giappone")
        territoryAS6 = Territory("Kamchatka")
        territoryAS7 = Territory("Medio Oriente")
        territoryAS8 = Territory("Mongolia")
        territoryAS9 = Territory("Siam")
        territoryAS10 = Territory("Siberia")
        territoryAS11 = Territory("Urali")
        territoryAS12 = Territory("Jacuzia")

        # Oceania Territories
        territoryOC1 = Territory("Australia Orientale")
        territoryOC2 = Territory("Indonesia")
        territoryOC3 = Territory("Nuova Guinea")
        territoryOC4 = Territory("Australia Occidentale")
        '''
        # TODO: in some territories miss neighbors from other continent
        # Add neighbords to Europe territories
        territoryE1.addNeighbors([territoryE2, territoryE4, territoryE3, territoryE7])
        territoryE2.addNeighbors([territoryE4, territoryE1])  # Miss , territoryNA5 !!!!
        territoryE3.addNeighbors([territoryE1, territoryE4, territoryE5, territoryE6, territoryE7])
        territoryE4.addNeighbors([territoryE1, territoryE2, territoryE3, territoryE6])
        territoryE5.addNeighbors([territoryE3, territoryE6, territoryE7])  # Miss territoryAF3, territoryAS7
        territoryE6.addNeighbors([territoryE3, territoryE4, territoryE5])  # Miss territoryAS11, territoryAS1, territoryAS7
        territoryE7.addNeighbors([territoryE3, territoryE5, territoryE1])  # Miss territoryAF5

        # add to Continent Europe
        self.__board['Europa'].addTerritory([territoryE1, territoryE2, territoryE3, territoryE4, territoryE5, territoryE6, territoryE7])

    def getBoard(self):
        return self.__board

    def getMapId(self):
        return self.__mapId


