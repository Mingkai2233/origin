def bubbleSort(larr):  # 从后往前排
    length = len(larr)
    for nowPosition in range(length-1, 0, -1):
        for i in range(nowPosition):
            if larr[i] > larr[i + 1]:
                larr[i], larr[i + 1] = larr[i + 1], larr[i]
    return larr
