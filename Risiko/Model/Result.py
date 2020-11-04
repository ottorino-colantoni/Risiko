from Risiko.Model.Territory import Territory


class Result:

    def __init__(self, atkLosses, defLosses, conquered):
        self.atkLosses = atkLosses
        self.defLosses = defLosses
        self.conquered = conquered

    def __repr__(self):
        out = f'Armate perse dall\'attaccante: {self.atkLosses}. \n Armate perse dal difensore: {self.defLosses}. \n Territorio Conquistato = {self.conquered}.'
        return out