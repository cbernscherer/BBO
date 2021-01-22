import json
import pandas as pd

def append_id(name:str):
    if name.find('#') == -1:
        name = name + '#{}'.format(players[players['Spieler']==name]['OeBV-Nummer'].values[0])

    return name

def is_identical(pair1, pair2):
    return ((pair1[0] == pair2[0]) & (pair1[1] == pair2[1])) | ((pair1[0] == pair2[1]) & (pair1[1] == pair2[0]))

json_file = '210121127224B4ATeamCupJnnerSemifinale.json'
players_file = 'players.csv'

with open(json_file, 'r', encoding='utf-8') as f:
    config = json.load(f)

players = pd.read_csv(players_file, encoding='utf-8')
# print(players.head(3))
print(len(players[players['OeBV-Nummer'].isnull()]))

lineups = config['co_lineups']
for i, lineup in enumerate(lineups):
    # append IDs
    for j, pair in enumerate(lineup['pairs']):
        # print(pair)
        for k, pl in enumerate(pair[0:2]):
            config['co_lineups'][i]['pairs'][j][k] = append_id(pl)

# search identical
lineups = config['co_lineups']
identical = []
for lineup in lineups:
    pairs = lineup['pairs']
    for i in range(len(pairs)):
        for j in range(i+1, len(pairs)):
            if is_identical(pairs[i], pairs[j]):
                identical.append((int(pairs[i][2]), int(pairs[j][2])))

print(identical)

# add totals for identical pairs
for pair in identical:
    config['co_pair'][pair[0]] +=config['co_pair'][pair[1]]
    config['co_pair'][pair[1]] = 0.

    config['co_pair_den'][pair[0]] +=config['co_pair_den'][pair[1]]
    config['co_pair_den'][pair[1]] = 0

    config['co_pair_num_boards'][pair[0]] +=config['co_pair_num_boards'][pair[1]]
    config['co_pair_num_boards'][pair[1]] = 0

with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False)


print(len(identical))
print(sum(config['co_pair_num_boards']))
print(sum(config['co_pair_den']))
print(sum(config['co_pair']))