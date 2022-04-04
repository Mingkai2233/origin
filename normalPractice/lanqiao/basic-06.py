n = int(input())
for i in range(1, n+1):
    cur = []
    for j in range(0, i):
        if j == 0:
            cur.append(1)
        elif j == i-1:
            cur.append(1)
        else:
            cur.append(pre[j]+pre[j-1])
    for i in cur:
        print(i, end=" ")
    print(" ")
    pre = cur


