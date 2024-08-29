class Vehicle:
    __COLOR_VARIANTS = ['Red','Black','Blue','White']
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def get_model(self):
        return f'Модель: {self.__model}'

    def print_info(self):
        print(f'{self.get_model()} \n{self.get_horsepower()} \n{self.get_color()}')
        print('Владелец:', self.owner)

    def set_color(self, new_color):
        changes_color = False
        for i in self.__COLOR_VARIANTS:
            if new_color.lower() == i.lower():
                self.__color = new_color
                changes_color = True
        if changes_color == False:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5



vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()