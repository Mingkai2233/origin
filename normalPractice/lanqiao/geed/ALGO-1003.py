N, S = map(int, input().split())
weights = list(map(int, input().split()))
greed=list(range(len(weights)))
for i in range(len(weights)):
    weightsum = 0
    k = 0
    j = i
    while j >= 0 and weightsum+weights[j] <= S:
        weightsum += weights[j]
        j -= 1
        k+=1
    greed[i] = k
res = 0
for i in range(len(weights)):
    if i+greed[i] < len(weights) and i+greed[i] - greed[i+greed[i]] <= greed[i]:
        res = max(res, greed[i]*2)
print(res)