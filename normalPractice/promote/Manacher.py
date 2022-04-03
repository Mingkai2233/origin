import sys


# 暴力方法:中心扩散
def manacherString(string: str) -> str:
    res = ['#']
    for i in string:
        res.append(i)
        res.append('#')
    return ''.join(res)


def centerSpread(s: str) -> int:
    if s is None:
        return 0
    if len(s) == 1:
        return 1
    s = manacherString(s)
    maxLen = 0
    for i in range(0, len(s)):
        for j in range(1, len(s)):
            if not(i-j > -1 and i+j < len(s)) or s[i-j] != s[i+j]:
                break
        if j-1 > maxLen:
            maxLen = j-1
    return maxLen


# Manacher
def manacher_original(s: str) -> int:
    if s is None or len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    C = -1
    R = -1
    s = manacherString(s)
    radius = [0 for i in range(len(s))]
    maxLen = -sys.maxsize-1

    for i in range(0, len(s)):
        if i > R:
            for j in range(1, len(s)):
                if not(i+j < len(s) and i-j > -1) or s[i+j] != s[i-j]:
                    break
            radius[i] = j
        else:
            ii = 2*C-i  # i点关于C点的对称
            if ii-radius[ii] > C-radius[C]:
                radius[i] = radius[ii]
            elif ii - radius[ii] < C - radius[C]:
                radius[i] = R-i+1
            else:
                for j in range(R-i+1, len(s)-i):
                    if not(i+j < len(s) and i-j > -1) or s[i+j] != s[i-j]:
                        break
                radius[i] = j
        if radius[i]+i > R:
            R = radius[i]+i
            C = i
        maxLen = max(maxLen, radius[i])
    print(radius)
    return maxLen-1


string = '1111'
print(manacherString(string))
print(manacher_original(string))