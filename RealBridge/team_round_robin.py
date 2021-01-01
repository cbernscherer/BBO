from bs4 import BeautifulSoup
from rb_classes import Player, Pair, Team

with open('201227121341TeamforAustria27122020_lin.xml', 'r') as f:
    t = f.read()

# print(t)

soup = BeautifulSoup(t, 'xml')
# print(soup.text)

participants = soup.find('PARTICIPANTS')
teamssoup = participants.findAll('TEAM')

teams = []
for ts in teamssoup:
    attrs = ts.attrs
    team = Team(int(attrs['TEAM_ID']), attrs['TEAM_NAME'])

    pairsoup = ts.findAll('PAIR')

    pairs = []
    players =[]

    for ps in pairsoup:
        pair_id = int(ps.find('PAIR_NUMBER').text.split(':')[1])
        boards_played = int(ps.find('BOARDS_PLAYED').text)
        pair_imps = float(ps.find('PAIR_IMPS').text)

        print(':'.join((str(team.id), str(pair_id))), boards_played, pair_imps)

    teams.append(team)

for team in teams:
    print(team.id, team.name)