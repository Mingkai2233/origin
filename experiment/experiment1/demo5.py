a, b, c = list(map(lambda x: float(x), input("请依次输入a,b,c的值:").split(' ')))
delta = b*b - 4*a*c
if delta > 0:
    x1 = (-b+delta**0.5)/(2*a)
    x2 = (-b-delta**0.5)/(2*a)
    print("x1 = {0}\nx2 = {1}".format(x1,x2))
elif delta == 0:
    x1 = -b/(2*a)
    print("x = {0}".format(x1))
else:
    print("方程无解")