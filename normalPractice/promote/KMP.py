def getNext(pat: str) -> list:
    length = len(pat)
    if length == 1:
        return [-1]
    nextArray = [0 for i in range(length)]
    nextArray[0] = -1
    nextArray[1] = 0
    for i in range(2, length):  # i为当前计算的next数组下标
        j = i-1  # j为与nextArray数组下标,对应nextArray数组的值为与i-1位置进行比较的位置下标
        while j > 0:
            if pat[nextArray[j]] == pat[i-1]:
                nextArray[i] = nextArray[j] + 1
                break
            else:
                j = nextArray[j]
        if j == 0:
            nextArray[i] = 0
    return nextArray


def KMP(txt: str, pat: str) -> int:
    if txt is None or pat is None or len(txt) < len(pat) or len(pat) < 1:
        return -1
    i = 0
    j = 0
    txtLength = len(txt)
    patLength = len(pat)
    nextArray = getNext(pat)
    while i < txtLength and j < patLength:
        if txt[i] == pat[j]:  # i和j位置匹配,两者都往后移
            i += 1
            j += 1
        elif nextArray[j] == -1:  # 模式串已经不能再回溯,主串换位置进行匹配
            i += 1
        else:  # 模式串回溯
            j = nextArray[j]

    return i-j if j == patLength else -1


pattern = "aabbbaab"
print(getNext(pattern))
text = "aaaaa"


print(KMP(text, pattern))
