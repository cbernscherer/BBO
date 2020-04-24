import pandas as pd
from _collections import defaultdict

convert_uml = True

def convert(string:str):
    string = string.replace('Ä', 'Ae')
    string = string.replace('Ö', 'Oe')
    string = string.replace('Ü', 'Ue')
    string = string.replace('ä', 'ae')
    string = string.replace('ö', 'oe')
    string = string.replace('ü', 'ue')
    string = string.replace('ß', 'ss')

    return string

reg_players = pd.read_excel('Spielerliste BBO.xlsx', names=['Nick', 'Name'], usecols=[0, 1])
reg_players = reg_players[reg_players['Nick'].notna() & reg_players['Name'].notna()]

oebv_players = pd.read_excel('Spielerliste BBO.xlsx', sheet_name='ÖBVSpielerdatei',
                             names=['Zuname', 'Vorname'], usecols=[1, 2])
oebv_players = oebv_players[oebv_players['Vorname'].notna() & oebv_players['Zuname'].notna()]
oebv_list = oebv_players[['Vorname', 'Zuname']].values
names = [' '.join(list(oebv_list[i])).lower() for i in range(len(oebv_list))]
oebv_players['Name'] = names

reg_players['ALIAS'] = reg_players['Nick']
reg_players['CLUB1'] = reg_players['Nick']
reg_players['CLUB2'] = ''
reg_players['CLUB3'] = ''
reg_players['CLUB4'] = ''
reg_players['CLUB5'] = ''


duplicates = reg_players.duplicated('Name')
duplicate_entries = reg_players[duplicates]
reg_players = reg_players[duplicates == False]

occurrencies = defaultdict(lambda: 1)

for entry in duplicate_entries.itertuples():
    occurrencies[entry.Name] += 1
    if occurrencies[entry.Name] > 5:
        continue

    tmp = reg_players[reg_players['Name'] == entry.Name]['ALIAS'].values
    reg_players.loc[reg_players['Name'] == entry.Name, ["ALIAS"]] = tmp[0] + ';' + entry.ALIAS
    reg_players.loc[reg_players['Name'] == entry.Name, ['CLUB' + str(occurrencies[entry.Name])]] = entry.ALIAS

names = list(reg_players['Name'])

surnames = []
firstnams = []

for name in names:
    oebv_entry = oebv_players[oebv_players['Name'] == name.lower()].values

    if len(oebv_entry) > 0:
        if convert_uml:
            firstnams.append(convert(oebv_entry[0, 1]).title())
            surnames.append(convert(oebv_entry[0, 0]).title())
        else:
            firstnams.append(oebv_entry[0, 1].title())
            surnames.append(oebv_entry[0, 0].title())
    else:
        if convert_uml:
            name = convert(name)

        tmp = name.split(' ')

        surnames.append(tmp[-1])
        firstnams.append(' '.join(tmp[0:-1]))

reg_players['SURNAME'] = surnames
reg_players['FIRSTNAME'] = firstnams
reg_players['STATUS'] = 'Member'

reg_players.drop(columns=['Nick', 'Name'], inplace=True)
# reg_players = reg_players.head(10)

reg_players.to_csv('bridgewebs_import.csv', encoding='iso 8859-1', index=False)

# print(reg_players.head())


