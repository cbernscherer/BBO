base_link = 'https://play.realbridge.online/bm.html?p=210102122486&q=TeilnehmerLink001'
participants ='participants.txt'
link_file = 'links.txt'

with open(participants, 'r', encoding='utf-8') as f:
    players = f.read().split('\n')

players = [p.split(',') for p in players[1:]]

with open(link_file, 'w', encoding='utf-8') as f:
    for player in players:
        line = player[0] + ':\n' + base_link + '&n=' + player[0].replace(' ', '%20')

        if len(player) > 1:
            if len(player[1].strip()):
                line += '&i=' + player[1].strip()

        line += '\n\n'
        f.write(line)