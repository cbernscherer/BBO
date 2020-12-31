class Player():
    def __init__(self, pl_name, pl_id=0):
        self.name = pl_name
        self.id = pl_id

class Pair():
    def __init__(self, players, id):
        self.players = players
        self.id = id

class Team():
    def __init__(self, team_id, team_name):
        self.id = team_id
        self.name = team_name

        self.players = []
        self.pairs = []