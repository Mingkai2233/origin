# 打印一个字符串的全部排列,要求不出现重复
def printStr(string: str):
    string = list(string)
    process(0, string)


def process(i: int, chars: list):
    if i == len(chars):
        print(''.join(chars))
    else:
        visited = [False for i in range(26)]
        for j in (range(i, len(chars))):
            if not visited[ord(chars[j])-ord('a')]:  # 分支限界,进行剪枝操作,删除不可能的分支
                visited[ord(chars[j]) - ord('a')] = True
                chars[i], chars[j] = chars[j], chars[i]
                process(i+1, chars)
                chars[i], chars[j] = chars[j], chars[i]



printStr('abb')