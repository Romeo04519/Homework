class Figure:
    sides_count = 1
    __sides = []
    __color = [1,1,1]
    filled = False

    def __init__(self, color, *sides):
        self.set_color(*color)
        if len(sides) == self.sides_count:
            self.__sides.clear()
            for i in sides:
                self.__sides.append(i)
        else:
            self.__sides.clear()
            for i in range(self.sides_count):
                self.__sides.append(1)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if r <= 255 and g <= 255 and b <= 255:
            self.r = r
            self.g = g
            self.b = b
            self.filled = True

    def set_color(self, r, g, b):
        self.__is_valid_color(r, g, b)
        if self.filled == True:
            self.__color[0] = self.r
            self.__color[1] = self.g
            self.__color[2] = self.b
        else:
            pass

    def __is_valid_sides(self, *sides_):
        check_sides = False
        list = []
        for i in sides_:
            if i > 0:
                list.append(i)
            else:
                list.append(0)
        if all(list) and len(sides_) == self.sides_count:
            check_sides = True
        return check_sides

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            for i in new_sides:
                for j in range(len(new_sides)):
                    self.__sides[j] = i



class Circle(Figure):
    sides_count = 1

    def get_square(self):
        __radius = sum(self.get_sides()) / 6.28
        s = sum(self.get_sides()) / (4 * 3.14)
        return s




class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        perim = sum(self.get_sides())/2
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        s = (perim * (perim - a) * (perim - b) * (perim - c))**0.5
        return s


class Cube(Figure):
    sides_count = 12
    __sides = []

    def __init__(self, color, *sides):
        self.set_color(*color)
        if len(sides) == 1:
            Cube.__sides.clear()
            for i in range(self.sides_count):
                Cube.__sides.append(*sides)
        else:
            Cube.__sides.clear()
            for i in range(self.sides_count):
                Cube.__sides.append(1)

    def get_sides(self):
        return Cube.__sides

    def get_volume(self):
        v = Cube.__sides[0]**3
        return v


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())






