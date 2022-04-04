n, m = map(int, input().split(' '))
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
base = chars[:m]
mode = 1
tmp = 'A'
if m == 1:
    for i in range(n):
        print(chr((ord(tmp)+i)))
else:
    for row in range(1, n+1):
        print(base)
        tmp = base[:m-1]
        # if base[0] == 'A':
        #     mode = 1
        # if base[0] == chars[m-1]:
        #     mode = -1
        base = chars[(ord(tmp[0])-ord('A')+mode)%26]+tmp
