import pandas as pd

in_file = 'Wiener Mixed Team Meisterschaft.xlsx'
out_file = 'wr_players.csv'

players = pd.read_excel(in_file)
# print(players)

names = players['Spieler'].values
# print(names)

for i, name in enumerate(names):
    n = name.split(' ')
    n[0] = n[0].capitalize()
    names[i] = ' '.join(n[1:] + [n[0]])

# print(names)

players['Spieler'] = names
players.to_csv(out_file, encoding='utf-8', index=False)