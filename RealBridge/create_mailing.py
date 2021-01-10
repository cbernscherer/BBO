import pandas as pd
import numpy as np

teams_file = 'teams.csv'
players_file = 'players.csv'
mailing_list = 'mailing.csv'
base_link = 'bt.html?p=210114124325&q=x2UVekZ868SltpLinz'

teams = pd.read_csv(teams_file, encoding='utf-8')
players = pd.read_csv(players_file, encoding='utf-8', dtype={'OeBV-Nummer':np.str})

with open(mailing_list, 'w', encoding='utf-8') as mf:
    mf.write(','.join(teams.columns.values))
    for i in range(1,11):
        mf.write(',Spieler{},Link{}'.format(i, i))

    for team_name in teams['Name'].values:
        team = teams[teams['Name'] == team_name]
        mf.write('\n{},{},{}'.format(team['Name'].values[0], team['Email'].values[0], team['Anrede'].values[0]))

        team_members = players[players['Team'] == team_name]

        pl_names = team_members['Spieler'].values
        oebv_nrs = team_members['OeBV-Nummer'].values

        for pl_i, pl_n in enumerate(pl_names):
            mf.write(',{},{}&n={}'.format(pl_n, base_link, pl_n.replace(' ', '%20')))

            if pd.notnull(oebv_nrs[pl_i]):
                 mf.write('&i={}'.format(oebv_nrs[pl_i]))

        for i in range(pl_i+1,10):
            mf.write(',,')