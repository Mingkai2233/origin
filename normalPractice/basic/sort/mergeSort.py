def mergeSort(arr):
    process(arr, 0, len(arr)-1)


def process(arr, left, right):
    if left == right:
        return
    mid = left + ((right-left) >> 1)  # 运算符运算顺序会影响结果
    process(arr, left, mid)  # 划分出左侧
    process(arr, mid+1, right)  # 划分出右侧
    merge(arr, left, mid, right)  # 合并


def merge(arr, left, mid, right):
    p1 = left  # 左侧部分的指针
    p2 = mid+1  # 右侧部分的指针
    tmp = []  # 用于暂存外排序结果
    while p1 <= mid and p2 <= right:  # 合并两个有序部分,并存于tmp
        if arr[p1] < arr[p2]:
            tmp.append(arr[p1])
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
    for i in range(len(tmp)):  # 拷贝回原数组
        arr[left+i] = tmp[i]
