def findTwoNum(arr: list):
    eor = 0
    for i in arr:
        eor ^= i
    target = eor & (~eor+1)  # 假设两个数为a和b, 此时eor=a^b,当eor某位为1时,说明a和b的这一位一定不同,通过这个指标可以将原来的数分为两类,a,b各在其中一类
    eor1 = 0
    for i in arr:
        if i & target > 0:  # 将两类中的某一类全部异或起来得到ab中的一个
            eor1 ^= i  # eor为两个数中的其中一个
    eor = eor ^ eor1  # 另一个
    return eor, eor1
