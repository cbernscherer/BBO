import json

filename = 'd:\\Users\\cbern\\Desktop\\210102122486Dreiknigspokal2021.json'

with open(filename, 'r', encoding='utf-8') as f:
    print(json.dumps(json.load(f)))