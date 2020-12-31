from bs4 import BeautifulSoup
from rb_classes import Player

with open('201227121341TeamforAustria27122020_lin.xml', 'r') as f:
    t = f.read()

# print(t)

soup = BeautifulSoup(t, 'xml')
# print(soup.text)

participants = soup.find('PARTICIPANTS')
teamssoup = participants.findAll('TEAM')

teams = []
for team in teamssoup:
    t = {}
    t['Nr'] =team.attrs['TEAM_ID']
    t['Name'] = team.attrs['TEAM_NAME']
    teams.append(t)