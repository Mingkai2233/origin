import random


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


# 在本版本堆中, 大根堆的大小由heapSize控制, 和输入的数据公用一个内存
# 寻找新加入堆中数字在堆中应该处于的位置
def heapInsert(arr: list, index: int):
    while arr[index] > arr[int((index-1)/2)]:  # 隐含了index>=0的条件, 正常可以加上 index > 0
        swap(arr, index, int((index-1)/2))
        index = int((index-1)/2)


# 判断给定数字在堆中是否需要调整并调整为堆结构
def heapify(arr, index, heapSize):
    left = 2*index+1
    while left < heapSize:
        largest = left
        right = left+1
        if right < heapSize:  # 如果有右孩子, 找到左右孩子中较大的那个
            largest = left if arr[left] > arr[right] else right
        largest = index if arr[index] > arr[largest] else largest  # 找到当前当前位置,和左右孩子中值最大的
        if largest == index:  # 如果index位置数字没问题,直接退出循环
            break
        swap(arr, index, largest)  # 更换数字到合适位置
        index = largest  # 检查位置更新到需要检查数字的新位置
        left = 2 * index + 1


def heapSort1(arr):
    heapSize = 0
    for i in range(len(arr)):  # 先将数据组织成大根堆
        heapInsert(arr, i)
        heapSize += 1
    while heapSize > 0:  # 每轮pop出堆根,放置到列表某位也就是排序后的位置(记得heapSize要减小)
        heapSize -= 1
        swap(arr, 0, heapSize)
        heapify(arr, 0, heapSize)


def heapSort2(arr):
    heapSize = len(arr)
    for i in range(heapSize-1, -1, -1):  # 用小堆构成大堆,
        heapify(arr, i, heapSize)
    while heapSize > 0:
        heapSize -= 1
        swap(arr, 0, heapSize)
        heapify(arr, 0, heapSize)



nums = [1,3,2,2,1,3]
result = sorted(nums)
heapSort2(nums)
print(nums)

