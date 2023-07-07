class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass

class Circle(Figure):
    def __init__(self,radius):
        self.__radius = radius

    def calculate_area(self):
        return (self.__radius ** 2) * 3.14

    def info(self):
        print(f'''CIRCLE RADIUS: {self.__radius}{self.unit}
AREA: {self.calculate_area()}{self.unit}''')



class RightTriangle(Figure):
    def __init__(self,side_a,side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return (self.__side_a * self.__side_b) / 2

    def info(self):
        print(f'''RIGHTTRIANGLE SIDE A : {self.__side_a}{self.unit},
SIDE B : {self.__side_b}{self.unit}
AREA : {self.calculate_area()}''')


circle1 = Circle(3)
circle2 = Circle(5)

triangle1 = RightTriangle(6,4)
triangle2 = RightTriangle(5,3)
triangle3 = RightTriangle(3,5)

figure_list = [circle1,circle2,triangle1,triangle2,triangle3]

for figure in figure_list:
    figure.info()
    print('____________________')

