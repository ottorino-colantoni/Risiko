import pickle
import time


class Eventlistener:

    # fase/attributo1/attributo2...

    def __init__(self, game, socketPlayer):
        self.game = game
        self.socketPlayer = socketPlayer


    def manageRequest(self, string):
        if self.game.gameStarted():
            data = string.split("/")
            if self.socketPlayer == self.game.getCurrentRound().getRoundPlayer().getNickName():
                if data[0] == "startCPhase":
                    dts = self.startCPhase()
                elif data[0] == "enterAttackingTerritory":
                    if len(data) == 2:
                        dts = self.enterAttackingTerritory(data[1])
                elif data[0] == "confirmAttack":
                    if len(data) == 4:
                        dts = self.confirmAttack(data[1], data[2], int(data[3]))
                elif data[0] == "endCPhase":
                    dts = self.endCombatPhase()
                else:
                    dts = "Comando non corretto"
            else:
                #COSE CHE PUO FARE IL GIOCATORE NON DI TURNO
                if data[0] == "defending":
                    if len(data) == 2:
                        dts = self.setDefendingArmies(int(data[1]))
                else:
                    dts = "Non sei di turno"
            return dts
        else:
            return "Waiting for more player\n"

    # def setGame(self, game):
    #     self.game = game

    def startCPhase(self):

        #TODO NON POSSO FAR PARTIRE UN'ALTRA COMBAT PHASE SE UNA GIA' E' IN ATTO ---- DA METTERE BOOLS IN CLASSE COMBATPHASE (?)

        data_to_send = ""
        playerTerritories = self.game.getCurrentRound().startCombatPhase()
        if len(playerTerritories) == 0:
            data_to_send = "Non ci sono territori da cui puoi attaccare"
        else:
            data_to_send += ("Puoi muovere un attacco dai seguenti territori: " + "\n")
            for territory in playerTerritories:
                data_to_send += f'{territory.getNameID()}[{territory.getArmiesNumber()}]\n'

        return data_to_send

    def enterAttackingTerritory(self, territoryID):
        data_to_send = ""

        # raised whenever an attacking territory is missing
        try:
            attackableTerritories = self.game.getCurrentRound().enterAttackingTerritory(territoryID)

            if len(attackableTerritories) > 0:
                data_to_send += ("I territori attaccabili sono: " + "\n")
                for attackableTerritory in attackableTerritories:
                    data_to_send += f'{attackableTerritory.getNameID()}[{attackableTerritory.getArmiesNumber()}]\n'
            else:
                data_to_send = "Non puoi attaccare nessun territorio da qui\n"
        except Exception as err:
            data_to_send = err

        return data_to_send


    def confirmAttack(self, attackingTerritoryID, defendingTerritoryID, armies):
        #TODO SE STO IN ATTESA DI UN DIFENSORE NON POSSO FARE UN ALTRO ATTACCO (O NIENTE INSOMMA)
        try:
            self.game.getCurrentRound().confirmAttack(attackingTerritoryID, defendingTerritoryID, armies)

            self.__notifyDefPlayer(attackingTerritoryID, defendingTerritoryID, armies)
            data_to_send = "In attesa del difensore..."
        except Exception as err:
            data_to_send = err

        return data_to_send

    def __notifyDefPlayer(self, attackingTerritoryID, defendingTerritoryID, armies):
        board = self.game.getCurrentRound().getBoard()
        defTerritory = board.findTerritory(defendingTerritoryID)
        defPlayer = defTerritory.getOwner()
        defPlayerSocket = self.game.playerSocket[defPlayer.getNickName()]
        atkPlayer = self.game.getCurrentRound().getRoundPlayer()
        data_to_send = f'Il giocatore {atkPlayer.getNickName()} ti sta attaccando da {attackingTerritoryID} a {defendingTerritoryID} con {armies} armate\n'
        defPlayerSocket.send(data_to_send.encode())

    def setDefendingArmies(self, armies):
        try:
            self.game.getCurrentRound().enterDefendingArmies(armies)
            #TODO (?) IN TEORIA CI SERVE QUALCUNO CHE DECIDA CHE IL RISULTATO DELL'ATTACCO VADA A TUTTI (PER ORA E' IL LISTENER STESSO)
            data_to_send = self.game.getCurrentRound().getCombatPhase().getLastAttack().getResult().__repr__()

            for player in self.game.get_player_socket():
                self.game.get_player_socket()[player].send(data_to_send.encode())
            data_to_send = ""
            return data_to_send

        except Exception as err:
            data_to_send = err

    def endCombatPhase(self):
        self.game.makeTurn()
        data_to_send = f'Ora è il turno di {self.game.getCurrentRound().getRoundPlayer().getNickName()} \n'
        #TODO MANDARE QUESTO MESSAGGIO A TUTTI TRANNE CHE AL GIOCATORE ASSOCIATO ALLA SOCKET
        for player in self.game.get_player_socket():
            self.game.get_player_socket()[player].send(data_to_send.encode())

        data_to_send = ""
        return data_to_send

