
n, N = map(int, input().split())
prices = list(map(int, input().split()))
res = 0
pre = 0
curIndex = 0
for i in prices:
    cur = i
    res += (cur-pre)*curIndex
    curIndex += 1
    pre = cur
res += (N-pre)*curIndex
print(res)