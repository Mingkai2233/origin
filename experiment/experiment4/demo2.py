class Circle:
    __x = 0
    __y = 0
    __r = 0

    @staticmethod
    def setCircle(x, y, z):
        Circle.__x = x
        Circle.__y = y
        Circle.__r = z

    @staticmethod
    def showCircle():
        print("x:", Circle.__x, "y:", Circle.__y, "r:", Circle.__r)

    @staticmethod
    def perimeterAera():
        aera = 3.1415*Circle.__r**2
        print("aera:", aera)
        perimeter = 2*3.1415*Circle.__r
        print("perimeter:", perimeter)


if __name__ == "__main__":
    circle = Circle()
    circle.setCircle(0, 0, 2)
    circle.perimeterAera()
    circle.setCircle(1, 2, 10)
    circle.perimeterAera()