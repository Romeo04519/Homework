
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x[0])-len(x[1]) for x in zip(first, second) if len(x[0]) != len(x[1]))
print(list(first_result))

second_result = (len(first[x]) > len(second[x]) for x in range(3))
print(list(second_result))