# 给定一个数字字符串,1对应A,2对应B,将数字字符串转化为字母字符串
def numToChar(num: str) -> int:
    return process(0, num)


def process(i: int, num: str) -> int:  # 从左往右扫描, i之前的都已经固定, 根据i位置的字符进行选择
    if i == len(num):
        return 1
    if num[i] == '0':  # 第i个为0,后续的都无法转换,直接返回0
        return 0
    if num[i] == '1':  # i自己转化或者和后边的一位一起转化
        res = process(i+1, num)
        if i+1 < len(num):
            res += process(i+2, num)
        return res
    if num[i] == '2':  # i自己转化,或者和后边的一位进行转化
        res = process(i+1, num)
        if i+1 < len(num) and ord(num[i+1]) <= ord('6'):
            res += process(i+2, num)
        return res
    return process(i+1, num)  # 当i处字符大于2时,只能自己进行转化

if __name__ == '__main__':
    numstr = '1111'
    print(numToChar(numstr))