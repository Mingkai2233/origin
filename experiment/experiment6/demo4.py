import math

class Vector:
    def __init__(self, vx, vy, vz):
        self.x = vx
        self.y = vy
        self.z = vz
        self.module = abs(math.sqrt(self.x**2+self.y**2+self.z**2))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return "("+str(x)+","+str(y)+","+str(z)+")"

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return "(" + str(x) + "," + str(y) + "," + str(z) + ")"

    def __mul__(self, other):
        x = self.x*other
        y = self.y*other
        z = self.z*other
        return "(" + str(x) + "," + str(y) + "," + str(z) + ")"

    def __truediv__(self, other):
        x = self.x / other
        y = self.y / other
        z = self.z / other
        return "(" + str(x) + "," + str(y) + "," + str(z) + ")"


if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(2, 3, 4)
    print(v1 + v2)
    print(v1 - v2)
    print(v1 * 3)
    print(v2 / 2)
    print(v1.module)  # 表示向量的模
