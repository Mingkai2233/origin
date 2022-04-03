class A:
    def __init__(self, num1, num2):
        if num1 < num2:
            num1, num2 = num2, num1
        self.num1 = num1
        self.num2 = num2

    def f(self):
        a = self.num1
        b = self.num2
        while True:
            c = a%b
            if c == 0:
                break
            a = b
            b = c
        return b


class B(A):
    def __init__(self, num1, num2):
        super(B, self).__init__(num1, num2)

    def f(self):
        gcd = super(B, self).f()
        lcm = self.num1*self.num2/gcd
        return lcm


if __name__ == "__main__":
    a = A(6, 8)
    gcd = a.f()
    print("gcd:", gcd)
    b = B(10, 18)
    lcm = b.f()
    print("lcm:", lcm)