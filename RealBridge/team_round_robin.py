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
    team = Team(attrs['TEAM_ID'], attrs['TEAM_NAME'])

    teams.append(team)

for team in teams:
    print(team.id, team.name)