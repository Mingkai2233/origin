conins = [1, 5, 10, 20, 25]
n = int(input())  # 输入找零的金额
minCoinNum = list(range(n+1))  # 默认每个金额均用对应数量的面值为1的硬币找零
lastuse = [1 for i in range(n+1)]  # 记录当前金额相比前一个金额所增加的硬币的面值
for money in range(n+1):
    coinNum = minCoinNum[money]
    for coin in [i for i in conins if i <= money]:
        if minCoinNum[money-coin]+1 <= coinNum:
            coinNum = minCoinNum[money-coin]+1
            lastuse[money] = coin
    minCoinNum[money] = coinNum
print(minCoinNum[n])

while n > 0:  # 输出所用硬币的面值
    print(lastuse[n])
    n = n-lastuse[n]