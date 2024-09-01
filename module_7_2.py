from Tools.scripts.md5sum import printsum


def custom_write(file_name, string):
    file = open(file_name, 'w', encoding = 'utf-8')
    string_positions = {}
    number = 0
    for i in string:
        curs_byte = file.tell()
        file.write(f'{i}\n')
        string_positions[number+1, curs_byte] = i
    file.close()
    return string_positions




info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)


