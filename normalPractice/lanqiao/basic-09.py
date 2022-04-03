def check(num: int) -> bool:
    num = list(str(num))
    stack = []
    for i in num:
        stack.append(i)
    for i in num:
        if i != stack.pop():
            return False
    return True


def getSum(num: int) -> int:
    result = 0
    while num > 0:
        result += num % 10
        num = num // 10
    return result


total = int(input())
for n in range(10000, 1000000):
    if getSum(n) == total:
        if check(n):
            print(n)
