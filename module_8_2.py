def personal_sum(*numbers):
    result = 0
    incorrect_data = 0
    for i in list(*numbers):
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчета суммы - {i}')

    return incorrect_data, result

def calculate_average(*numbers):
    try:
        incor, resul = personal_sum(*numbers)
        result_finish = resul/(len(*numbers)-incor)
        return result_finish
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать








# # cities = ["Москва", "Астрахань", "Самара", "Уфа", "Смоленск", "Тверь"]
# # b = map(len, cities)
# # print(list(b))
# # def symbols(s):
# #     return list(s.lower())
#
# cities = {'a': "Москва", 'b': "Астрахань",'c': " Piter"}
# def proba(x):
#     return cities.get(x, 'Привет')
#
# b = list(map(proba, ["a", "b", "c","d"]))
# print(b)