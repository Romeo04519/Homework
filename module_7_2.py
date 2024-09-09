from Tools.scripts.md5sum import printsum


def custom_write(file_name, string):
    file = open(file_name, 'w', encoding = 'utf-8')
    string_positions = {}
    number = 1
    for i in string:
        curs_byte = file.tell()
        file.write(f'{i}\n')
        string_positions[number, curs_byte] = i
        number += 1
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


