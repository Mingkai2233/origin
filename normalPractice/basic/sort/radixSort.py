import random
import sys


def radixSort(arr):
    if len(arr) < 2 or arr is None:
        return
    radixSort(arr, 0, len(arr)-1, maxbits(arr))


def maxbits(arr):
    maxNum = -(sys.maxsize-1)
    for i in arr:
        if i > maxNum:
            maxNum = i
    res = 0
    while maxNum > 0:
        res += 1
        maxNum //= 10
    return res


def getDigit(num, d):  # 当d大于当前num的最大位数时会返回0,即用0填充原来的数字
    return (num // pow(10, d-1)) % 10


def radixSort(arr, begin, end, maxbits):
    pass


list1 = [100, 10000]
print(getDigit(191, 4))