import pickle
import time


class RequestHandler:

    def __init__(self, game, player, msgCache):
        self.game = game
        self.player = player
        self.msgCache = msgCache

    def manageRequest(self, string):
        if self.game.gameStarted():
            data = string.split("/")
            if self.player == self.game.getCurrentRound().getRoundPlayer().getNickName():
                if data[0] == "startCPhase":
                    self.startCPhase()
                elif data[0] == "enterAttackingTerritory":
                    if len(data) == 2:
                        self.enterAttackingTerritory(data[1])
                elif data[0] == "confirmAttack":
                    if len(data) == 4:
                        self.confirmAttack(data[1], data[2], int(data[3]))
                elif data[0] == "setConquerArmies":
                    if len(data) == 2:
                        self.setArmiesToMoveAfterConquer(int(data[1]))
                elif data[0] == "endCPhase":
                    self.endCombatPhase()
                else:
                    self.msgCache.putMsg("Comando non corretto", self.player)

            else:
                #COSE CHE PUO FARE IL GIOCATORE NON DI TURNO
                if data[0] == "defending":
                    if len(data) == 2:
                        self.setDefendingArmies(int(data[1]))
                else:
                    self.msgCache.putMsg("Non sei di turno", self.player)
        else:
            self.msgCache.putMsg("Waiting for more players", self.player)

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

        self.msgCache.putMsg(data_to_send, self.player)

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
            data_to_send = str(err)

        self.msgCache.putMsg(data_to_send, self.player)

    def confirmAttack(self, attackingTerritoryID, defendingTerritoryID, armies):
        #TODO SE STO IN ATTESA DI UN DIFENSORE NON POSSO FARE UN ALTRO ATTACCO (O NIENTE INSOMMA)
        try:
            self.game.getCurrentRound().confirmAttack(attackingTerritoryID, defendingTerritoryID, armies)

            self.__notifyDefPlayer(attackingTerritoryID, defendingTerritoryID, armies)
            data_to_send = "In attesa del difensore..."
        except Exception as err:
            data_to_send = str(err)

        self.msgCache.putMsg(data_to_send, self.player)

    def __notifyDefPlayer(self, attackingTerritoryID, defendingTerritoryID, armies):
        board = self.game.getCurrentRound().getBoard()
        defTerritory = board.findTerritory(defendingTerritoryID)
        defPlayerID = defTerritory.getOwnerID()
        atkPlayer = self.game.getCurrentRound().getRoundPlayer()
        data_to_send = f'Il giocatore {atkPlayer.getNickName()} ti sta attaccando da {attackingTerritoryID} a {defendingTerritoryID} con {armies} armate\n'
        self.msgCache.putMsg(data_to_send, defPlayerID)


    def setDefendingArmies(self, armies):
        try:
            self.game.getCurrentRound().enterDefendingArmies(armies)
            #TODO (?) IN TEORIA CI SERVE QUALCUNO CHE DECIDA CHE IL RISULTATO DELL'ATTACCO VADA A TUTTI (PER ORA E' IL LISTENER STESSO)
            result = self.game.getCurrentRound().getCombatPhase().getLastAttack().getResult()
            data_to_send = result.__repr__()

            for player in self.game.players:
                self.msgCache.putMsg(data_to_send, player.getNickName())

            if result.conquered:
                self.msgCache.putMsg("Hai conquistato il territorio! Quante armate vuoi spostare?", self.game.
                                     getCurrentRound().getRoundPlayer().getNickName())


        except Exception as err:
            data_to_send = str(err)
            self.msgCache.putMsg(data_to_send, self.player)


    def setArmiesToMoveAfterConquer(self, armies):

        try:
            self.game.getCurrentRound().conquer(armies)
            data_to_send = str("Spostamento effettuato!")
        except Exception as err:
            data_to_send = str(err)

        self.msgCache.putMsg(data_to_send, self.player)




    def endCombatPhase(self):
        self.game.makeTurn()
        #TODO MANDARE QUESTO MESSAGGIO A TUTTI TRANNE CHE AL GIOCATORE ASSOCIATO ALLA SOCKET
        for player in self.game.players:
            if player.getNickName != self.game.getCurrentRound().getRoundPlayer().getNickName():
                self.msgCache.putMsg(f'Ora è il turno di {self.game.getCurrentRound().getRoundPlayer().getNickName()} \n', player.getNickName())
            else:
                self.msgCache.putMsg("E' il tuo turno", player.getNickName())
