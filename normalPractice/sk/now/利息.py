k, n = map(int, input().split())
for i in range(n):
    if k <= 59:
        k += k// 10 + 5
    else:
        k += 10
print(k)