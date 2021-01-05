import json

directions = ['n', 's', 'e', 'w']
config = 'd:\\Users\\cbern\\Desktop\\dkpsettings.json'
participants ='participants.txt'

with open(config, 'r', encoding='utf-8') as f:
    conf = json.load(f)

tables = []
if 'seat_assignments' in conf:
    tables = conf['seat_assignments']

names = []
for table in tables:
    for direction in directions:
        if direction in table:
            names.append(table[direction])

with open(participants, 'r', encoding='utf-8') as f:
    partic_exist = f.read()

with open(participants, 'a', encoding='utf-8') as f:
    for name in names:
        if partic_exist.find(name) != -1:
            continue

        f.write(name + ',\n')