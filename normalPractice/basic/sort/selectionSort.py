def selectionSort(arr: list):
    for i in range(len(arr)):
        minValue = arr[i]
        index = i
        for j in range(i+1, len(arr)):
            if arr[j] < minValue:
                minValue = arr[j]
                index = j
        arr[i], arr[index] = arr[index], arr[i]
    return arr