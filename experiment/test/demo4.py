import abc
import math


class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_area(self):
        raise NotImplemented("not implemented")

    @abc.abstractmethod
    def get_perimeter(self):
        raise NotImplemented("not implemented")


class Circle(Shape):
    def __init__(self, vr):
        self.r = vr

    def get_area(self):
        return self.r**2*math.pi

    def get_perimeter(self):
        return 2*math.pi*self.r


class Rectangle(Shape):
    def __init__(self, vlength, vwidth):
        self.width = vwidth
        self.length = vlength

    def get_perimeter(self):
        return 2*self.length+2*self.width

    def get_area(self):
        return self.length*self.width

    def getsomething(self):
        return self.length - self.width


class Squre(Rectangle):
    def __init__(self, vlength):
        super(Squre, self).__init__(vlength, vlength)


if __name__ == "__main__":
    circle = Circle(10)
    rectangle = Rectangle(10, 5)
    squre = Squre(10)
    shape_list = [circle, rectangle, squre]
    for i in shape_list:
        print("type:", type(i))
        print("area:", i.get_area())
        print("perimeter:", i.get_perimeter())
        if isinstance(i, Rectangle):
            print("length-width:", i.getsomething())
        print("")
