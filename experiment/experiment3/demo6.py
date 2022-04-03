from functools import reduce

def factorial(n):  # 计算n的阶乘
    list1 = list(range(1, n+1))
    return reduce(lambda x, y: x*y, list1)


n = int(input('请输入n的值:'))
nums = list(range(1, n+1))
total = reduce(lambda x, y: x+y, list(map(lambda x: factorial(x), nums)))
print(total)

