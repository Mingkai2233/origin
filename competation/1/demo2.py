def func(n: int):
    return int(n*(3*n-3)/2)


inputnum = []
n = int(input())
for i in range(n):
    inputnum.append(int(input()))
for i in inputnum:
    n = i // 3
    tmp = func(n)
    begin = 3*n+1
    for j in range(begin, i+1):
        tmp += j
    print(tmp)

