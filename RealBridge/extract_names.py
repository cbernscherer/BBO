import re

config = 'd:\\Users\\cbern\\Desktop\\dkpsettings.json'
participants ='participants.txt'

with open(config, 'r', encoding='utf-8') as f:
    conf = f.read()

conf = conf[conf.find('seat_assignments')-1:]
# print(conf)

search_for = r'\w+ \w+'
match = re.compile(search_for)

names = match.findall(conf)

with open(participants, 'r', encoding='utf-8') as f:
    partic_exist = f.read()

with open(participants, 'a', encoding='utf-8') as f:
    for name in names:
        if partic_exist.find(name) != -1:
            continue

        f.write(name + ',\n')