n = int(input())
for i in range(10000, 1000000):
    res, num = 0, i
    while num > 0:
        res += num % 10
        num = num // 10
    if n == res:
        tmp = list(str(i))
        stack = tmp[:]
        stack.reverse()
        if stack == tmp:
            print(i)
