import re

config = 'd:\\Users\\cbern\\Desktop\\dkpsettings.json'

with open(config, 'r') as f:
    conf = f.read()

conf = conf[conf.find('seat_assignments')-1:]


