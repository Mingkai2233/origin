def hexToDec(num: str):
    num = str(num)
    tmp = '0123456789ABCDEF'
    tmp = list(tmp)
    dec = 0
    length = len(num)
    for i in range(length):
        dec += tmp.index(num[length-1-i]) * 16**i
    print(dec)

data = 0
hexToDec(data)