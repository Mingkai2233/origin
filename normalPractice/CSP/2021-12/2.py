n, N = map(int, input().split())
prices = list(map(int, input().split()))
prices.append(N)
r = N//(n+1)
pre = 0
curIndex = 0
res = 0
for i in prices:
    for j in range(pre, i):
        res+=abs(j//r - curIndex)
    pre = i
    curIndex +=1
print(res)