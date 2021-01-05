import json
import pandas as pd
import numpy as np

directions = ['n', 's', 'e', 'w']
config = 'd:\\Users\\cbern\\Desktop\\dkpsettings.json'
participants ='participants.txt'
member_file = 'SpoXls.xls'

with open(config, 'r', encoding='utf-8') as f:
    conf = json.load(f)

members = pd.read_excel(member_file)

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
            # print(1)
            continue

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

        f.write('{},{}\n'.format(name, str(oebv_nr)))