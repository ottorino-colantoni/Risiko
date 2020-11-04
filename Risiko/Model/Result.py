class Result:

    def __init__(self, atkTerr: Territory, defTerr: Territory, atkArmies: int):
        self.attackingTerritory = atkTerr
        self.defendingTerritory = defTerr
        self.attackingArmies = atkArmies