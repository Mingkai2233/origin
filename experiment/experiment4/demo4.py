import abc


class Shape(metaclass=abc.ABCMeta):
    num = 0

    def __init__(self, num):
        self.num = num

    @abc.abstractmethod
    def getAera(self):
        raise NotImplemented("not implemented")


class Circle(Shape):
    def __init__(self, r):
        super(Circle, self).__init__(r)

    def getAera(self):
        aera = 3.1415*self.num**2
        return aera


class Rectangle(Shape):
    def __init__(self, length, width):
        super(Rectangle, self).__init__(length)
        self.width = width

    def getAera(self):
        aera = self.num * self.width
        return aera


if __name__ == '__main__':
    c = Circle(4)
    print(c.getAera())
    r = Rectangle(10, 5)
    print(r.getAera())
