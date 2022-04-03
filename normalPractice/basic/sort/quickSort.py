import random


def swap(arr, p1, p2):
    arr[p1], arr[p2] = arr[p2], arr[p1]


def partition1(arr, num):  # 把数组分成 <num 和>=num的两部分
    bound = -1
    p = 0
    while p < len(arr):
        if arr[p] <= num:
            bound += 1
            swap(arr, p, bound)
        p += 1


def partition2(arr, num):
    smallbound = -1
    bigbound = len(arr)
    p = 0
    while p < bigbound:
        if arr[p] < num:
            smallbound += 1
            swap(arr, p, smallbound)
            p += 1
        elif arr[p] > num:
            bigbound -= 1
            swap(arr, p, bigbound)
        else:
            p += 1


def partition(arr, left, right):  # 以数组最右侧的数为基准值
    smallbound = left - 1  # 左侧边界
    bigbound = right  # 右侧边界, 因为数组最右侧为基准值
    p = left  # 用于遍历的指针
    while p < bigbound:
        if arr[p] < arr[right]:
            smallbound += 1
            swap(arr, p, smallbound)
            p += 1
        elif arr[p] > arr[right]:  # 此种情况p不变,因为新换过来的元素仍需要被判断分往哪里
            bigbound -= 1
            swap(arr, p, bigbound)
        else:
            p += 1
    swap(arr, bigbound, right)  # 最后将基准值从最右侧换到大数值的边界处
    bigbound += 1
    return smallbound, bigbound


def quickSort(arr, left, right):
    if left < right:
        swap(arr, right, random.randint(left, right))  # 挑选一个基准值,并将其移到当前数组最右侧
        l, r = partition(arr, left, right)  # 进行一次划分,然后对划分出的两部分进行同样操作
        quickSort(arr, left, l)
        quickSort(arr, r, right)


list1 = [random.randint(1, 100) for i in range(10)]
print(list1, '\n')
quickSort(list1, 0, len(list1)-1)
print(list1)
