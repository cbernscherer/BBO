import pandas as pd

player_file = 'players.csv'
member_file = 'SpoXls.xls'
teams_file = 'teams.csv'

players = pd.read_csv(player_file, encoding='utf-8')
print(players.head())
names = players['Spieler'].values

members = pd.read_excel(member_file)
member_names = members['NAME'].values
member_names = [n.upper() for n in member_names]
members['NAME'] = member_names

oebv_nrs = []

for name in names:
    name_parts = name.split(' ')
    last_name = name_parts[-1].upper()
    first_name = ' '.join(name_parts[:-1])

    oebv_nr = ''

    extract_members = members[(members['NAME'] == last_name) & (members['VNAME'] == first_name)]
    if len(extract_members) == 1:
        oebv_nr = int(extract_members['NR'])

    else:
        extract_members = members[members['NAME'] == last_name]

        first_names_found = extract_members['VNAME'].values

        matches = []
        for fnf in first_names_found:
            matches.append(first_name.lower() in str(fnf).lower())

        if sum(matches) == 1:
            oebv_nr = int((extract_members[matches])['NR'])

        else:
            # no firstname match
            if len(extract_members) == 1:
                if input('In den ÖBV Daten gefunden: {} {}; Name in der Sitzordnung: {}; Zuordnen(j/n)'.format(
                    str(extract_members['VNAME'].values[0]), str(extract_members['NAME'].values[0]), name)) == 'j':

                    oebv_nr = int((extract_members)['NR'])

    oebv_nrs.append(str(oebv_nr))

players['OeBV-Nummer'] = oebv_nrs
players.to_csv(player_file, encoding='utf-8', index=False)

# Anrede
teams = pd.read_csv(teams_file, encoding='utf-8')
captains = players[players['Captain']]

teams['Anrede'] = ['Lieber {}'.format(n.split(' ')[0]) for n in captains['Spieler'].values]
teams.to_csv(teams_file, encoding='utf-8', index=False)

