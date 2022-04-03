x = int(input("请输入x的值:"))
result = lambda i: 2*i+1
print("x=%d" % x, '结果为:%d' % result(x))
x = int(input("请输入x的值:"))
print("x=%d" % x, '结果为:%d' % result(x))
x = int(input("请输入x的值:"))
y = int(input("请输入y的值:"))
result = lambda i, j: i*i+j*j
print("x = {0}, y = {1}时".format(x, y), '结果为:', result(x, y))
x = int(input("请输入x的值:"))
y = int(input("请输入y的值:"))
print("x = {0}, y = {1}时".format(x, y), '结果为:', result(x, y))
