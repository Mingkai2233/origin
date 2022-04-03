import random


# 用归并排序的思路解决小和问题
def enumeration(arr: list) -> int:  # 暴力枚举,用于验证是否正确
    res = []
    for i in range(1, len(arr)):
        tmp = 0
        for j in range(i):
            if arr[j] < arr[i]:
                tmp += arr[j]
        res.append(tmp)
    return sum(res)


def smallSum(arr):
    return process(arr, 0, len(arr)-1)


def process(arr, left, right):
    if left == right:
        return 0  # 与正常归并排序的区别
    mid = left + ((right - left) >> 1)
    return process(arr, left, mid) + process(arr, mid+1, right) + merge(arr, left, mid, right)  # 与正常归并排序的区别


def merge(arr, left, mid, right):
    p1 = left
    p2 = mid + 1
    tmp = []
    total = 0
    while p1 <= mid and p2 <= right:
        if arr[p1] < arr[p2]:
            tmp.append(arr[p1])
            total = total + (right-p2+1)*arr[p1]  # 与正常归并排序的区别
            p1 += 1
        else:
            tmp.append(arr[p2])
            p2 += 1
    while p1 <= mid:
        tmp.append(arr[p1])
        p1 += 1
    while p2 <= right:
        tmp.append(arr[p2])
        p2 += 1
    for i in range(len(tmp)):
        arr[left+i] = tmp[i]
    return total


list1 = [random.randint(1, 100) for i in range(10)]
list1 = [1, 3, 4, 2, 5]
print(list1)
print(enumeration(list1))
print(smallSum(list1))
