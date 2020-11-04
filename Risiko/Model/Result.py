from Risiko.Model.Territory import Territory


class Result:

    def __init__(self, atkLosses, defLosses, conquered):
        self.atkLosses = atkLosses
        self.defLosses = defLosses
        self.conquered = conquered