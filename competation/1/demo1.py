n = int(input())
# total = 0
# for i in range(1, 200):
#     total += i
#     if total-i <= n <= total:
#         print(i)
#         break
tmp = n
i = 0
while tmp > 0:
    i += 1
    tmp = tmp-i
print(i)
