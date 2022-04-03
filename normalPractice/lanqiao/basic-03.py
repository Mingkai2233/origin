n, m = map(int, input().split(' '))
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
base = chars[:m]
print(base)
for row in range(n-1):
    tmp = base[:m-1]
    base = chars[(ord(tmp[0])-ord('A')+1)%26]+tmp
    print(base)