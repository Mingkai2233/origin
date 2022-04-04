n = int(input())
money = []
dp = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    money.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            dp[i][j] = money[i][j]
        elif i == 0:
            dp[i][j] = dp[i][j-1] + money[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + money[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + money[i][j]
print(dp[n-1][n-1])