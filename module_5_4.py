class House:
    houses_history = []
    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, houses_history, number_of_floors):
        self.houses_history = houses_history
        self.number_of_floors = number_of_floors

    def __del__(self):
        print (f'{self.houses_history} снесен, но он останется в истори')
        return self

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.houses_history}, кол - во этажей: {self.number_of_floors}.'

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)


del h2
del h3

print(House.houses_history)




# print(h1 == h2)  # __eq__
#
# h1 = h1 + 10  # __add__
# print(h1)
# print(h1 == h2)
#
# h1 += 10  # __iadd__
# print(h1)
#
# h2 = 10 + h2  # __radd__
# print(h2)
#
# print(h1 > h2)  # __gt__
# print(h1 >= h2)  # __ge__
# print(h1 < h2)  # __lt__
# print(h1 <= h2)  # __le__
# print(h1 != h2)  # __ne__
