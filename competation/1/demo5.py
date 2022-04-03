def func(m, k, x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return m*func(m, k, x-1) - k*func(m, k, x-2)


m, k = list(map(int, input().split(" ")))
x = int(input())
print(int(func(m, k, x) % 1e9+7))
