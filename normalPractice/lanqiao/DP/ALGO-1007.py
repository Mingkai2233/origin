import math
n, m = map(int, input().split())
dp = [[0 for i in range(n+1)] for j in range(m+1)]  # dp[i][j]的含义为购买第i个徽章时凑齐j种的概率
p = 1/n
for i in range(1, m+1):
    for j in range(1, n+1):
        if i < j: #
            dp[i][j] = 0
        elif j==1: # base
            dp[i][j] = p**(i-1)
        else:  # 两种情况， 第i-1次已经集齐了j种， 第i-1次集齐了j-1种
            dp[i][j] = dp[i-1][j]*j*p + dp[i-1][j-1]*(n-j+1)*p
print("%.4f"%(dp[m][n]))