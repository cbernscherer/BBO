# filename = '210102122486Dreiknigspokal2021_lin.xml'
filename = input('Bitte gib den Filenamen ein und dann Enter: ')

convert_table = {
    'Ä': '&#196;',
    'Ö': '&#214;',
    'Ü': '&#220;',
    'ä': '&#228;',
    'ö': '&#246;',
    'ü': '&#252;',
    'ß': '&#223;',
    'á': '&#225;',
    'é': '&#233;',
    'í': '&#237;',
    'ó': '&#243;',
    'ú': '&#250;',
}

def convert(string:str):
    for k, v in convert_table.items():
        string = string.replace(k, v)

    return string

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

with open(filename, 'w', encoding='utf-8') as f:
    f.write(convert(content))