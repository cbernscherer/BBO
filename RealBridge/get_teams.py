import json
import pandas as pd

config_file = '210107123686B4ATeamCupJnner07012021.json'
player_file = 'players.csv'
teams_file = 'teams.csv'

with open(config_file, 'r', encoding='utf-8') as f:
    config = dict(json.load(f))

# for k in config.keys():
#     print(k)

teams = config['team_names']

players = []

for team_ind, lineup in enumerate(config['co_lineups']):
    players.append([])

    for pair in lineup['pairs']:
        for player in pair[:2]:
            if not player in players[team_ind]:
                players[team_ind].append(player)

# write players to csv
with open(player_file, 'w', encoding='utf-8') as f:
    f.write('Team,Spieler,OeBV-Nummer,Captain,Link')

    for team_ind in range(0, len(teams)):
        for player_ind in range(0, len(players[team_ind])):
            f.write('\n{},{},,False,'.format(teams[team_ind], players[team_ind][player_ind]))

teams = pd.DataFrame(pd.Series(teams),columns=['Name'])
teams['Email'] = teams['Anrede'] =''
teams.to_csv(teams_file, encoding='utf-8', index=False)