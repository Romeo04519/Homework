class Animal:
    alive = True
    fed = False
    def __init__(self, name = 1):
        self.name = name


class Plant:
    edible = False
    def __init__(self, name = 1):
        self.name = name


class Mammal(Animal):
    food = Plant()
    name = Animal()
    def eat(self, food):
        #self.food = food
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = True


class Predator(Animal):
    food = Plant()
    name = Animal()
    def eat(self, food):
        # self.food = food
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
