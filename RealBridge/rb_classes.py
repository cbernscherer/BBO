class Player():
    def __init__(self, pl_name, pl_id=0):
        self.name = pl_name
        self.id = pl_id

class Pair():
    def __init__(self, players, id, hands_played, imps):
        self.players = players
        self.id = id
        self.hands_played = hands_played
        self.imps = imps


class Team():
    def __init__(self, team_id, team_name):
        self.id = team_id
        self.name = team_name

        self.players = []
        self.pairs = []