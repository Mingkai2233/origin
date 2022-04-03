import math

class Point():
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def setxy(self, x, y):
        self.__x = x
        self.__y = y

    def getxy(self):
        return [self.__x, self.__y]


class Circle:
    __p = None
    __radius = 1

    def __init__(self, x=0, y=0, radius=1):
        self.__p = Point(x, y)
        self.__radius = radius

    def contains(self, p: Point):
        x1, y1 = self.__p.getxy()
        x2, y2 = p.getxy()
        distance = math.sqrt(pow(x1-x2, 2)+pow(y1-y2, 2))
        distance = abs(distance)
        if distance < self.__radius:
            print("点p({0},{1})在圆内".format(x2, y2))
        else:
            print("点p({0},{1})不在圆内".format(x2, y2))


if __name__=="__main__":
    p = Point()
    circle1 = Circle()
    circle1.contains(p)

    p.setxy(5, 5)
    circle1.contains(p)

    circle2 = Circle(radius=64)
    circle2.contains(p)
