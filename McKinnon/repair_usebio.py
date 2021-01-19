file = '13T 13R M00006.xml'

with open(file, 'r') as f:
    content = f.read()

content = content.replace('TABLE_NUMBER', 'round_NUMBER')
content = content.replace('ROUND_NUMBER', 'TABLE_NUMBER')
content = content.replace('round_NUMBER', 'ROUND_NUMBER')

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)