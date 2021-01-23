import json
import pandas as pd
import numpy as np

def append_id(name:str):
    if name.find('#') == -1:
        name = name + '#{}'.format(players[players['Spieler']==name]['OeBV-Nummer'].values[0])

    return name

def is_identical(pair1, pair2):
    return ((pair1[0] == pair2[0]) & (pair1[1] == pair2[1])) | ((pair1[0] == pair2[1]) & (pair1[1] == pair2[0]))

json_file = '210121127224B4ATeamCupJnnerSemifinale.json'
players_file = 'players.csv'
crossimps_file = 'ximps.csv'

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

# print(identical)

# add totals for identical pairs
for pair in identical:
    config['co_pair'][pair[0]] +=config['co_pair'][pair[1]]
    config['co_pair'][pair[1]] = 0.

    config['co_pair_den'][pair[0]] +=config['co_pair_den'][pair[1]]
    config['co_pair_den'][pair[1]] = 0

    config['co_pair_num_boards'][pair[0]] +=config['co_pair_num_boards'][pair[1]]
    config['co_pair_num_boards'][pair[1]] = 0

to_delete = np.array([config['co_pair_den'][i] == 0 for i in range(len(config['co_pair_den']))])
new_nrs = [i - sum(to_delete[0:i]) for i in range(len(to_delete))]

to_keep = np.nonzero(config['co_pair_den'])[0]

# remove duplets and build results
participants = ['' for i in range(len(to_keep))]

for i in range(len(config['co_lineups'])):
    pairs = config['co_lineups'][i]['pairs']
    for j in range(len(pairs)-1, -1, -1):
        pair_nr = int(pairs[j][2])

        if to_delete[pair_nr]:
            pairs.pop(j)
        else:
            pairs[j][2] = str(new_nrs[pair_nr])
            participants[new_nrs[pair_nr]] = '{} - {}'.format(
                pairs[j][0].split('#')[0],
                pairs[j][1].split('#')[0]
            )

    config['co_lineups'][i]['pairs'] = pairs
    # print(config['co_lineups'][i])

# remove information of deleted pais
config['co_pair'] = list(np.array(config['co_pair'])[to_keep])

dens = []
bds = []
for i in range(len(config['co_pair_den'])):
    if not to_delete[i]:
        dens.append(config['co_pair_den'][i])
        bds.append(config['co_pair_num_boards'][i])

config['co_pair_den'] = dens
config['co_pair_num_boards'] = bds

config['total_num_pairs'] = len(to_keep)

# s = json.dumps(config)
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False)

# print(len(identical))
# print(config['co_pair_den'])
print(sum(config['co_pair_num_boards']))
print(sum(config['co_pair_den']))
# print(participants)

# build crossimp table
crossimps = pd.DataFrame()
ranks= crossimps['Rang'] = np.zeros(len(to_keep), dtype=np.int)
crossimps['Paar'] = participants
crossimps['Schnitt'] = np.zeros(len(to_keep))
crossimps['total imps'] = config['co_pair']
crossimps['Vergleiche'] = config['co_pair_den']
crossimps['Boards'] = config['co_pair_num_boards']
imps = crossimps['Schnitt'] = round(crossimps['total imps'] / crossimps['Vergleiche'], 2)
crossimps['total imps'] = round(crossimps['total imps'])

crossimps.sort_values(by='Schnitt', ascending=False, inplace=True)

# determine ranks
ranks[0] = old_rank = 1
old_imps = imps[0]

for i in range(1, len(ranks)):
    if imps[i] == old_imps:
        ranks[i] = old_imps
    else:
        old_imps = imps[i]
        ranks[i] = old_rank = i + 1

crossimps['Rang'] = ranks

crossimps.to_csv(crossimps_file, encoding='utf-8', index=False, sep=';', decimal=',')

print(crossimps.head())